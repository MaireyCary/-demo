import test_function
import test_ConnectMySQL
import test_excel
import data

# 生成课表
classes = data.get_list('classes')
for table in classes:
    # 创建班级课表
    table_name = table
    test_excel.create_xlsx(table_name)
    # 获取班级对应的教师信息
    class_name = data.get_list(table_name)
    #  
    demand = test_function.genetic_algorithm(class_name)
    # 输出排序情况
    print(demand)

    for teacher in demand:
        # 关键信息
        teacher_name = teacher[0]
        week_time = teacher[1]
        class_time = teacher[2]

        # 排课班级
        # 通过已有关键信息从数据库中提取排课信息
        schedules = test_ConnectMySQL.activate(table_name, teacher_name)

        # 调用 excel 函数将排课信息写入课表
        test_excel.excel(schedules, week_time, class_time, table_name)
