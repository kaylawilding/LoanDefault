from pydantic import BaseModel

class LoanData(BaseModel):
    Gender: str
    year: int
    loan_amount: float
