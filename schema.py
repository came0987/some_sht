from typing import Dict, List, Optional
from pydantic import BaseModel

class Node(BaseModel):
    id: str
    type: str
    params: Dict = {}

class Edge(BaseModel):
    from_: str
    to: str
    target_handle: Optional[str]

    class Config:
        fields = {"from_": "from"}

class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]
