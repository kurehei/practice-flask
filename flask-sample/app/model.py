import pymysql.cursors

def get_user_info(id):
    connect = pymysql.connect(host='flask-sample_db_1',
                            port=3306,
                            password='password',
                            user='root',
                            db='main',
                            cursorclass=pymysql.cursors.DictCursor)

    with connect.cursor() as cursor:
        sql = "SELECT * FROM user WHERE id = " + id
        cursor.execute(sql)
        results = cursor.fetchall()

    connect.close()
    return results