"""
Module that would serve as mock db, and provide methods to modify data stored in this db
"""

"""
This dict would act as key value pair for books. Each entry would have isbn as its key and value as the book object. 
When a new book is created, a new key-value pair would be added.
"""
book_db = {
    'ISBN741': {
        'isbn': 'ISBN741',
        'title': 'Mysterious Affair at Styles',
        'author': 'Agatha Christie',
        'genre': 'FICTION_THRILLER',
        'pub_year': 1960
    },
    'ISBN852': {
        'isbn': 'ISBN852',
        'title': 'The Monk Who Sold His Ferrari',
        'author': 'Robin Sharma',
        'genre': 'PHILOSOPHY',
        'pub_year': 1997
    },
    'ISBN963': {
        'isbn': 'ISBN963',
        'title': 'Half Girlfriend',
        'author': 'Chetan Bhagat',
        'genre': 'FICTION_ROMANTIC',
        'pub_year': 2005
    },
    'ISBN123': {
        'isbn': 'ISBN123',
        'title': 'Tripwire',
        'author': 'Lee Child',
        'genre': 'FICTION_ADVENTURE',
        'pub_year': 1987
    },
    'ISBN456': {
        'isbn': 'ISBN456',
        'title': 'Egyptian Civilization',
        'author': 'Mike Henry',
        'genre': 'HISTORY',
        'pub_year': 1960
    }
}
