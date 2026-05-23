from service.user_service import UserService

class UserController:
    """用户控制层"""
    def __init__(self):
        self._user_service = UserService()

    def register(self):
        print("\n--- 用户注册 ---")
        username = input("请输入用户名: ")
        password = input("请输入密码(不少于6位): ")
        role = input("请输入角色(student/teacher/admin): ")
        try:
            self._user_service.register(username, password, role)
            print("✅ 注册成功！")
        except ValueError as e:
            print(f"❌ 注册失败: {e}")

    def login(self):
        print("\n--- 用户登录 ---")
        username = input("请输入用户名: ")
        password = input("请输入密码: ")
        try:
            user = self._user_service.login(username, password)
            print(f"✅ 登录成功！欢迎 {user.username} ({user.role})")
            return True
        except ValueError as e:
            print(f"❌ 登录失败: {e}")
            return False