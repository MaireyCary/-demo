import pymysql

# 定义需要查询的数据库库列表信息
class CourseSchedule:
    def __init__(self, class_name, course_name, weekly_hours, start_end_week, venue_requirement, teacher, scheduling_willingness):
        self.class_name = class_name
        self.course_name = course_name
        self.weekly_hours = weekly_hours
        self.start_end_week = start_end_week
        self.venue_requirement = venue_requirement
        self.teacher = teacher
        self.scheduling_willingness = scheduling_willingness

# 定义数据库连接信息
class DatabaseConnection:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connect(self):
        return pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)

# 定义查询语句
def read_course_schedules_by_table_name(db_connection, table_name, teacher_name):
    course_schedules = []
    conn = db_connection.connect()
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT class_name, course_name, weekly_hours, start_end_week, venue_requirement, teacher, scheduling_willingness FROM `{table_name}` WHERE teacher = '{teacher_name}'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                course_schedule = CourseSchedule(*row)
                course_schedules.append(course_schedule)
    finally:
        conn.close()

    return course_schedules

# 定义激活函数
def activate(table_name, teacher_name):
    # 数据库连接信息
    db_info = DatabaseConnection(host='localhost', user='root', password='123456', db='arrangeclassdata')
    # 执行查询并获取课程表信息
    schedules = read_course_schedules_by_table_name(db_info, table_name, teacher_name)
    # 返回CourseSchedule对象列表
    return schedules
