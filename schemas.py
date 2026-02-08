from pydantic import BaseModel, ConfigDict
from typing import Dict, Any


class Question(BaseModel):
    category: str
    question_text: str
    answer_list: Dict[str, Any]
    answer_cor: str
    from_source: str
    analysis: str
    model_config = ConfigDict(from_attributes=True)


class ResponseAns(BaseModel):
    response_id: str
    ans: str
