from pydantic import BaseModel, Field
from typing import Annotated


class Review(BaseModel):
    review: Annotated[int | None, Field(ge=1, le=5)] = None