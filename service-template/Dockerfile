# ---------- build stage ----------
FROM python:3.12-slim AS build
WORKDIR /code
COPY pyproject.toml poetry.lock* /code/
RUN pip install --no-cache-dir poetry==1.8.2 \
 && poetry config virtualenvs.create false \
 && poetry install --only main --no-root --no-interaction

COPY service-template/src /code/src
RUN python -m compileall -q /code/src

# ---------- runtime ----------
FROM gcr.io/distroless/python3-debian12:nonroot
WORKDIR /app
COPY --from=build /code /app
ENTRYPOINT ["python", "-m", "app.main"]
