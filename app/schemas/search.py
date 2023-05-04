

from pydantic import BaseModel, PositiveInt, conint


class SkipLimit(BaseModel):
    skip: conint(ge=0) = 0
    limit: PositiveInt = 20