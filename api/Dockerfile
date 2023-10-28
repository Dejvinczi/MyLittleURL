FROM python:3.11

WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ./

RUN chmod +x start.sh
CMD ["/bin/sh", "start.sh"]