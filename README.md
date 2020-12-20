# Used Stack
### Python
### FastAPI
### SqlAlchemy

# How To Start

### Clone the repository

```bash
git clone https://github.com/MykolaZ12/backend-hackathon.git
```

### Install requirements
```bash
pip install -r requirements.txt
```

### In config/ directory create local_config.py and fill by exemple
```bash
SECRET_KEY = "SECRET"

EMAILS_FROM_NAME = "Desired Name"
EMAILS_FROM_EMAIL = "your@email.com"

SMTP_HOST = "your mail server"
SMTP_PORT = port
SMTP_TLS = True
SMTP_USER = "your@email.com"
SMTP_PASSWORD = "strong_password"

```

### Create migrations & run migrations
```bash
alembic revision --autogenerate
alembic upgrade head
```

### Start project
```bash
uvicorn main:app --reload
```