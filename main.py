import argparse
from pathlib import Path


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
    ingest_parser.add_argument(
        "--docs-dir",
        type=Path,
        help="覆盖 .env 中的 DOCS_DIR。"
    )
    ingest_parser.add_argument(
        "--files",
        help="只处理指定 Markdown，多个文件用英文逗号分隔。"
    )
    query_parser = subparsers.add_parser(
        name="query",
        help="向 GraphRAG 知识库提问。"
    )
    query_parser.add_argument(
        "question",
        help="要问的问题"
    )
    query_parser.add_argument(
        "--mode",
        choices=["local", "global", "drift"],
        default="local",
        help=(
            "检索模式："
            "local 适合实体相关的具体问题；"
            "global 适合全局聚合/主题性问题；"
            "drift 先 global 再 local，适合既要全局又要细节的问题。"
        ),
    )
    query_parser.add_argument(
        "--top-k",
        type=int,
        help="覆盖 .env 中的 TOP_K。")

    return parser


