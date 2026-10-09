# py03_helper_return.py
# EXPECT: flow   (tainted value goes through a DEFINED helper and comes back)
def wrap(s):
    return "'" + s + "'"

def handler_py03(request, cur):
    name = wrap(request.args["name"])
    cur.execute("SELECT * FROM u WHERE n=" + name)
