FROM python:3.6
MAINTAINER Priya A <prananth@microsoft.com>
ADD news.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
ENV FLASK_APP=news.py
CMD [ "python", "./news.py" ]