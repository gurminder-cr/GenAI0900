# pip install uvicorn fastapi 
import uvicorn 
from fastapi import FastAPI
from input import getData

app =FastAPI()
    
# get, post, update, delete 
@app.get('/')
def index():
    return {'message':'Hello Students, How are you!!'}

@app.get('/name')
def printNaam():
    return {'message':'Hello Karanpreet'}

# @app.get('/{name}')
# def getName(name:str):
#     return {'Name is':f'{name}'}
# @app.post('/{name}')
# def getName(name:str):
#     return {'Name is':f'{name}'}

@app.post('/getname')
def getName(data:getData):
    dict_data= data.model_dump() #Export the model instance to a dictionary
    print(dict_data)
    
    return dict_data




# to run fastapi - uvicorn filename:objectname --reload

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
    
    