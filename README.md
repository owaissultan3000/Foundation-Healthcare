# Foundation Healthcare Assessment

A simple full-stack application consisting of:
- **Backend API** (FastAPI + PostgreSQL)
- **Frontend** (Vue 3 + Vite)
- **Dockerized setup** using Docker Compose

---

## Project Structure

```
├── backend/
│ ├── app/
│ │ ├── main.py # FastAPI entry point
│ │ ├── routes/ # API routes
│ │ ├── models/ # Database models
│ │ ├── schemas/ # Pydantic schemas
│ │ └── service/ # Busniess Logic
| | └── utils/ # Utility functions
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/
│ ├── src/
│ │ ├── views/ # Pages (Login, Register, Consultations)
│ │ ├── router/ # Vue router & guards
│ │ └── services/ # API calls (Axios)
│ ├── vite.config.js
│ └── Dockerfile
│
├── docker-compose.yml
└── README.md
```


---

## How to Run

### Prerequisites
- Docker
- Docker Compose

---

### Run the Application

From the project root:

```bash
docker-compose up --build


### Access the App

Frontend: http://localhost:5173

Backend API: http://localhost:8000

API Docs (Swagger): http://localhost:8000/docs

```

### Notes

- Frontend uses Vue 3 with Ant Design Vue

- Backend uses FastAPI with PostgreSQL

- Authentication is JWT-based

- Route guards handle login/register access
