# 🌈 Gaali API

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)

**A FastAPI-based Random Gaali Generator API**

</div>

## 📋 About

Gaali API is a simple FastAPI application that serves random "gaali" (Hindi slang) from a MongoDB database. It provides a single endpoint that returns a random gaali in JSON format.

## ✨ Features

- 🚀 **FastAPI Powered** - Built with FastAPI for high performance
- 📊 **MongoDB Integration** - Stores and retrieves data from MongoDB
- 🔄 **Random Selection** - Returns a random gaali on each request
- 📝 **Auto-generated Swagger docs** - Interactive API documentation

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/0xmainak/gaali-api.git

# Navigate to the project directory
cd gaali-api

# Install dependencies
pip install fastapi uvicorn python-dotenv pymongo

# Set up environment variables in .env file
MONGO_URI=your_mongodb_connection_string

# Start the server
uvicorn main:app --reload
```

## 🚀 Quick Start

```python
# Python client example
import requests

response = requests.get('http://localhost:8000/')
data = response.json()
print(data)
```

Response format:
```json
{
  "gaali": "example_gaali"
}
```

## 📘 API Documentation

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Returns a random gaali |

For complete API documentation, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📄 License

This project is licensed under the MIT License.

<div align="center">
  <sub>Built with FastAPI + MongoDB</sub>
</div>
