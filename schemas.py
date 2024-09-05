from pydantic import BaseModel

class GeneralPayload(BaseModel):
    topic: str



class AnalyzePayload(BaseModel):
    content: str

