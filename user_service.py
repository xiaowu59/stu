from dao.user_dao import UserDAO
from entity.user import User

class UserService:
    """用户业务逻辑层"""
    def __init__(self):
        self._user_dao = UserDAO()

    def register(self, username: str, password: str, role: str) -> bool:
        """用户注册"""
        # 校验用户名是否已存在
        if self._user_dao.get_user_by_username(username):
            raise ValueError("用户名已存在")
        # 校验密码长度
        if len(password) < 6:
            raise ValueError("密码长度不能少于6位")
        # 生成用户ID
        user_id = len(self._user_dao._user_list) + 1
        new_user = User(user_id, username, password, role)
        return self._user_dao.add_user(new_user)

    def login(self, username: str, password: str) -> Optional[User]:
        """用户登录"""
        user = self._user_dao.get_user_by_username(username)
        if not user:
            raise ValueError("用户不存在")
        if user.password != password:
            raise ValueError("密码错误")
        return user