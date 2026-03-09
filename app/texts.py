import json
from db.db import db_get_language


def load_text(language: str) -> dict:
    file_path = f"locales/{language}.json"
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_text(key: str, user_id: int) -> str:
    language = db_get_language(user_id)
    texts = load_text(language)
    return texts.get(key, key)

