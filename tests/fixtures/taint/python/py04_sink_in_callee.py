# py04_sink_in_callee.py
# EXPECT: flow   (the sink is INSIDE the callee: argument -> parameter)
def run(cur, q):
    cur.execute(q)

def handler_py04(request, cur):
    uid = request.args["id"]
    run(cur, "SELECT * FROM u WHERE id=" + uid)
