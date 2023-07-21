FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y cron python3 python3-pip vim 

WORKDIR /home
RUN mkdir /home/crawlers
COPY crawlers /home/crawlers
COPY Pipfile Pipfile.lock start_cron.sh  /home/

RUN pip install pipenv
RUN pipenv install --system --deploy

RUN chmod +x /home/start_cron.sh

CMD "/home/start_cron.sh"