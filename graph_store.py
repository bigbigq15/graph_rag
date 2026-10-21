from dataclasses import dataclass
from neo4j import GraphDatabase


@dataclass(frozen=True)
class EntityRecord:
    """从图谱里取出的实体，用于社区检测和 Local Search。"""
    normalized_name: str
    name: str
    type: str
    community_id: int | None = None


class Neo4jGraphStore:
    def __init__(self, *, uri: str, username: str, password: str) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self) -> None:
        self.driver.close()
