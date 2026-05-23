from controller.score_controller import ScoreController
from controller.user_controller import UserController

def show_menu():
    print("\n===== 🎓 学生成绩管理系统 =====")
    print("1. 用户注册")
    print("2. 用户登录")
    print("3. 录入成绩")
    print("4. 查看所有成绩")
    print("5. 按学生查询成绩")
    print("6. 修改成绩")
    print("7. 删除成绩")
    print("8. 退出系统")
    print("=============================")

def main():
    user_controller = UserController()
    score_controller = ScoreController()
    is_logged_in = False

    while True:
        show_menu()
        choice = input("请输入您的选择(1-8): ")
        if choice == "1":
            user_controller.register()
        elif choice == "2":
            is_logged_in = user_controller.login()
        elif choice in ["3", "4", "5", "6", "7"]:
            if not is_logged_in:
                print("❌ 请先登录！")
                continue
            if choice == "3":
                score_controller.insert_score()
            elif choice == "4":
                score_controller.display_all_scores()
            elif choice == "5":
                score_controller.display_scores_by_student()
            elif choice == "6":
                score_controller.modify_score()
            elif choice == "7":
                score_controller.remove_score()
        elif choice == "8":
            print("👋 感谢使用，系统退出！")
            break
        else:
            print("❌ 无效选项，请输入 1-8 之间的数字")

if __name__ == "__main__":
    main()