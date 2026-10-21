from dataclasses import dataclass
from pathlib import Path
import os
from dotenv import load_dotenv

@dataclass(frozen=True)
class Settings:
    """
    运行 GraphRAG pipeline 所需的配置。
    配置集中在一个对象里，目的是避免 API Key、模型名、Neo4j 密码等值散落在
    业务代码中。后续如果要切换模型或换文档目录，只需要改 `.env` 或命令行参数。
    """
    docs_dir: Path
    doc_files: list[str] | None
    chroma_dir: Path
    chroma_collection: str
    entity_collection: str
    siliconflow_api_key: str
    siliconflow_base_url: str
    siliconflow_chat_model: str
    siliconflow_embedding_model: str
    siliconflow_embedding_dimensions: int | None
    neo4j_uri: str
    neo4j_username: str
    neo4j_password: str
    chunk_size: int
    chunk_overlap: int
    top_k: int
    graph_hops: int
    community_min_size: int
    global_min_score: int
    embedding_batch_size: int
    log_level: str
    siliconflow_timeout: float
    siliconflow_max_retries: int
