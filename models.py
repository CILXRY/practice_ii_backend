from sqlalchemy import Column, Integer, String, Text, JSON
from database import Base


class QuestionDB(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    question_text = Column(Text, nullable=False)
    answer_list = Column(JSON, nullable=False)
    answer_cor = Column(String)
    from_source = Column(String)
    analysis = Column(Text)
