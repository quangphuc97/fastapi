from fastapi import HTTPException
def http_exception_not_found():
    raise HTTPException(status_code=404, detail="Item not found")