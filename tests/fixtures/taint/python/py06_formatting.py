# py06_formatting.py
# EXPECT: flow for all three
def handler_py06a(request, cur):
    uid = request.args["id"]
    cur.execute(f"SELECT * FROM u WHERE id={uid}")

def handler_py06b(request, cur):
    uid = request.args["id"]
    cur.execute("SELECT * FROM u WHERE id=%s" % uid)

def handler_py06c(request, cur):
    uid = request.args["id"]
    cur.execute("SELECT * FROM u WHERE id={}".format(uid))
