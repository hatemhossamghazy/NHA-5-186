# py10_tainted_receiver.py
# EXPECT: no-flow   (tainted object is the RECEIVER, the argument is constant;
#                    checks that argument(1) really restricts the sink)
def handler_py10(request, cur):
    conn = request.args["c"]
    conn.execute("SELECT 1")
