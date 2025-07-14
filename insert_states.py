
from database import SessionLocal, State

states_data = [
    {"id": 1, "name": "cairo"},
    {"id": 2, "name": "giza"},
    {"id": 3, "name": "alexandria"},
    {"id": 4, "name": "aswan"},
    {"id": 5, "name": "luxor"},
    {"id": 6, "name": "port said"},
    {"id": 7, "name": "suez"},
    {"id": 8, "name": "sharm el-sheikh"},
    {"id": 9, "name": "hurghada"},
    {"id": 10, "name": "mansoura"}
]

def insert_states():
    db = SessionLocal()
    for state in states_data:
        db_state = State(id=state["id"], name=state["name"])
        db.add(db_state)
    db.commit()
    db.close()

if __name__ == "__main__":
    insert_states()
    print("States inserted successfully!")
