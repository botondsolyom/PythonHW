# Aici primim cererea de calcul de la client, o procesam si o inregistram in jurnal. (logging)

from fastapi import APIRouter, HTTPException
from app.models import OperationRequest, OperationResult
from app.logic import calc_pow, calc_factorial, calc_fibonacci
from app.database import SessionLocal, OperationLog
from datetime import datetime


router = APIRouter()


@router.post("/calculate", response_model=OperationResult)
def calculate(op: OperationRequest):
    db = SessionLocal()
    try:
        if op.type == "pow":
            result = calc_pow(op.input1, op.input2)
        elif op.type == "factorial":
            result = calc_factorial(int(op.input1))
        elif op.type == "fibonacci":
            result = calc_fibonacci(int(op.input1))
        else:
            raise HTTPException(status_code=400, detail="Unknown operation type")

        log = OperationLog(
            operation=op.type,
            input1=op.input1,
            input2=op.input2,
            result=result
        )
        db.add(log)
        db.commit()
        db.refresh(log)

        return OperationResult(operation=op.type, result=result, timestamp=log.timestamp)
    finally:
        db.close()
