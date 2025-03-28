# Lucid_test

This project is a FastAPI-based web application that includes authentication and post management features. It integrates SQLAlchemy for database management, provides token-based authentication, and uses caching to optimize the retrieval of posts.

## Project Structure

```plaintext
project_root/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   ├── crud.py
│   ├── dependencies.py
│   ├── caching.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── posts.py
│   ├── config.py
│
├── requirements.txt
└── README.md
```

 ## Installation
To set up and run the project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/BileichukIvan/lucid_test.git
cd lucid_test
```
2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows, use 
```bash 
venv\Scripts\activate
```
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```
4. Set up environment variables by creating a .env file in the project root:

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
CACHE_EXPIRY=300
```
5.Run the FastAPI application:
```
bash
uvicorn app.main:app --reload
```