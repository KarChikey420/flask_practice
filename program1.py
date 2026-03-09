from fastapi import FastAPI
import uvicorn


@app.middleware('http')
async def middleware(request,call_next):
    print("Request before calling")
    response=await call_next(request)
    print("Request after calling")
    return response



if __name__=='__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)