FROM python:alpine

# Copy files
RUN mkdir -p /application
COPY . /application

# Install dependencies
RUN pip install -r application/requirements.txt

# Run app
WORKDIR /application

EXPOSE 5000
CMD ["python3", "main.py"]