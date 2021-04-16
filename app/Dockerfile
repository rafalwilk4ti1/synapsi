FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip3 install uvicorn
RUN pip3 install fastapi

COPY . /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0","--port","80"]
