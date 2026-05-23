class User:
    """用户实体类"""
    def __init__(self, user_id: int, username: str, password: str, role: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role  # student/teacher/admin

    def __str__(self):
        return f"用户ID:{self.user_id} 用户名:{self.username} 角色:{self.role}"