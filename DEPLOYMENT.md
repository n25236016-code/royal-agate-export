# Royal Agate Export Deployment Guide

# Royal Agate Export Deployment Guide

## Fly.io: frontend and API together

The Fly configuration builds React and Django into one service. Production browser requests use the same-origin `/api/v1` path, avoiding the deployed `localhost` URL and cross-origin configuration. SQLite persists on a Fly volume mounted at `/data`.

Run once from the project root to create the volume and configure Django secrets:

```powershell
fly volumes create data --region sin --size 1
fly secrets set DJANGO_SECRET_KEY="<long-random-secret>" JWT_SIGNING_KEY="<a-different-long-random-secret>"
```

Then deploy with:

```powershell
fly deploy
```

The app listens on port 8080, runs migrations at startup, and uses `/api/health/` for its health check. `fly.toml` configures the app name and allowed hostname. Do not commit production secrets or `.env` files.

Generate each secret locally with `python -c "import secrets; print(secrets.token_urlsafe(48))"` and use different values.

## Local development

Run Django from `backend/` with `python manage.py runserver 0.0.0.0:8000` and Vite from `frontend/` with `npm run dev`. The local frontend `.env` may point to `http://localhost:8000/api/v1`; Fly builds use `/api/v1` on the same origin.

## Separate frontend and backend hosting

For separate hosting platforms, set `VITE_API_BASE_URL` to the backend's full `/api/v1` URL and configure the backend's `CORS_ALLOWED_ORIGINS` with the frontend origin. Keep production secrets in the hosting platform's secret store and use PostgreSQL for non-Fly deployments.
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
