from typing import TypedDict


class Movie(TypedDict):
    name: str
    year: int
    image_url: str


movie: Movie = {
    'name': 'Blade Runner',
    'year': 1982,
    'image_url': 'asd'
}

movie2: Movie = {
    'name': 'Blade Runner',
    'year': 2020,
    'image_url': "asdf"
}

movie2['year'] = 2021

print(movie['name'])
