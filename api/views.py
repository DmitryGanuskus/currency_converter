from _pydecimal import Decimal

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from fake_useragent import UserAgent


@api_view(['GET'])
def converter(request):
    # Генерация случайного User-Agent
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}

    # Получение параметров из GET-запроса
    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    value = request.GET.get('value', 0)

    # Установка API-ключа для доступа к внешнему сервису
    api_key = 'd49918e6b1a4840a72e881805d212693d8d208fa'

    # Формирование URL-адреса для запроса к внешнему сервису конвертации валют
    url = f'https://api.getgeoapi.com/v2/currency/convert?api_key={api_key}&from={from_currency}&to={to_currency}&amount={value}&format=json'

    # Отправка GET-запроса к внешнему сервису с указанием сгенерированного User-Agent
    response = requests.get(url, headers=fake_ua)

    # Получение данных ответа в формате JSON
    data = response.json()

    # Получение конвертированной суммы из данных ответа
    result = str(
        Decimal(data['rates'][to_currency]['rate']) * Decimal(value)
    )

    # Возвращение ответа в формате JSON с указанием курса конвертации
    return Response(
        {
            f'Цена за {value} {to_currency} к {from_currency} составляет': result})
