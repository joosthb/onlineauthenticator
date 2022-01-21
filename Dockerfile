FROM python:3.9-alpine

RUN apk add --no-cache zbar

# to compile Pillow
RUN apk add --no-cache zlib-dev jpeg-dev gcc musl-dev

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
