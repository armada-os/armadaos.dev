preview:
    #!/usr/bin/env bash
    set -euo pipefail
    if command -v podman >/dev/null 2>&1; then
        RUNTIME=podman
    elif command -v docker >/dev/null 2>&1; then
        RUNTIME=docker
    else
        echo "Error: neither podman nor docker is installed" >&2
        exit 1
    fi
    "$RUNTIME" run --rm -it -p 8000:8000 -v "${PWD}:/docs:Z" docker.io/squidfunk/mkdocs-material
