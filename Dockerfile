FROM python:3.10-slim

ARG USER_ID="10001"
ARG GROUP_ID="app"
ARG HOME="/application"

RUN groupadd --gid ${USER_ID} ${GROUP_ID} && \
    useradd --create-home --uid ${USER_ID} --gid ${GROUP_ID} --home-dir /app ${GROUP_ID}

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        file        \
        gcc         \
        libwww-perl && \
    apt-get autoremove -y && \
    apt-get clean

WORKDIR ${HOME}

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ./server.py .


RUN chown -R ${USER_ID}:${GROUP_ID} ${HOME}
USER ${USER_ID}