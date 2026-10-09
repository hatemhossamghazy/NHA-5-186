# py01_direct.py
# EXPECT: flow
def handler(request, cur):
    uid = request.args["id"]
    q = "SELECT * FROM u WHERE id=" + uid
    cur.execute(q)
