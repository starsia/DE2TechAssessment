#!/usr/bin/env bash

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

cd "$PROJECT_ROOT"

source "$PROJECT_ROOT/myenv/bin/activate"

export PYTHONPATH="$PROJECT_ROOT/src"

python -m data_pipelines.pipeline