# py07_container.py
# EXPECT: flow   (hypothesis: Joern MISSES this; if so it is a recorded limitation)
def handler_py07(request, cur):
    d = {"k": request.args["id"]}
    cur.execute(d["k"])
