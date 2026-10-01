import json
from html import escape
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "videos.json"
LANGUAGES = {
    "de": "German",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "it": "Italian",
    "ko": "Korean",
    "pt": "Portuguese",
    "ru": "Russian",
    "uk": "Ukrainian",
}


def _url(video):
    return f"https://www.youtube.com/watch?v={video['id']}"


def _channel(video):
    return (
        f'<a class="armada-videos__channel" href="{escape(video["channel_url"], quote=True)}" '
        f'target="_blank" rel="noopener">{escape(video["channel"])}</a>'
    )


def _language(video):
    code = video["language"]
    return f'<span class="armada-videos__lang" lang="en">{escape(LANGUAGES.get(code, code))}</span>'


def _card(video):
    title = escape(video["title"])
    return "\n".join([
        "<li>",
        f'<a href="{_url(video)}" target="_blank" rel="noopener">',
        f'<img src="https://i.ytimg.com/vi/{video["id"]}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">',
        f'<span class="armada-videos__title" lang="{video["language"]}" title="{title}">{title}</span>',
        "</a>",
        f'<span class="armada-videos__meta">{_channel(video)} {_language(video)}</span>',
        "</li>",
    ])


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "project/videos/index.md":
        return markdown

    videos = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    return "\n".join([
        markdown.rstrip(),
        "",
        '<ul class="armada-videos" role="list">',
        *map(_card, videos),
        "</ul>",
        "",
    ])
