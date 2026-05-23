from user import user_list
from score import score_list
from course import course_list

# 修改用户密码
def change_password(user_id, old_password, new_password):
    for user in user_list:
        if user["user_id"] == user_id:
            if user["password"] == old_password:
                user["password"] = new_password
                return True, "密码修改成功"
            return False, "原密码输入错误"
    return False, "该用户不存在"

# 获取用户基础资料
def get_user_basic_info(user_id):
    for user in user_list:
        if user["user_id"] == user_id:
            return {
                "user_id": user["user_id"],
                "username": user["username"]
            }
    return None

# 获取个人学习统计数据
def get_personal_statistics(user_id):
    my_scores = [s for s in score_list if s["user_id"] == user_id]
    relate_course_ids = set()
    for s in my_scores:
        relate_course_ids.add(s["course_id"])
    my_courses = [c for c in course_list if c["course_id"] in relate_course_ids]

    if my_scores:
        score_data = [item["score"] for item in my_scores]
        avg_score = sum(score_data) / len(score_data)
        max_score = max(score_data)
        min_score = min(score_data)
    else:
        avg_score = 0
        max_score = 0
        min_score = 0

    stat_result = {
        "study_course_count": len(my_courses),
        "exam_count": len(my_scores),
        "average_score": round(avg_score, 2),
        "highest_score": max_score,
        "lowest_score": min_score,
        "my_course_list": my_courses,
        "my_score_list": my_scores
    }
    return stat_result