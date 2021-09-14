from requests.models import Response
from movie_model import MovieModel
from temp_model import TempModel
import requests
from requests.api import request
from bs4 import BeautifulSoup

def callTempApi():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%98%84%EC%9E%AC%EC%98%A8%EB%8F%84'
    req = requests.get(url)
    
    soup = BeautifulSoup(req.content, 'html.parser')

    temp = soup.select('span.todaytemp')[0].text

    return temp


    

def callMovieApi(page=1):
    url = f'''
        https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number={page}&limit=20
    '''

    response = requests.get(url)
    
    responseDict = response.json()
    movies = responseDict["data"]["movies"]
    
    return convert_model(movies)


def convert_model(movies):
    list = []

    for movie in movies:
        movie_model = MovieModel(movie["title"], movie["rating"], movie["small_cover_image"], movie["summary"])
        list.append(movie_model)
        
    print(list)
    return list