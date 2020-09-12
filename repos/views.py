import requests
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from datetime import date as dt, timedelta, datetime
from requests.exceptions import ConnectionError


def index(request):
    """
    function to get all data for frontend task and render data to template
    """
    url = "https://api.github.com/search/repositories?q=created:>2017-10-22&sort=stars&order=desc?page="
    try:
        data = requests.get(url).json()
    except ConnectionError as e:
        print(e)
        data = "No response"
    return render(request, 'repos/index.html', {"data": data})


def info(request):
    """
    That is the main function to fetch the 100 trending
    public repos.. i call this function in all next functions
    to get data
    """
    date = (dt.today() - timedelta(days=30)).isoformat()
    url = f"https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc&page=1&per_page=100"
    try:
        data = requests.get(url).json()
    except ConnectionError as e:
        print(e)
        data = "No response"
    return data


def p_languages(request):
    """
    This function for endpoint 'http://127.0.0.1:8000/repos/languages'
    to return all languages used in 100 trending repos.
    """
    data = info(request)
    languages = []
    for item in data['items']:
        if item['language'] is not None and item['language'] not in languages:
            languages.append(item['language'])

    return JsonResponse(languages, safe=False)


def info_languages(request, language):
    """
    function return number of repos used by each language and
    names of these repos using endpoint 'http://127.0.0.1:8000/repos/languages/<language>'
    by replacing <language> with any language i want to know about it.
    """
    data = info(request)
    repos_names = []
    repos_num = sum(item['language'] == language for item in data['items'])
    for item in data['items']:
        if item['language'] == language:
            repos_names.append(item['full_name'])

    print(repos_names)
    return JsonResponse({"language": language, "Number of Repos": repos_num, "repos": repos_names}, safe=False)
