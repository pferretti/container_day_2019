FROM python:3.7.5-alpine3.10 AS builder

RUN apk update && apk upgrade && apk add shadow build-base libffi-dev openssl-dev
RUN groupadd -g 1000 cd_user && \
    useradd -r -m -u 1000 -g cd_user cd_user

USER cd_user:cd_user
WORKDIR /home/cd_user

ADD --chown=1000:1000 ./main.py .
ADD --chown=1000:1000 ./requirements.txt .
RUN pip3 install --user -r requirements.txt

FROM python:3.7.5-alpine3.10

RUN apk update && apk upgrade && apk add shadow openssl
RUN groupadd -g 1000 cd_user && \
    useradd -r -m -u 1000 -g cd_user cd_user

USER cd_user:cd_user
WORKDIR /home/cd_user

COPY --from=builder --chown=1000:1000 /home/cd_user /home/cd_user
COPY --from=builder --chown=1000:1000 /home/cd_user/.local /home/cd_user/.local

ENV PATH="/home/cd_user/.local/bin:${PATH}"
ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]

