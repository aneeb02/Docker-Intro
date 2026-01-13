FROM python:3.12.1-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app
COPY pyproject.toml  .python-version uv.lock ./
RUN uv sync --locked 

RUN pip install --no-cache-dir pandas pyarrow fastparquet

COPY pipeline.py /app/pipeline.py

ENTRYPOINT ["uv", "run", "python", "pipeline.py"]