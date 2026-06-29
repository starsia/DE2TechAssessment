#!/usr/bin/env bash

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

(
    crontab -l 2>/dev/null
    echo "0 * * * * /bin/bash \"$PROJECT_ROOT/scripts/run_pipeline.sh\""
) | crontab -

echo "Cron job installed."