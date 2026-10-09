# py02_constant.py
# EXPECT: no-flow (negative control: source read but never reaches the sink)
def handler(request, cur):
    uid = request.args["id"]
    q = "SELECT 1"
    cur.execute(q)
