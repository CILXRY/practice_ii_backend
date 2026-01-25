from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import database, models, schemas
from sqlalchemy import func

app = FastAPI(title="答题系统 API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4321", "http://127.0.0.1:4321"],  # Astro 默认端口
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 创建数据库表 (如果不存在)
models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Still alive."}


@app.get("/question/get_question", response_model=List[schemas.Question])
def get_questions(category: str, limit: int = 10, db: Session = Depends(get_db)):
    """
    获取指定分类的题目
    - **category**: 题目分类 (如 '数学')
    - **limit**: 获取数量 (默认10)
    """
    questions = (
        db.query(models.QuestionDB)
        .filter(models.QuestionDB.category == category)
        .order_by(func.random())
        .limit(limit)
        .all()
    )

    if not questions:
        raise HTTPException(status_code=404, detail="未找到该分类的题目")

    return questions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,      # ❌ 关闭自动重载
    )