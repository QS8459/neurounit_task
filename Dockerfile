FROM python:3.11-alpine

RUN apk update && apk add --no-cache bash busybox-suid tzdata supervisor nano

#     rm --rf /var/cache/apk/*
ENV TZ=America/New_York
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY . .

COPY requirements.txt .

RUN mkdir -p /var/log/cron/
RUN chmod -R 777 /var/log
RUN touch /var/log/cron/cron.log
RUN chown -R root:root /var/log/cron/cron.log
RUN chmod -R 664 /var/log/cron/cron.log
RUN chmod +x cronjob.sh

COPY supervisord.conf /etc/supervisord.conf
COPY --chown=root:root cronfile /etc/crontabs/root

RUN chmod 600 /etc/crontabs/root

ENV NE_PG_HOST=neuro_db
ENV NE_PG_DB=neurounit
ENV NE_PG_USER=neuro
ENV NE_PG_PASSWD=unit
ENV NE_PG_PORT=5432
ENV NE_PG_URI=postgresql+asyncpg://${NE_PG_USER}:${NE_PG_PASSWD}@${NE_PG_HOST}:${NE_PG_PORT}/${NE_PG_DB}

RUN pip install -r requirements.txt

EXPOSE 7100

#CMD ["supervisord", "-c", "/etc/supervisord.conf"]
CMD ["tail", "-f","/dev/null"]