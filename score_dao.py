from typing import List, Optional
from entity.score import Score

class ScoreDAO:
    def __init__(self):
        self._score_list: List[Score] = []

    def add_score(self, score: Score) -> bool:
        self._score_list.append(score)
        return True

    def get_all_scores(self) -> List[Score]:
        return self._score_list.copy()

    def get_scores_by_student(self, student_name: str) -> List[Score]:
        return [s for s in self._score_list if s.student_name == student_name]

    def update_score(self, score_id: int, new_score_value: float) -> bool:
        for score in self._score_list:
            if score.score_id == score_id:
                score.score_value = new_score_value
                return True
        return False

    def delete_score(self, score_id: int) -> bool:
        for i, score in enumerate(self._score_list):
            if score.score_id == score_id:
                del self._score_list[i]
                return True
        return False