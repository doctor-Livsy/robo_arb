FROM python:3.8.8-windowsservercore-1809

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --upgrade pip \
    && pip install poetry==1.1.11 \
    && poetry config virtualenvs.create false \
    && cd /usr/src/app \
    && poetry install

COPY robo_arb/. ./robo_arb

CMD [ "python", "./robo_arb/app.py" ]
