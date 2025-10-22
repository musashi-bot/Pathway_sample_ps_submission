FROM python:3.10-slim
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y gcc
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code and input files
COPY . /app

# Run the app
CMD ["python", "app.py"]
