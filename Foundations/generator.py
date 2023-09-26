# iterator generator eg a remote control system
def remote_control_next():
    yield "TV West"
    yield "CNN"
    yield "NTV"
    yield "BBC"
    yield "UBC"
    yield "St Kungu fu"
    yield "Bukedde"

itr = remote_control_next()
next(itr)