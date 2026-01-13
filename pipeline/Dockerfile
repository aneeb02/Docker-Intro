FROM python:3.12.1-slim

RUN pip install --no-cache-dir pandas pyarrow fastparquet

WORKDIR /app
COPY pipeline.py /app/pipeline.py