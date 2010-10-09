import cx_Oracle
import dbconfig

connStr = '%s/%s@%s' % (dbconfig.USER, dbconfig.PASS, dbconfig.SID)

with cx_Oracle.connect(connStr) as conn:
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM D_CARRIL_PM_2008_01')
    for s in cur.fetchall():
        print s
