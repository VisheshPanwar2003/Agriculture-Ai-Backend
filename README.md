🌱 AgriSense AI – Smart Agriculture Assistant

"🚀 Live Demo" (https://agriculture-ai-frontend.vercel.app/)

AgriSense AI is an AI-powered agriculture platform designed to help farmers make informed decisions through crop analysis, disease detection, weather insights, agricultural guidance, and intelligent chatbot support. The platform combines Google's Gemini AI with modern web technologies to provide real-time agricultural assistance through an intuitive user interface.

---

🚀 Features

🤖 AI Agriculture Chatbot

- Agriculture-specific AI assistant
- Crop management guidance
- Pest and disease recommendations
- Farming best practices
- Fertilizer and irrigation suggestions

🌿 Crop Disease Analysis

- Upload crop or plant images
- AI-powered disease detection
- Plant health assessment
- Severity analysis
- Treatment recommendations

🌦 Weather Intelligence

- Real-time weather information
- Farming-specific weather insights
- Agricultural recommendations based on weather conditions

📅 Agricultural Almanac

- Seasonal farming guidance
- Crop planning support
- Agricultural calendar assistance

🔐 Authentication System

- User registration
- Secure login system
- JWT-based authentication
- Personalized user experience

📊 Smart Analysis Tools

- Crop health analysis
- Agricultural recommendations
- AI-generated farming insights

---

🛠 Tech Stack

Frontend

- React.js
- Vite
- Tailwind CSS
- Axios
- React Router DOM
- Framer Motion

Backend

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT Authentication
- Passlib (Password Hashing)
- Python Multipart (File Uploads)
- Uvicorn (ASGI Server)
- Python Dotenv
- CORS Middleware

AI & Machine Learning

- Google Gemini 2.5 Flash
- Google GenAI SDK
- Pillow (Image Processing)

Deployment

- Vercel (Frontend)
- Render / Railway / Docker (Backend)
- PostgreSQL
- GitHub

---

📁 Project Structure

AgriSense-AI/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── middleware/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── .env
│   └── alembic/
│
└── README.md

---

⚙️ Installation

Clone Repository

git clone https://github.com/your-username/agrisense-ai.git

cd agrisense-ai

---

Backend Setup

cd backend

python -m venv venv

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

---

Environment Variables

Create a ".env" file inside the backend folder.

PORT=8000

DATABASE_URL=postgresql://username:password@localhost:5432/agrisense_ai

JWT_SECRET=your_jwt_secret

GEMINI_API_KEY=your_gemini_api_key

WEATHER_API_KEY=your_weather_api_key

---

Run Backend

Development

uvicorn app.main:app --reload

Production

uvicorn app.main:app --host 0.0.0.0 --port 8000

Backend URL

http://localhost:8000

Interactive API Documentation

http://localhost:8000/docs

ReDoc Documentation

http://localhost:8000/redoc

---

Frontend Setup

cd frontend

npm install

npm run dev

Frontend URL

http://localhost:5173

---

📡 API Endpoints

Authentication

POST /api/auth/register

POST /api/auth/login

GET  /api/auth/profile

Chatbot

POST /api/chatbot

Vision Analysis

POST /api/vision/analyze

Weather

GET /api/weather

Almanac

GET /api/almanac

Smart Analysis

POST /api/analysis

---

📸 Vision AI Workflow

1. Upload crop image.
2. Image processed using Python Multipart and Pillow.
3. Gemini Vision analyzes the image.
4. Detects plant diseases and health issues.
5. Provides severity assessment.
6. Generates treatment recommendations.

---

🗄 Database

AgriSense AI uses PostgreSQL as its primary database.

Stores

- User accounts
- Authentication details
- Chat history
- Crop analysis history
- Disease detection reports
- User preferences

Database migrations are managed using Alembic, while SQLAlchemy provides ORM support for efficient database interactions.

---

🔒 Security

- JWT Authentication
- Password hashing using Passlib (bcrypt)
- Environment variables for API keys
- FastAPI security middleware
- CORS protection
- Request validation using Pydantic
- Sensitive credentials excluded using ".gitignore"

---

🌍 Future Enhancements

- Multi-language support
- Voice-enabled farming assistant
- Crop yield prediction
- Market price forecasting
- Farm management dashboard
- Mobile application
- IoT sensor integration

---

👨‍💻 Author

Vishesh Panwar

AI & Full Stack Developer

---

📜 License

This project is developed for educational, research, and portfolio purposes.
