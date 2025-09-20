#!/bin/sh

# Check if all arguments are provided
if [ $# -lt 3 ]; then
    echo "Usage: $0 project_folder \"commit message\" remote_url"
    exit 1
fi

PROJECT_DIR="$1"
COMMIT_MSG="$2"
REMOTE="$3"

# Change to project folder
if [ -d "$PROJECT_DIR" ]; then
    cd "$PROJECT_DIR" || { echo "Failed to change to folder $PROJECT_DIR"; exit 1; }
else
    echo "Folder $PROJECT_DIR does not exist"
    exit 1
fi

# Remove __pycache__ directories and .pyc files
echo "Deleting __pycache__ directories and .pyc files..."
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete

# Add __pycache__ and .pyc to .gitignore if not already present
if ! grep -q "__pycache__/" .gitignore 2>/dev/null; then
    echo "__pycache__/" >> .gitignore
fi
if ! grep -q "*.pyc" .gitignore 2>/dev/null; then
    echo "*.pyc" >> .gitignore
fi

# Git workflow
git status
git add .
git commit -m "$COMMIT_MSG"
git pull origin main --rebase
git push "$REMOTE" main

