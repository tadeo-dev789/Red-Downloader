# 🎬 Red Downloader

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A powerful, containerized full-stack application to download YouTube videos and audio efficiently within a local network. Built with a modern **React** frontend and a robust **FastAPI** backend, fully orchestrated with **Docker**.

---

## 🚀 Key Features

* **🎥 Audio:** Support for high-quality MP3 audio extraction.
* **🐳 Fully Dockerized:** Deploy the entire stack (Frontend, Backend, Nginx) with a single command.
* **⚡ High Performance:** Backend processing using FastAPI and `yt-dlp`.
* **📱 Responsive UI:** Clean interface built with React and Vite.

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | React, Vite, Nginx |
| **Backend** | Python, FastAPI, yt-dlp |
| **DevOps** | Docker, Docker Compose |
| **OS** | Linux / Windows Compatible |

## 📦 Installation & Usage

Prerequisites: Make sure you have **Docker Desktop** installed.

1.  **Clone the repository**
    ```bash
    git clone https://github.com/tadeo-dev789/Red-Downloader.git
    cd Red-Downloader
    ```

2.  **Run with Docker Compose**
    Build and start the containers:
    ```bash
    docker-compose up --build
    ```

3.  **Access the App**
    Open your browser and go to:
    > `http://localhost` (Frontend)

## 📂 Project Structure

```text
Red-Downloader/
├── docker-compose.yml      # Orchestration config
├── backend/                # FastAPI Microservice
│   ├── Dockerfile
│   ├── main.py             # App Entry point
│   └── requirements.txt    # Dependencies
├── frontend/               # React UI
│   ├── Dockerfile
│   ├── nginx.conf          # Reverse Proxy config
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── App.jsx         # Main Component
│       ├── components/     # UI Components (Chakra/Tailwind)
│       └── assets/         # Images & SVGs
└── downloads/              # Mounted volume for media
