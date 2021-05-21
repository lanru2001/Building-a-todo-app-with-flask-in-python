def get_item(item):
try:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("select status from items where item='%s'" % item)
    status = c.fetchone()[0]
    return status
except Exception as e:
    print('Error: ', e)
    return None
