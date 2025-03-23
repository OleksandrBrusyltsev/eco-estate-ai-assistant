from functools import lru_cache

import langdetect

from .const import Const


class LanguageDetector:
    @staticmethod
    @lru_cache(maxsize=512)
    def detect_language(text: str) -> str:
        lang = langdetect.detect(text)
        return Const.UK if lang == Const.UK else Const.RU
