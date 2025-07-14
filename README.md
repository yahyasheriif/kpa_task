KPA Form Data Backend Assignment

Project Overview
This project implements two APIs from the KPA Form Data collection:
- *POST /login*: User login via phone number and password.
- *GET /states*: Fetch all states from the PostgreSQL database.

The APIs demonstrate:
- Authentication with request validation.
- Database interaction using SQLAlchemy and PostgreSQL.
- Proper response structure as per API documentation.

Tech Stack
- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn

Setup Instructions

1. Clone the repository:
bash
git clone https://github.com/yahyasheriif/kpa_task/
cd kpa_task


2. Create and activate virtual environment:
bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows


3. Install dependencies:
bash
pip install -r requirements.txt


4. Setup PostgreSQL database:
- Create a database named `kpa_db`.
- Update the `DATABASE_URL` in your code if necessary.

5. Insert initial data (states):
bash
python insert_states.py


6. Run the server:
bash
uvicorn main:app --reload


7. Test the APIs using Postman:
- POST /login with JSON body:
[7:42 pm, 14/07/2025] Chat Gpt: json
{
  "phone": "7760873976",
  "password": "to_share@123"
}


- GET /states to get all states.

Key Features Implemented
- User login authentication with validation.
- Fetching states data from PostgreSQL.
- Proper response format.
- Asynchronous API endpoints.

Limitations / Assumptions
- Login uses hardcoded credentials.
- No token or session management.
- Basic database operations only.
- No file uploads or complex features.
