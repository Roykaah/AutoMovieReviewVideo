import requests
from urllib.parse import urlencode
from urllib.parse import quote
import json
import csv


def coletando_dados_do_ultimo_filme(api_key, session_id, headers):
    account_id = "account_id"
    url_base = f"https://api.themoviedb.org/3/account/{account_id}/rated/movies?api_key="
    page = '1'
    url_link = f"{url_base}{api_key}&session_id={session_id}&sort_by=created_at.desc&page={page}"
    DadosDaPagina = requests.get(url_link, headers=headers).json()
    response_dict = {
        'title': DadosDaPagina['results'][0]['original_title'],
        'year': DadosDaPagina['results'][0]['release_date'][:4],
        'my_rating': DadosDaPagina['results'][0]['rating'],
        "director": '',
    }
    return response_dict


def validando_com_login(str_before_api_key, Usuario, headers):
    request_token = generate_Request_Token(str_before_api_key,
                                           Usuario['api_key'], headers)
    url_base = "https://api.themoviedb.org/3/authentication/token/validate_with_login?"
    url_link = f"{url_base}{str_before_api_key}{Usuario['api_key']}&request_token={request_token}&username={Usuario['login']}&password={Usuario['senha']}"
    #Uso o token para logar.
    requests.post(url_link, headers=headers).json()
    url_link = f"https://api.themoviedb.org/3/authentication/session/new?api_key={Usuario['api_key']}"
    params = {
        "request_token": f"{request_token}",
        "Content-Type": "application/json;charset=utf-8"
    }
    #Uso o token já logado para criar id da sessao
    session_id_json = requests.post(url_link, headers=headers,
                                    params=params).json()
    return session_id_json["session_id"]


def generate_Request_Token(str_before_api_key, api_key, headers):
    url_base = "https://api.themoviedb.org/3/authentication/token/new"
    url_link = f"{url_base}{str_before_api_key}{api_key}"
    resposta = requests.get(url_link, headers=headers)
    resposta_em_dict = resposta.json()
    return resposta_em_dict['request_token']


def dados_do_ultimo_filme_assistido():

    Usuario = {
        'login':
        "Royka",
        'senha':
        "ProjetoPython555",
        'api_key':
        "9f0b4f14fa986dec0ae942392adc2de4",
        'access_token':
        "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZjBiNGYxNGZhOTg2ZGVjMGFlOTQyMzkyYWRjMmRlNCIsInN1YiI6IjVmYWQyOWU0ZGUxMWU1MDA0MTE2YjA5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.a9yTBggzSveyZp6hgbV_ZMFcJaEgu39SoOd7femE4yg"
    }
    headers = {
        "Authorization": f"Bearer {Usuario['access_token']}",
        "Content-Type": "application/json;charset=utf-8"
    }
    str_before_api_key = "?api_key="
    session_id = validando_com_login(
        str_before_api_key,
        Usuario,
        headers,
    )
    DadosUltimoFilme = coletando_dados_do_ultimo_filme(
        Usuario['api_key'],
        session_id,
        headers,
    )
    return DadosUltimoFilme