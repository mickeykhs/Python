import pymysql 

e_id = "3"
e_name = "5"
sex = "5"
addr = "5"
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
 
curs = conn.cursor()
sql = f"""
    update emp
    set e_name='{e_name}',
        sex='{sex}',
        addr='{addr}'
    where
        e_id= '{e_id}'
"""
print(sql)
cnt = curs.execute(sql)
print("cnt" , cnt)
# curs.execute(sql,('3','3','3','3'))
# print("cnt" , curs.rowscount) 이런방법도 있다.

conn.commit()
curs.close()
conn.close()