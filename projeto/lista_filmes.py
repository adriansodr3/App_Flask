import requests


def resultado_filmes(tipo):
    if tipo == 'Populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=27c622fdf010fde8e313705fbbd42679"
    elif tipo == 'Animacao':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=27c622fdf010fde8e313705fbbd42679"
    elif tipo == "2010":
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=27c622fdf010fde8e313705fbbd42679"

    response = requests.get(url)
    dados_json = response.json()
    return dados_json['results']