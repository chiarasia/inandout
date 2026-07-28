import json
import os

FILE = "data/sessions.json"

def load_sessions():

    if not os.path.exists(FILE):

        return []

    with open(FILE) as f:

        return json.load(f)

def save_session(session):

    data = load_sessions()

    data.append(session)

    with open(FILE, "w") as f:

        json.dump(data, f, indent=4)
