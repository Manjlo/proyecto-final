from models.movie import Movie
from work_logic.handleJson import create_new_register


def add_new_register(name, image, año, idioma_original, director, genero, actores_principales):
    """
Function to add a new movie register
"""
    new_movie = Movie(
        image,
        name,
        año,
        idioma_original,
        director,
        genero,
        actores_principales
    )
    

