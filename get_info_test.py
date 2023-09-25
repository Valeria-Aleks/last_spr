import sender_stand_request
import data


def test_get_info_by_track():
    # Записываем результат создания заказа с данными из файла data
    response = sender_stand_request.post_new_order(data.order_body)
    # Присваиваем переменной трек-номер заказа, преобразуя в формат строки
    track_order = str(response.json()['track'])
    # Вызываем функцию получения данных по треку
    result = sender_stand_request.get_info_by_track(track_order)
    # Проверяем, что код ответа равен 200
    assert result.status_code == 200