from src.eco_estate_ai import EcoEstateAssistant, Embedder, LanguageDetector, QAStorage
from eco_estate_ai.const import Const


def create_assistant(
    qa_path: str = Const.QA_PAIRS_PATH,
    model_path: str = Const.MODEL_PATH
) -> EcoEstateAssistant:
    _storage = QAStorage(qa_path)
    _embedder = Embedder(model_path)
    _detector = LanguageDetector()
    return EcoEstateAssistant(_storage, _embedder, _detector)
