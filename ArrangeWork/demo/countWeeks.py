from connectMySQL import peoples_on_duty
from data import choiceWeek

# 定义人员值班问题的参数
peoples = peoples_on_duty

# 分配人员到各周次
def assign_people_to_weeks(peoples):
    # 定义所有周次和时间段
    all_weeks = ['13周', '14周', '15周', '16周', '17周']
    for week in all_weeks:
        all_days_periods = choiceWeek(week)

        # 创建一个字典来存储每周的人员时间段列表
        schedule = {week: {day: {period: [] for period in all_days_periods[day]} for day in all_days_periods} for week
                    in all_weeks}
        # 创建一个字典来跟踪每个人员在每周是否已经被安排过
        arranged = {person.name[0]: {week: False for week in all_weeks} for person in peoples}

        # 遍历每个排班周次
        for current_week in all_weeks:
            all_days_periods = choiceWeek(current_week)
            # 遍历每个工作日
            for day, periods in all_days_periods.items():
                # 遍历每个时间段
                for period in periods:
                    # 初始化当前时间段的人员列表
                    current_period_people = []
                    # 遍历每个人员
                    for person in peoples:
                        # 如果该人员在这周和下周都没有被安排过，则尝试安排
                        if (current_week not in arranged[person.name[0]] or arranged[person.name[0]][
                            current_week] is False) and \
                                (current_week != '14周' or not arranged[person.name[0]].get('13周', False)) and \
                                (current_week != '15周' or not arranged[person.name[0]].get('14周', False)) and \
                                (current_week != '16周' or not arranged[person.name[0]].get('15周', False)) and \
                                (current_week != '17周' or not arranged[person.name[0]].get('16周', False)):

                            if current_week in person.weeks and person.relax_day != f"{day}{period}":
                                # 检查当前时间段是否已经排满两个人
                                if len(current_period_people) < 2:
                                    # 安排该人员
                                    current_period_people.append(person.name[0])
                                    arranged[person.name[0]][current_week] = True  # 标记该人员在这周已经被安排过
                    # 将当前时间段的人员列表添加到日程表中
                    if current_period_people:
                        schedule[current_week][day][period] = current_period_people

    return schedule

# 打印并返回排班结果
def print_and_return_schedule(schedule):
    for week, week_info in schedule.items():
        if week_info:  # 如果该周次有人值班
            print(f"{week}:")
            for day, periods in week_info.items():
                if periods:  # 如果该天有人值班
                    print(f"  {day}:")
                    for period, people in periods.items():
                        if people:  # 如果该时间段有人值班
                            print(f"    {period}:")
                            for person in people:
                                print(f"      {person}")

# 运行分配算法，并打印结果，返回排班字典
final_schedule = assign_people_to_weeks(peoples)
print_and_return_schedule(final_schedule)
