# 📘 Quotes API – FastAPI (Single File Version)

A simple REST API built with **FastAPI** and **SQLite** that allows you to create, read, search, and get random inspirational quotes.

---

## 🚀 Features

- Create a new quote (text + author)
- Fetch all quotes
- Get quote by ID
- Search quotes by author name
- Get a random quote

---

## 🧠 Tech Stack

- **FastAPI** – Web framework
- **SQLite** – Lightweight embedded database
- **SQLAlchemy** – ORM for Python
- **Uvicorn** – ASGI server

---

## 🛠️ Installation

### 1. Clone or copy the project:

```bash
git clone https://github.com/yourusername/quotes-api-fastapi.git
cd quotes-api-fastapi
```

### 2. Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy
```

### 3. Run the app:

```bash
uvicorn main:app --reload
```

---

## 📂 API Endpoints

| Method | Endpoint                      | Description             |
| ------ | ----------------------------- | ----------------------- |
| POST   | `/quotes`                   | Create a new quote      |
| GET    | `/quotes`                   | Get all quotes          |
| GET    | `/quotes/{quote_id}`        | Get quote by ID         |
| GET    | `/quotes/search?author=xyz` | Search quotes by author |
| GET    | `/quotes/random`            | Get a random quote      |

---

## 📄 Example Request & Response

### ✅ Create Quote

**POST** `/quotes`

```json
{
  "text": "Stay hungry, stay foolish.",
  "author": "Steve Jobs"
}
```

**Response**

```json
{
  "id": 1,
  "text": "Stay hungry, stay foolish.",
  "author": "Steve Jobs"
}
```

---

## 🧪 Testing via Swagger

Once running, go to:

📎 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Use the Swagger UI to test the API visually.

---

## 📌 Notes

- The project uses SQLite and stores data in `quotes.db` in the current directory.
- It’s built in **a single file** for simplicity. Great for learning and small projects.
- All responses are in JSON format.

---

## 📦 Future Improvements

- JWT authentication
- Like/favorite quotes
- Pagination for large result sets
- Docker support

---

## 👨‍💻 Team

**Amar Murmu**, **Pramod Kumar**, **Manish Kumar**
