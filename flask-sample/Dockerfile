FROM python:3.9

WORKDIR /app

COPY ./app /app

RUN pip install Flask
RUN pip install -U PyMySQL #今回使うモジュール(DBエンジン)

CMD ["python", "index.py"]