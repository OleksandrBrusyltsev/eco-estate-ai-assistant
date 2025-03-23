from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self, model_path: str = "paraphrase-multilingual-MiniLM-L12-v2"):
        self.model = SentenceTransformer(model_path)

    def encode(self, texts: list[str]):
        return self.model.encode(texts, convert_to_tensor=True)
