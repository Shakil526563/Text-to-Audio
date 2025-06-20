# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install espeak for phonemizer backend (required by VITS pipeline)
RUN apt-get update && apt-get install -y espeak-ng && rm -rf /var/lib/apt/lists/*

# Copy the rest of the app
COPY . .

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]
