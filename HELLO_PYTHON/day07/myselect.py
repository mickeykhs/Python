import mysql.connector # DB연동에 필요한 모듈 추가
from mysql.connector import errorcode # DB 연동 시 Error 체크 

# mysql/mariaDB 환경변수
config = {
    'user':'root',
    'password':'python', #임의의 *로 가린겁니다
    'host':'127.0.0.1',
    'database':'python',
    'port':'3305'
}

try:
    # db 연결 객체 생성
    conn = mysql.connector.connect(**config)
    # SQL 실행 객체 생성
    cursor = conn.cursor()

    sql = "select * from emp"
    cursor.execute(sql) #sql문 실행
    
    #insert, update, delete는 execute()이후 커밋을 해야 적용됨
    #conn.commit()

    res = cursor.fetchall()
    for row in res:
        print(row)

# DB 연결 예외 처리
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('id or password 오류')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('db 연동 오류')
    else:
        print('기타 에러:', err)
    conn.rollback() # 롤백 처리
finally:
    cursor.close(); conn.close() # 연결 객체 닫기