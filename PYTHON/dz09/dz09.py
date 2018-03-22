import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute("SELECT Host,User FROM user")
for response in cur:
    print(response)
cur.close()
conn.close()
