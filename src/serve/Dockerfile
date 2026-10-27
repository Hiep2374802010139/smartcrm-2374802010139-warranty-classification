FROM python:3.11-slim AS runtime
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m -u 10001 app
COPY src ./src
COPY artifacts/model_v1.joblib ./artifacts/model_v1.joblib
USER app

ENV MODEL_PATH=artifacts/model_v1.joblib NGUONG_TIN_CAY=0.45
EXPOSE 8080
HEALTHCHECK --interval=10s --timeout=3s --start-period=30s --retries=6 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8080/health').status==200 else 1)"
CMD ["uvicorn", "src.serve.app:app", "--host", "0.0.0.0", "--port", "8080"]