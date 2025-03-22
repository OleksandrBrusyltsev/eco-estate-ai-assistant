from src.eco_estate_ai.assistant import EcoEstateAssistant
from src.eco_estate_ai.detector import LanguageDetector
from src.eco_estate_ai.embedder import Embedder
from src.eco_estate_ai.storage import QAStorage

storage = QAStorage("src/data/qa_pairs.json")
embedder = Embedder("src/eco_estate_ai/models/local_model")
detector = LanguageDetector()
assistant = EcoEstateAssistant(storage, embedder, detector)

# @dp.message_handler()
# async def handle_message(message: types.Message):
#     response = assistant.get_answer(message.text)
#     await message.reply(response)
#
if __name__ == "__main__":
    print(assistant.get_answer("чи є баня?"))
