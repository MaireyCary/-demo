classes = ['软件技术1班', '软件技术2班']
class1 = [
    {"name": "汪卫星", "days": ["周一", "周二", "周三", "周四", "周五"], "performance": "高"},
    {"name": "张丽英", "days": ["周一", "周二", "周三", "周四", "周五"], "consecutive": "4节连排"},
    {"name": "肖小红", "days": ["周一", "周二", "周三", "周四", "周五"], "consecutive": "4节连排"},
    {"name": "徐健", "days": ["周一", "周二", "周三", "周四", "周五"]}
]
class2 = [
    {"name": "卢益博", "days": ["周一", "周二", "周三", "周四", "周五"]},
    {"name": "邹国霞", "days": ["周一", "周二", "周三", "周四", "周五"]},
    {"name": "肖小红", "days": ["周一", "周二", "周三", "周四", "周五"]},
    {"name": "薛云兰", "days": ["周一", "周二", "周三", "周四", "周五"]}
]

def get_list(list_name):
    if list_name == "classes":
        return classes
    elif list_name == "软件技术1班":
        return class1
    elif list_name == "软件技术2班":
        return class2
    else:
        return "List not found"
