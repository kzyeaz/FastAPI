from fastapi import FastAPI, HTTPException
import os
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
async def health_check():
    health_status = {"status": "healthy"}
    return JSONResponse(content=health_status, status_code=200)

@app.get("/hello")
async def name(VALUE: str=None):
    if VALUE is None:
        raise HTTPException(status_code = 400S, detail="Query parameter name is not specified")
    input_value = {"message": f"Hello {VALUE}"}
    return JSONResponse(content=input_value, status_code=200)

@app.get("/")
async def root():
    raise HTTPException(status_code = 404, detail = "Not Found")

'''if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)'''
