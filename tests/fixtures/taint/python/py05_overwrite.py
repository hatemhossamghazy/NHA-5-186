# py05_overwrite.py
# EXPECT: no-flow   (negative control: the tainted value is overwritten before the sink)
def handler_py05(request, cur):
    q = request.args["id"]
    q = "SELECT 1"
    cur.execute(q)
