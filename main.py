import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="本地 GraphRAG（A 模式）：社区检测 + 摘要 + Local/Global/DRIFT 查询。"
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )
    ingest_parser = subparsers.add_parser(
        name="ingest",
        help="读取 Markdown，建立向量索引、图谱、社区检测和社区报告。"
    )
    ingest_parser.add_argument("--")
