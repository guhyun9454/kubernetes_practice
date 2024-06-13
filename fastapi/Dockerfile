FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["fastapi", "run", "main.py", "--port", "8000"]