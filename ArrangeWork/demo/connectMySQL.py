import pymysql

class PersonOnDuty:
    def __init__(self, weeks, relax_day, name):
        # 将字符串转换为列表
        self.weeks = [week.strip() for week in weeks.split('、') if week.strip()]
        self.relax_day = relax_day
        self.name = [name.strip() for name in name.split('、') if name.strip()]

class DatabaseConnection:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connect(self):
        return pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)

def read_people_on_duty(db_connection, table_name):
    people_on_duty = []
    conn = db_connection.connect()
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT * FROM `{table_name}`"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                person_on_duty = PersonOnDuty(*row)
                people_on_duty.append(person_on_duty)
    finally:
        conn.close()
    return people_on_duty

def activate(table_name):
    db_info = DatabaseConnection(host='localhost', user='root', password='123456', db='arrangeworkdata')
    peoples = read_people_on_duty(db_info, table_name)
    return peoples

# 使用激活函数并传入表名
table_name = '纪检排班'
peoples_on_duty = activate(table_name)

# 打印查询结果
# for person in peoples_on_duty:
#     print(f"Weeks: {person.weeks}, Relax Day: {person.relax_day}, Name: {person.name}")
