from pydantic import BaseModel
class BaseResponse(BaseModel):
    message: str
    statuc_code: str