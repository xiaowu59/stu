from controller.score_controller import ScoreController
from controller.user_controller import UserController

def show_menu():
    print("\n===== 🎓 学生成绩管理系统 =====")
    print("1. 用户注册")
    print("2. 用户登录")
    print("3. 录入成绩")
    print("4. 查看所有成绩")
    print("5. 退出系统")
    print("=============================")

def main():
    user_controller = UserController()
    score_controller = ScoreController()
    is_logged_in = False

    while True:
        show_menu()
        choice = input("请输入您的选择(1-5): ")
        if choice == "1":
            user_controller.register()
        elif choice == "2":
            is_logged_in = user_controller.login()
        elif choice == "3":
            if not is_logged_in:
                print("❌ 请先登录！")
                continue
            score_controller.insert_score()
        elif choice == "4":
            if not is_logged_in:
                print("❌ 请先登录！")
                continue
            score_controller.display_all_scores()
        elif choice == "5":
            print("👋 感谢使用，系统退出！")
            break
        else:
            print("❌ 无效选项，请输入 1-5 之间的数字")

if __name__ == "__main__":
    main()