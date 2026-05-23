from typing import List, Optional
from entity.user import User

class UserDAO:
    """用户数据访问层"""
    def __init__(self):
        self._user_list: List[User] = []

    def add_user(self, user: User) -> bool:
        self._user_list.append(user)
        return True

    def get_user_by_username(self, username: str) -> Optional[User]:
        for user in self._user_list:
            if user.username == username:
                return user
        return None