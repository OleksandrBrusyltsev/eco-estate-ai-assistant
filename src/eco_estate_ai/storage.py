import json


class QAStorage:
    def __init__(self, filepath: str):
        with open(filepath, "r", encoding="utf-8") as f:
            self.qa_pairs = json.load(f)

    def get_questions_and_answers(self, lang: str):
        questions = [q[f"question_{lang}"] for q in self.qa_pairs]
        answers = [q[f"answer_{lang}"] for q in self.qa_pairs]
        return questions, answers
