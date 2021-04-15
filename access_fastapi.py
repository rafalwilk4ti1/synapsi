import os
import secrets

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

safety = HTTPBasic()


def authorize(credentials: HTTPBasicCredentials = Depends(safety)):
    user = secrets.compare_digest(credentials.username, os.getenv('Login'))
    password = secrets.compare_digest(credentials.password, os.getenv('Password'))

    if not (user and password):
        raise HTTPException( status_code=status.HTTP_401_UNAUTHORIZED,
                             detail='Your login or password is wrong.',
                             headers={'WWW-Authenticate': 'Basic'})


app = FastAPI(openapi_url='/api/access/openapi.json', docs_url='/api/access/docs')

@app.get('/api/access/auth', dependencies=[Depends(authorize)])
def auth():
    return {'Granted': True}

