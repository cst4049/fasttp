from pydantic import BaseModel, Field


class Response(BaseModel):
    """响应信息"""
    code: int = Field(..., title='响应码')
    msg: str = Field(..., title='响应信息')
    data: dict = Field(..., title='响应数据')
