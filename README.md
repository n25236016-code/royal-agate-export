# Royal Agate Export

Royal Agate Export is a React/Vite storefront backed by Django REST Framework.

## Project layout

- `backend/`: Django project, feature apps, configuration, logs, static files, tests, and SQLite database directory.
- `frontend/`: React application and Vite build configuration.
- `docs/`: requirements, workflows, and API documentation.

## Local development

Install backend dependencies with `python -m pip install -r backend/requirements.txt`. Copy `backend/.env.example` to `backend/.env`, then run `python backend/manage.py migrate` and `python backend/manage.py runserver 0.0.0.0:8000`.

In a second terminal, run `npm install` and `npm run dev` from `frontend/`. The Fly deployment instructions are in `DEPLOYMENT.md`.
