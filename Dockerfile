FROM python:3.10

RUN pip install fastapi uvicorn[standard]

WORKDIR /app/
COPY main.py ./

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
