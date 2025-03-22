import time

from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self, model_path: str = "models/local_model"):
        self.model = SentenceTransformer(model_path)

    def encode(self, texts: list[str]):
        return self.model.encode(texts, convert_to_tensor=True)
