from movie_model import MovieModel
import requests


def callMovieApi(page=1):
    url = f'''
        https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number={page}&limit=20
    '''

    response = requests.get(url)
    
    responseDict = response.json()                  # 딕셔너리 타입으로 변환
    movies = responseDict["data"]["movies"] # list 타입
    
    return convert_model(movies)


def convert_model(movies):
    list = []

    for movie in movies:
        movie_model = MovieModel(movie["title"], movie["rating"], movie["small_cover_image"], movie["summary"])
        list.append(movie_model)
            
    print(list)
    return list


