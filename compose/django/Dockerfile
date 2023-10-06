FROM python:3
ENV PYTHONUNBUFFERED 1
ENV APP_PROJ=/src/app

WORKDIR $APP_PROJ

RUN useradd valdo && chown valdo:valdo -R $APP_PROJ
RUN apt-get update && apt-get install -y supervisor
RUN pip install "setuptools<58.0.0"

COPY ["requirements/base.txt", $APP_PROJ]
RUN pip install -r requirements/base.txt

COPY [".", $APP_PROJ]

COPY compose/django/start.sh /start.sh
RUN chmod +x /start.sh && chown valdo:valdo /start.sh
USER valdo
