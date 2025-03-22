# 🏡 Eco-Estate AI Assistant — GrandpaBot

A lightweight, multilingual AI-powered assistant built specifically for the eco-lodge *"На селі у Дідуся"* — a cozy retreat near the Blue Lakes in Chernihiv region, Ukraine.

This mini-assistant is designed to help visitors and guests get instant answers to frequently asked questions via Telegram.

> ✅  The assistant is already in use and actively answering questions only for the website ecousadba.in.ua via the Telegram bot. [ecousadba.in.ua](https://ecousadba.in.ua/uk)

---

## 🔧 Features

- ✅ Understands semantically similar questions (not just keywords)
- ✅ Supports both Ukrainian 🇺🇦 and Russian 🇷🇺 languages
- ✅ Lightning-fast responses thanks to preloaded embeddings
- ✅ Easily extendable FAQ via simple JSON
- ✅ Clean modular architecture (can be used as a Python library)
- ✅ Plug-and-play integration with Telegram or any bot platform

---

## 🧠 Technologies Used

- Python 3.11+
- [sentence-transformers](https://www.sbert.net/) — multilingual semantic embeddings
- [langdetect](https://pypi.org/project/langdetect/) — language identification
- Telegram Bot API (optional)
- FastAPI-ready architecture
- (Optional) `uvicorn`, `faiss`, `pickle` — for advanced deployments

---

## 🚀 How It Works

1. User sends a message via Telegram (or any interface).
2. The assistant detects the language (`uk` or `ru`).
3. It encodes the question into a semantic vector.
4. Compares it to known Q&A embeddings using cosine similarity.
5. Returns the most relevant answer from the local knowledge base.

---

## 📦 Installation

### 🔗 From GitHub

Install directly via pip or poetry:

```bash
# pip
pip install git+https://github.com/OleksandrBrusyltsev/eco-estate-ai-assistant.git

# poetry
poetry add git+https://github.com/OleksandrBrusyltsev/eco-estate-ai-assistant.git
```

---

## 🧪 Usage Example

```python
from eco_estate_ai import create_assistant

assistant = create_assistant()
response = assistant.get_answer("чи є вайфай?")
print(response)
```

Or integrate with your Telegram bot like this:

```python
@dp.message_handler()
async def handle_message(message: types.Message):
    response = assistant.get_answer(message.text)
    await message.reply(response)
```

---



## 🛖 About the Estate

This project was created specifically for the eco-estate *Grandpa's Village*, located in the forest near the Blue Lakes  Chernihiv region, Ukraine.

The assistant helps automate guest communication by answering common questions 24/7 in Telegram. You can learn more at [ecousadba.in.ua](https://ecousadba.in.ua/uk).

---

## 🤝 Contributing

Pull requests and feedback are welcome!  
If you have ideas for improving accuracy, adding languages, or new features — feel free to open an issue or PR.

---

## 🌐 Links

- GitHub: [github.com/OleksandrBrusyltsev/eco-estate-ai-assistant](https://github.com/OleksandrBrusyltsev/eco-estate-ai-assistant)
