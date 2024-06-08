FROM python:3.9-alpine

RUN apk update \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev postgresql-client

WORKDIR /src

COPY requirements.txt /src/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /src/

# RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stocks_products.wsgi:application"]