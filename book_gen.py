import json
from conf import MODEL
from fields import other_fields
OUTPUT_FILE = "output.json"

def book_gen():
    other_fields()
    book_dict = {'model': MODEL,
         'pk':"",
         "fields": other_fields()}
    return d

def to_json_file(book_gen):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(book_gen(), f, indent=4, ensure_ascii=False)


