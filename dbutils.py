import cx_Oracle
import dbconfig

connStr = '%s/%s@%s' % (dbconfig.USER, dbconfig.PASS, dbconfig.SID)

def get_tables():
    with cx_Oracle.connect(connStr) as conn:
        cur = conn.cursor()
        cur.execute('SELECT owner, table_name FROM all_tables')
        return [table for owner, table in cur.fetchall()]
