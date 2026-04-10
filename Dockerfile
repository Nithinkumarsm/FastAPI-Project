#Docker file for FAST API project

FROM python:3.10-slim 

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# This Dockerfile sets up a container for a FastAPI project. It uses the official Python 3.10 slim image, sets the working directory to /app, copies the requirements.txt file, installs the dependencies, copies the rest of the application code, exposes port 8000, and runs the FastAPI application using Uvicorn.