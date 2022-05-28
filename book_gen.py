import json
from conf import MODEL
from fields import other_fields
OUTPUT_FILE = "output.json"

def book_gen(am):
    d = {}
    for i in range(1, am+1):
        book_dict = {'model': MODEL,
         'pk':i,
         "fields": other_fields()}
        d[i] = book_dict
    return d

def to_json_file(g):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(g, f, indent=4, ensure_ascii=False)


