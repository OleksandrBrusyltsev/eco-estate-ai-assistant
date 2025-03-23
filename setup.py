from setuptools import find_packages, setup

setup(
    name="eco_estate_ai_assistant",
    version="0.1.0",
    packages=find_packages(where="eco-estate-ai-assistant/src/eco_estate_ai/"),
    install_requires=["sentence-transformers", "langdetect", "torch"],
    description="Multilingual AI assistant for Eco Estate Telegram bots",
    author="Oleksandr Brusyltsev",
    url="https://github.com/OleksandrBrusyltsev/eco-estate-ai-assistant",
    license="MIT",
)
