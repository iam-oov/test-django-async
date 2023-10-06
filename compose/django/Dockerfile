FROM python:3
ENV PYTHONUNBUFFERED 1

ENV APP_DIR=/src/app

WORKDIR $APP_DIR

RUN useradd valdo && chown valdo:valdo -R $APP_DIR \
  && apt-get update \
  && apt-get install -y supervisor \
  && pip install "setuptools<58.0.0" \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ["requirements/base.txt", "."]

RUN pip install -r base.txt

COPY [".", "."]

COPY ["compose/django/start.sh", "/start.sh"]
RUN chmod +x /start.sh && chown valdo:valdo /start.sh

# establecer el usuario para la ejecucion del contenedor
USER valdo
