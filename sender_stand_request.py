import data
import configuration
import requests


# Запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body,  # тут передаем тело
                         headers=data.headers)  # передаем заголовки


# Запрос на получение данных о заказе по трекеру
def get_info_by_track(track_order):
    # Подставляем полный url с трекером
    return requests.get(configuration.URL_SERVICE + configuration.GET_INFO_BY_TRACK_PATH + "?t=" + track_order)