from fastapi import FastAPI


app=FastAPI()

@app.get('/')
def get_root():
    return {'data':{'name':'akhil'}}

@app.get('/about')
def get_about():
    return {'data':{"about-page"}}