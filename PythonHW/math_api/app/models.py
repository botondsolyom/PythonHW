# Aici verificam input-ul, il returnam JSON structure of the output

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OperationRequest(BaseModel):
    type: str
    input1: float
    input2: Optional[float] = None  # numai pentru pow trebuie


class OperationResult(BaseModel):
    operation: str
    result: float
    timestamp: datetime
