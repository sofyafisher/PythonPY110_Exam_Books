from conf import MODEL
from fields import other_fields

def book_gen():
    other_fields()
    d = {'model': MODEL,
         'pk': "amount_of_books",
         "fields": other_fields()}
    return d


