import os
import requests

BAD = 'Bad'

GOOD = 'Good'


def get_weather(city: str) -> str:
    """
    :param city:
    :return: Weather conditions

    Reference: https://openweathermap.org/current
    """

    url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appId}&units=metric".format(
        city=city,
        appId=os.getenv('APP_ID')
    )
    response = requests.get(url)

    if response.status_code != 200:
        msg = 'openweathermap.org returned non-200 code. Actual code is: {code}, message is: {message}'.format(
            code=str(response.status_code),
            message=response.json()['message']
        )
        raise RuntimeError(msg)

    temp = response.json()['main']['temp']

    if temp > 18:
        return GOOD
    else:
        return BAD
