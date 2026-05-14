from pydantic import BaseModel
from typing import Literal


class IncidentRequest(BaseModel):

    service: str
    severity: Literal["Critical", "High", "Medium", "Low"]
    issue: str
    status: str