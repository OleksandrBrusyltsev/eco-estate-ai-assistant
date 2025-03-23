from src import Const

from .assistant import EcoEstateAssistant
from .detector import LanguageDetector
from .embedder import Embedder
from .storage import QAStorage


def create_assistant(
    qa_path: str = Const.QA_PAIRS_PATH, model_path: str = Const.MODEL_PATH
) -> EcoEstateAssistant:
    _storage = QAStorage(qa_path)
    _embedder = Embedder(model_path)
    _detector = LanguageDetector()
    return EcoEstateAssistant(_storage, _embedder, _detector)
