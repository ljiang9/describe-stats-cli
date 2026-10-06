"""命令行：python3 cli.py numbers.txt（每行一个数 或 逗号分隔）"""
import argparse
import json
import sys

from stats import describe


def _load(file: str) -> list[float]:
    with open(file, encoding="utf-8") as f:
        text = f.read()
    parts = text.replace(",", "\n").splitlines()
    return [float(x) for x in parts if x.strip()]


def main(argv=None):
    p = argparse.ArgumentParser(description="describe-stats-cli 描述统计")
    p.add_argument("file", help="数据文件，每行一个数或逗号分隔")
    p.add_argument("--json", action="store_true")
    args = p.parse_args(argv)
    try:
        values = _load(args.file)
    except FileNotFoundError:
        print(f"错误：文件不存在 {args.file}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(describe(values), ensure_ascii=False, indent=2))
    else:
        d = describe(values)
        for k, v in d.items():
            print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
