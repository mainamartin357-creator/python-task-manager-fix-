FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure test scripts are executable
RUN chmod +x tests/*.sh solution/*.sh

CMD ["bash"]
