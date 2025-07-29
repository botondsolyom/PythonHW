# 1. Base image - Python 3.11
FROM python:3.11-slim

# ODBC driver installing for SQL Server
RUN apt-get update && \
    apt-get install -y curl gnupg2 apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev gcc g++ && \
    rm -rf /var/lib/apt/lists/*

# 2. New folder inside the container
WORKDIR /app

# 3. Copying files from computer to container
COPY ./app ./app
COPY requirements.txt .

# 4. Installing the packages
RUN pip install --no-cache-dir -r requirements.txt

# 5. Open the port
EXPOSE 8000

# 6. Running the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]