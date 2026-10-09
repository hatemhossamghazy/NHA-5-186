# py08_helper.py
# EXPECT: (helper module for py08_main.py, no handler)
def build(uid):
    return "SELECT * FROM u WHERE id=" + uid
