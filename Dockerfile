FROM python:3.8.8-slim

ENV PYTHONUNBUFFERED=1 \
    BINANCE_TICKER=BTCUSDT \
    FTX_TICKER=BTC-PERP \
    REFRESH_RATE=0.01 \
    PRICE_DIFFERENCE=50 \
    MARGIN=1000

RUN mkdir -p /app/

RUN python -m pip install --upgrade pip \
    && pip install poetry==1.1.11 \
    && poetry config virtualenvs.create false

WORKDIR /app/

COPY env.list pyproject.toml poetry.lock /app/
RUN poetry install

COPY ./robo_arb/ /app/

CMD [ "python", "/app/app.py" ]
