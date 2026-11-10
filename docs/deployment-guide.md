# Deployment Guide - SmartCRM Warranty Classification (L10)

## 1. Requirements
- Docker Desktop (Engine 24+, Docker Compose v2)
- Git
- Port 8080 must be free.

## 2. Setup steps
1. `git clone --branch v1.0 https://github.com/Hiep2374802010139/smartcrm-2374802010139-warranty-classification.git`
2. `cd smartcrm-2374802010139-warranty-classification`
3. `docker compose up -d --build`

## 3. Environment variables
| Variable | Meaning | Sample Value | Required |
| :--- | :--- | :--- | :--- |
| `LOG_LEVEL` | Logging level for the API | `INFO` | No (default: INFO) |
| `NGUONG_TIN_CAY` | Confidence threshold for prediction | `0.45` | No (default: 0.45) |

## 4. Sample data
The model is trained automatically during the Docker build using `data/issue_descriptions.csv`. No manual data loading is required.

## 5. Verify it works
1. Check container status: `docker compose ps` (STATUS must be `healthy`).
2. Test API health: `curl http://localhost:8080/health` -> expected `{"status":"ok","phien_ban_mo_hinh":"1.0.0"}`
3. Test prediction: 
   `curl -X POST http://localhost:8080/du-doan -H "Content-Type: application/json" -d "{\"mo_ta\": \"Màn hình bị sọc\"}"`
   -> expected JSON with predicted label `MAN_HINH`.
4. Run tests (if configured inside Docker): `docker compose exec model python -m pytest -q` -> expected `10 passed`.