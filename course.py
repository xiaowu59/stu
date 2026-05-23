# course.py 课程管理模块
course_list = []
course_id_auto = 1

# 添加课程
def add_course(course_name, teacher, credit):
    global course_id_auto
    new_course = {
        "course_id": course_id_auto,
        "course_name": course_name,
        "teacher": teacher,
        "credit": credit
    }
    course_list.append(new_course)
    course_id_auto += 1
    return True

# 查询所有课程
def get_all_course():
    return course_list

# 根据课程ID查询单门课程
def get_course_by_id(cid):
    for course in course_list:
        if course["course_id"] == cid:
            return course
    return None

# 修改课程信息
def update_course(cid, name, teacher, credit):
    course = get_course_by_id(cid)
    if course:
        course["course_name"] = name
        course["teacher"] = teacher
        course["credit"] = credit
        return True
    return False

# 删除课程
def delete_course(cid):
    global course_list
    course_list = [c for c in course_list if c["course_id"] != cid]
    return True