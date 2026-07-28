import json

from storage import load_sessions

def export():

    with open(

        "data/exports/report.json",

        "w"

    ) as f:

        json.dump(load_sessions(), f, indent=4)
