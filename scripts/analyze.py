#!/usr/bin/env python3
import os, re
from datetime import datetime
DATA_DIR = "data"
REPORT = "data/report.md"
def parse_status(text):
    info = {}
    for line in text.strip().split("\n"):
        if "=" in line:
            k, v = line.split("=", 1)
            info[k.strip()] = v.strip()
    return info
def main():
    path = os.path.join(DATA_DIR, "status.txt")
    if not os.path.exists(path):
        open(REPORT, "w").write("# 暂无数据\n")
        return
    with open(path) as f:
        current = parse_status(f.read())
    with open(REPORT, "w") as out:
        out.write("# 雅库茨克 SDR 站报告\n\n")
        out.write(f"更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M UTC')}\n\n")
        out.write(f"- 离线：{current.get('offline', '?')}\n")
        out.write(f"- 用户：{current.get('users', '?')}/{current.get('users_max', '?')}\n")
        out.write(f"- 名称：{current.get('name', '?')}\n")
        out.write(f"- GPS：{current.get('gps', '?')}\n")
if __name__ == "__main__":
    main()
