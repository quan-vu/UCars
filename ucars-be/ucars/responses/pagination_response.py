from typing import List
from pydantic import BaseModel


class PaginationResponse(BaseModel):
    total: int
    limit: int
    offset: int = 0
    total_page: int
    next_page_link: str = None
    data: List = []
