import uvicorn 
from fastapi import FastAPI


app =FastAPI()

@app.get('/')
def index():
    return {'message':'Hello Students, How are you!!'}

@app.get('/name')
def printNaam():
    return {'message':'Hello Rohitpreet'}


if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)
    
# uvicorn file_name:objectname --reload 