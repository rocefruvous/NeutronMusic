# Neutron Music
this is a uni project with deadline of less than a month

# Deployment Guide
> [!WARNING]
> This project has many flaws and it's not recommended to be used outside just playing around.

### 1. Clone the Repository
```bash
git clone https://github.com/rocefruvous/NeutronMusic.git
cd NeutronMusic
```
### 2. Create Environment File

Create a .env file inside the backend directory.

Example:

```env
SECRET_KEY=change-me
DEBUG=False
```

The .env file is intentionally excluded from Git.

### 3. Build Containers
```bash
docker compose build
```

### 4. Start Services
```bash
docker compose up -d
```

Check that containers are running:

```bash
docker compose ps
```

### 5. Run Database Migrations
Only required if database models have changed.

```bash
docker compose exec web python manage.py migrate
```

### 6. Access Application

Backend:
http://localhost:8000

Frontend:
http://localhost:3000
