from models.idGenerator import generateId


class Movie:
    """
    Movie class to define Movie Objects
    """
    def __init__(
        self,
        imageLink,
        title: str,
        year: int,
        idiom: list,
        director: list,
        gender: str,
        principalsActors: list
    ):
        self.id = generateId()
        self.imageLink = imageLink
        self.title = title
        self.year = year
        self.idiom = idiom
        self.director = director
        self.gender = gender
        self.principalsActors = principalsActors


