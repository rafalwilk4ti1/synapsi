import secrets
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials


safety = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(safety)):
    correct_username = secrets.compare_digest(credentials.username, "wilkrafal")
    correct_password = secrets.compare_digest(credentials.password, "password123")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


app = FastAPI()


@app.get("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}


class Item(BaseModel):
    text: str
    key = int


@app.get("/items/encode")
async def encode(text: str, key: int):
    """Function to decode plain text/sentence"""
    storage = ""  # We create an empty string
    for x in text:
        number = ord(x)  # Iterate text and converting each element to unicode character
        number += key  # Change number value to be equal with rot47
        if number < 32:  # Checking if number is between characters that is used in rot47
            number += 32
        elif number > 126:
            number = (number - 126) + 32
        storage += chr(number)  # Encoded text in string unicode
    return {text: storage}


@app.get("/items/decode")
async def decode(text: str, key: int):
    """Function to decode our encoded text/sentence"""
    storage = ""
    for x in text:  # Iterate text and converting each element to unicode character
        number = ord(x)  # Change number value to be able decode text
        number -= key  # Changing value to normal case sensitive
        if number < 32:  # checking value to make sure that our letter will be decoded in good way
            number = 126 - (32 - number)
        storage += chr(number)  # Making string with decoded message

    return {text: storage}
