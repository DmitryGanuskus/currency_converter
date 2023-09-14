from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from fake_useragent import UserAgent
import freecurrencyapi


@api_view(['GET'])
def converter(request):
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    value = float(request.GET.get('value', 0))

    api_key = 'd49918e6b1a4840a72e881805d212693d8d208fa'
    url = f'https://api.getgeoapi.com/v2/currency/convert?api_key={api_key}&from={from_currency}&to={to_currency}&amount={value}&format=json'

    response = requests.get(url, headers=fake_ua)
    data = response.json()

    return Response({'Курс рубля составляет': data['rates']['RUB']['rate']})
