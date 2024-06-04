from flask import Flask, request, jsonify
import MySQLdb

app = Flask(__name__)

# 데이터베이스 연결
def get_db_connection():
    connection = MySQLdb.connect(
        user='root',
        password='12345',
        database='point_class'
    )
    return connection

# 등급별 사용자 조회 함수
def get_users_by_class(point_class):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        if point_class == '브론즈':
            cursor.execute("SELECT name FROM class WHERE point < 500")
        elif point_class == '실버':
            cursor.execute("SELECT name FROM class WHERE point >= 500 AND point < 1000")
        elif point_class == '골드':
            cursor.execute("SELECT name FROM class WHERE point >= 1000 AND point < 1500")
        elif point_class == 'VIP':
            cursor.execute("SELECT name FROM class WHERE point >= 1500")

        result = cursor.fetchall() # 데이터베이스 쿼리 결과 가져오고, 'fetchall()'는 쿼리의 모든 결과 행을 반환.
        users = [row[0] for row in result] # 각 행의 첫번째 값을 추출하여 'users'리스트를 생성. 튜플로 반환.

        if users:
            response_text = f"{point_class} 등급의 사용자: " + ", ".join(users) # users리스트에 있는 사용자 이름들을 쉼표로 구분하여 문자열로 만듦.
        else:
            response_text = f"{point_class} 등급의 사용자가 없습니다."

    except Exception as e:
