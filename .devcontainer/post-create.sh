#!/bin/bash

set -e

echo "🚀 Initializing development environment..."

# Initialize project if pyproject.toml doesn't exist
if [ ! -f "pyproject.toml" ]; then
    echo "📝 Initializing Python project..."
    uv python pin 3.13
    uv init
fi

# Python virtual environment setup
echo "📦 Setting up Python virtual environment..."

# Create virtual environment only if it doesn't exist
if [ ! -d ".venv" ]; then
    uv venv --python 3.13
fi

uv sync

echo "✅ Development environment setup complete!"