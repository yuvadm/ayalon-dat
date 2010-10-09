import cx_Oracle
import dbconfig

connStr = u'%s/%s@%s' % (dbconfig.USER, dbconfig.PASS, dbconfig.SID)

conn = cx_Oracle.connect(connStr)

conn.close()
