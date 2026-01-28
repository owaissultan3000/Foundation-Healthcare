from pydantic import BaseModel

class DiagnosisBase(BaseModel):
    code: str
    description: str


class DiagnosisResponse(DiagnosisBase):
    id: int

    class Config:
        from_attributes = True
