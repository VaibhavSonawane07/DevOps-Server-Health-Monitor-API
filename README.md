# DevOps Server Health Monitor API

A lightweight Flask-based REST API that monitors server health metrics like CPU, Memory, and Disk usage.

Built using:
- Python
- Flask
- psutil
- Docker

---

##  Features

- CPU Usage Monitoring
- Memory Usage Monitoring
- Disk Usage Monitoring
- System Information
- JSON API Response
- Dockerized for deployment

---

##  Project Structure

```
devops-server-health-monitor/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

## ⚙️ Installation (Without Docker)

### 1. Clone the repository

```
git clone https://github.com/your-username/devops-server-health-monitor.git
cd devops-server-health-monitor
```

### 2. Create virtual environment (recommended)

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

## 🐳 Run with Docker

### 1. Build Docker Image

```
docker build -t health-monitor .
```

### 2. Run Container

```
docker run -p 5000:5000 health-monitor
```

Access API at:

```
http://localhost:5000
```

---

## 📊 Sample JSON Response

```
{
  "timestamp": "2026-02-23 12:00:00",
  "system": "Linux",
  "cpu_usage_percent": 15.4,
  "memory_usage_percent": 42.3,
  "disk_usage_percent": 68.5
}
```
## output
<img width="1854" height="1048" alt="Screenshot from 2026-02-23 15-17-48" src="https://github.com/user-attachments/assets/8ce041c8-6aa0-410f-8589-8c9202702558" />

