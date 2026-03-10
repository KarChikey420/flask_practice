from fastapi import FastAPI
import uvicorn
app=FastAPI()





if __name__=='__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)