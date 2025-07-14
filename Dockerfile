# Dockerfile
FROM python:3.13.2

# Set work directory
WORKDIR /app

#copy
COPY . .


# Run
RUN pip install -r requirements.txt

#port
EXPOSE 5000


# Entrypoint command
CMD ["python", "main.py"]
