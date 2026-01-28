from typing import List
from pydantic import BaseModel
from datetime import datetime

class PaginationMeta(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int

class ConsultationCreate(BaseModel):
    patient_name: str
    notes: str
    diagnosis_code_id: int


class ConsultationResponse(BaseModel):
    id: int
    patient_name: str
    notes: str
    diagnosis_code_id: int
    diagnosis_code: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True
    
class ConsultationListResponse(BaseModel):
    data: List[ConsultationResponse]
    pagination: PaginationMeta
