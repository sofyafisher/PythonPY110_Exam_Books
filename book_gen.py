import json

from fields import other_fields
from conf import MODEL

OUTPUT_FILE = "output.json"


def book_gen(amount) -> dict:
    d = {}
    for i in range(1, amount + 1):
        book_dict = {'model': MODEL,
                     'pk': i,
                     "fields": other_fields()}
        d[i] = book_dict
    return d


def to_json_file(g) -> json:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(g, f, indent=4, ensure_ascii=False)
