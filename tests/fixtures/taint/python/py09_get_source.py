# py09_get_source.py
# EXPECT: flow   (tests the .get() source pattern)
def handler_py09(request, cur):
    uid = request.args.get("id")
    cur.execute("SELECT * FROM u WHERE id=" + uid)
