# describe-stats-cli

描述统计命令行小工具。均值/中位数/众数/方差/分位数/偏态，文件输入。零第三方依赖。

## 功能

- 均值、中位数、众数；
- 方差、标准差；
- P25 / P75 分位数；
- 偏态（皮尔逊）。

## 快速开始

把数据写入文件（每行一个数，或逗号分隔）：

```bash
printf "1\n2\n3\n4\n5\n" > numbers.txt
python3 cli.py numbers.txt
```

## 无 API Key 如何运行

本工具**完全不需要 API Key**。

## 目录结构

```
describe-stats-cli/
├── stats.py      # 描述统计计算
├── cli.py        # 文件输入入口
├── tests/test_stats.py
├── README.md / LICENSE / .gitignore
```

## 测试

```bash
python3 -m unittest discover -s tests
```

## 许可证

[MIT](./LICENSE)
