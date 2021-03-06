FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8


ARG USER=fastapi_example
ARG WORKDIR=/app

WORKDIR $WORKDIR

RUN groupadd -f -g 1000 $USER && useradd -m $USER --gid 1000 && chown -R $USER:$USER $WORKDIR

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY --chown=$USER:$USER ./pyproject.toml ./poetry.lock* /app/

COPY --chown=$USER:$USER .env .

RUN poetry install --no-root --no-dev

COPY --chown=$USER:$USER src/ .

ENV MODULE_NAME="fastapi_best_practice.main"


