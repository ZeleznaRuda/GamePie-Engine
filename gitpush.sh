#!/bin/sh


cd "$(dirname "$0")"


if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Použití: $0 \"commit message\" remote_url"
    exit 1
fi


git status
git add .
git commit -m "$1"
git pull origin main --rebase
git push "$2" main

