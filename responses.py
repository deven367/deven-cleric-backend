
from typing import List, Optional

from pydantic import BaseModel


class GetQuestionAndFactsResponse(BaseModel):
    question: str
    facts: Optional[List[str]]
    status: str


class SubmitQuestionAndDocumentsResponse(BaseModel):
    question: str
    documents: List[str]