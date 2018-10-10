FROM python:3-alpine
MAINTAINER Maciej Strzelecki "strzelecki.maciek@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.pip
EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0" ]
