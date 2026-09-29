from hashlib import sha256
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


def _versioned_url(url, docs_dir):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return url

    content = (Path(docs_dir) / parts.path).read_bytes()
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
    return config
