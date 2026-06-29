#!/usr/bin/env bash

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RUN_SCRIPT="/bin/bash \"$PROJECT_ROOT/scripts/run_pipeline.sh\""


crontab -l 2>/dev/null | grep -Fv "$RUN_SCRIPT" | crontab -

echo "Cron job removed."