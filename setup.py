# from setuptools import find_packages, setup
#
# setup(
#     name="eco_estate_ai_assistant",
#     version="0.1.0",
#     packages=find_packages(),
#     install_requires=["sentence-transformers", "langdetect", "torch"],
#     description="Multilingual AI assistant for Eco Estate Telegram bots",
#     author="Oleksandr Brusyltsev",
#     url="https://github.com/OleksandrBrusyltsev/eco-estate-ai-assistant",
#     license="MIT",
# )
#
from src.eco_estate_ai import create_assistant

# from eco_estate_ai import EcoEstateAssistant, QAStorage, Embedder, LanguageDetector
#
# storage = QAStorage("data/qa_pairs.json")
# embedder = Embedder("models/multilingual_model")
# detector = LanguageDetector()
# assistant = EcoEstateAssistant(storage, embedder, detector)
#
# print(assistant.get_answer("где находится усадьба"))
assistant = create_assistant()
print(assistant.get_answer("как добраться до усдаьбы"))
