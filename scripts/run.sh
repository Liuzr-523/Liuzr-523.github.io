#!/usr/bin/env bash
# 便捷运行器：优先使用已装好依赖（pycryptodome / markdown）的 Python
# 用法示例：
#   scripts/run.sh scripts/encrypt_private.py liuzirui 密码
#   scripts/run.sh scripts/audit_apply.py "<申请密文>"
#   scripts/run.sh scripts/gen_apply_page.py

set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PY="/Users/liuzirui/.workbuddy/binaries/python/envs/default/bin/python"
if [ ! -x "$PY" ]; then
  PY="python3"
fi

cd "$DIR/.."
exec "$PY" "$@"
