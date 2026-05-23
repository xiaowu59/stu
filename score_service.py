from dao.score_dao import ScoreDAO
from entity.score import Score

class ScoreService:
    def __init__(self):
        self._score_dao = ScoreDAO()

    def add_score(self, student_name: str, subject: str, score_value: float) -> bool:
        if not (0 <= score_value <= 100):
            raise ValueError("分数必须在 0-100 之间")
        if not student_name.strip() or not subject.strip():
            raise ValueError("学生姓名和科目不能为空")
        
        score_id = len(self._score_dao.get_all_scores()) + 1
        new_score = Score(score_id, student_name.strip(), subject.strip(), score_value)
        return self._score_dao.add_score(new_score)

    def get_all_scores(self):
        return self._score_dao.get_all_scores()

    def get_scores_by_student(self, student_name: str):
        return self._score_dao.get_scores_by_student(student_name.strip())

    def update_score(self, score_id: int, new_score_value: float) -> bool:
        if not (0 <= new_score_value <= 100):
            raise ValueError("分数必须在 0-100 之间")
        return self._score_dao.update_score(score_id, new_score_value)

    def delete_score(self, score_id: int) -> bool:
        return self._score_dao.delete_score(score_id)