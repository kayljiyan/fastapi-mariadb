from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi import HTTPException


class SampleError(HTTPException):
    """
    Base template for future exceptions
    """

    def __init__(self) -> None:
        message = ""
        super().__init__(status_code=400, detail=message)
