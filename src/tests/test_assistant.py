from src.eco_estate_ai import QAStorage, Embedder, LanguageDetector, EcoEstateAssistant
from src.utils.const import Const


def test_answer():
    storage = QAStorage("src/data/qa_pairs.json")
    embedder = Embedder(Const.MODEL_PATH)
    detector = LanguageDetector()
    assistant = EcoEstateAssistant(storage, embedder, detector)

    assert "Олешня" in assistant.get_answer("где находится усадьба")
