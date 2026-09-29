import re
from hashlib import sha256
from html import escape, unescape
from pathlib import Path
from urllib.parse import parse_qsl, unquote, urlencode, urljoin, urlsplit, urlunsplit


def _versioned_url(url, docs_dir, asset_path=None):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or not parts.path:
        return url

    content = (Path(docs_dir) / unquote(asset_path or parts.path)).read_bytes()
    version = sha256(content).hexdigest()[:12]
    query = [
        (key, value)
        for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if key != "v"
    ]
    query.append(("v", version))
    return urlunsplit(parts._replace(query=urlencode(query)))


def on_config(config):
    config.extra_css = [_versioned_url(url, config.docs_dir) for url in config.extra_css]
    for index, script in enumerate(config.extra_javascript):
        if isinstance(script, str):
            config.extra_javascript[index] = _versioned_url(script, config.docs_dir)
        else:
            script.path = _versioned_url(script.path, config.docs_dir)
    for key in ("logo", "favicon"):
        if config.theme.get(key):
            config.theme[key] = _versioned_url(config.theme[key], config.docs_dir)
    return config


def on_page_content(html, page, config, files):
    def version_image(match):
        url = unescape(match[3])
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:
            return match[0]

        asset_path = urljoin(page.url, parts.path).lstrip("/")
        if files.get_file_from_path(unquote(asset_path)) is None:
            return match[0]

        versioned = _versioned_url(url, config.docs_dir, asset_path)
        return f"{match[1]}{match[2]}{escape(versioned, quote=True)}{match[2]}"

    return re.sub(
        r"(<img\b[^>]*?\ssrc\s*=\s*)([\"'])(.*?)\2",
        version_image,
        html,
        flags=re.IGNORECASE,
    )
