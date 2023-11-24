# syntax=docker/dockerfile:1
FROM tiangolo/uvicorn-gunicorn:python3.11

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

WORKDIR /app

# copy app source as last step prevents rebuilding the whole image on code update.
COPY . .

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]