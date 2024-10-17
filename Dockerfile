# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/data

# Copy the Python script and the text files into the container
COPY script.py /home/data/script.py
COPY IF.txt /home/data/IF.txt
COPY AlwaysRememberUsThisWay.txt /home/data/AlwaysRememberUsThisWay.txt

# Install any required dependencies (if needed, none required here)
RUN pip install --no-cache-dir --upgrade pip

# Run the Python script when the container starts
CMD ["python", "script.py"]
