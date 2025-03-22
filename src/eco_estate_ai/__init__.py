from .assistant import EcoEstateAssistant
from .embedder import Embedder
from .storage import QAStorage
from .detector import LanguageDetector
from ..utils.const import Const

QA_PAIRS_PATH = "src/data/qa_pairs.json"
MODEL_PATH = "src/eco_estate_ai/models/local_model"

def create_assistant(
    qa_path: str = Const.QA_PAIRS_PATH,
    model_path: str = Const.MODEL_PATH
) -> EcoEstateAssistant:
    _storage = QAStorage(qa_path)
    _embedder = Embedder(model_path)
    _detector = LanguageDetector()
    return EcoEstateAssistant(_storage, _embedder, _detector)
