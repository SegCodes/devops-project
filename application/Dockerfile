FROM python:alpine
RUN mkdir -p /application


COPY ./application /application
WORKDIR /application

EXPOSE 5000
CMD ["python3", "main.py"]