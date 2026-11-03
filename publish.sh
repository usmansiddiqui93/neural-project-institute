#!/bin/bash
# Usage: publish.sh "commit message" rwname [rwname...]
set -e
MSG="$1"; shift
cd /home/claude/npi
exec 9>/home/claude/npi/.publish.lock; flock 9
python3 check.py "$@"
cd /home/claude/neural-project-institute && git pull -q --rebase origin main
cd /home/claude/npi && python3 render.py "$@"
cd /home/claude/neural-project-institute
git add -A
git -c user.name=usmansiddiqui93 -c user.email=usmansiddiqui93@users.noreply.github.com commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01GC7wxL6T35chhC2tPCPCwB"
git push -q origin main
git log --oneline -1
# back up tooling and content files
cd /home/claude/npi && git add -A && (git -c user.name=usmansiddiqui93 -c user.email=usmansiddiqui93@users.noreply.github.com commit -q -m "Backup: $MSG" || true) && git push -q origin npi-tools
