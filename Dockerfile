FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system --deploy

EXPOSE 5432

CMD [ "python", "api.py" ]
