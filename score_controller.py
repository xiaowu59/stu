from service.score_service import ScoreService

class ScoreController:
    def __init__(self):
        self._score_service = ScoreService()

    def insert_score(self):
        print("\n--- 录入成绩 ---")
        student_name = input("请输入学生姓名: ")
        subject = input("请输入科目名称: ")
        try:
            score_value = float(input("请输入分数(0-100): "))
            self._score_service.add_score(student_name, subject, score_value)
            print("✅ 成绩录入成功！")
        except ValueError as e:
            print(f"❌ 录入失败: {e}")

    def display_all_scores(self):
        print("\n--- 所有成绩列表 ---")
        scores = self._score_service.get_all_scores()
        if not scores:
            print("📋 暂无成绩记录")
            return
        for score in scores:
            print(f"ID: {score.score_id} | 学生: {score.student_name} | 科目: {score.subject} | 分数: {score.score_value}")

    def display_scores_by_student(self):
        print("\n--- 按学生查询成绩 ---")
        student_name = input("请输入要查询的学生姓名: ")
        scores = self._score_service.get_scores_by_student(student_name)
        if not scores:
            print(f"📋 未找到学生 '{student_name}' 的成绩记录")
            return
        print(f"学生 '{student_name}' 的成绩如下：")
        for score in scores:
            print(f"科目: {score.subject} | 分数: {score.score_value}")

    def modify_score(self):
        print("\n--- 修改成绩 ---")
        try:
            score_id = int(input("请输入要修改的成绩ID: "))
            new_score = float(input("请输入新的分数(0-100): "))
            if self._score_service.update_score(score_id, new_score):
                print("✅ 成绩修改成功！")
            else:
                print("❌ 未找到对应ID的成绩记录")
        except ValueError as e:
            print(f"❌ 修改失败: {e}")

    def remove_score(self):
        print("\n--- 删除成绩 ---")
        try:
            score_id = int(input("请输入要删除的成绩ID: "))
            if self._score_service.delete_score(score_id):
                print("✅ 成绩删除成功！")
            else:
                print("❌ 未找到对应ID的成绩记录")
        except ValueError:
            print("❌ 请输入有效的数字ID")