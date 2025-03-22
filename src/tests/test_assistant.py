from eco_estate_ai import (EcoEstateAssistant, Embedder, LanguageDetector,
                           QAStorage)


def test_answer():
    storage = QAStorage("data/qa_pairs.json")
    embedder = Embedder("models/multilingual_model")
    detector = LanguageDetector()
    assistant = EcoEstateAssistant(storage, embedder, detector)

    assert "Олешня" in assistant.get_answer("где находится усадьба").lower()
