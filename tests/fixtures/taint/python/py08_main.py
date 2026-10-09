# py08_main.py
# EXPECT: flow   (hypothesis: uncertain, cross-file via import)
from py08_helper import build

def handler_py08(request, cur):
    cur.execute(build(request.args["id"]))
