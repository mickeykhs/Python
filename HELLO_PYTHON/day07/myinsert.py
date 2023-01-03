import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()
sql = """INSERT INTO emp (e_id, e_name, sex, addr) VALUES(%s,%s,%s,%s)"""
cnt = curs.execute(sql,('3','3','3','3'))
print("cnt" , cnt)
# curs.execute(sql,('3','3','3','3'))
# print("cnt" , curs.rowscount) 이런방법도 있다.
conn.commit()
curs.close()
conn.close()