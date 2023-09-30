FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache


# Copy the rest of your application code
COPY . /app


# Set the entrypoint for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]