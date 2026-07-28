from storage import save_session

def finish(duration):

    save_session({

        "duration": duration

    })
