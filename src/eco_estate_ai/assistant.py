from sentence_transformers import util

from ..utils.const import Const
from .detector import LanguageDetector
from .embedder import Embedder
from .storage import QAStorage
import torch


class EcoEstateAssistant:
    def __init__(
        self,
        storage: QAStorage,
        embedder: Embedder,
        detector: LanguageDetector,
        threshold: float = 0.2,
    ):
        self.storage = storage
        self.embedder = embedder
        self.detector = detector
        self.threshold = threshold
        self.embeddings_cache = self._prepare_embeddings()

    def _prepare_embeddings(self):
        cache = {}
        for lang in [Const.RU, Const.UK]:
            questions, answers = self.storage.get_questions_and_answers(lang)
            embeddings = self.embedder.encode(questions)
            cache[lang] = {
                "questions": questions,
                "answers": answers,
                "embeddings": embeddings,
            }
        return cache

    def get_answer(self, user_question: str) -> str:
        lang = self.detector.detect_language(user_question)

        cached = self.embeddings_cache[lang]

        query_embedding = self.embedder.encode([user_question])[0]

        cosine_scores = util.cos_sim(query_embedding, cached["embeddings"])[0]
        best_match_idx = int(torch.argmax(cosine_scores))
        best_score = float(cosine_scores[best_match_idx])

        if best_score >= self.threshold:
            return cached["answers"][best_match_idx]

        return Const.DEFAULT_ANSWER_UK if lang == Const.UK else Const.DEFAULT_ANSWER_RU
