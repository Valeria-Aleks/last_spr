﻿# Тест на проверку получения данных о заказе по трек-номеру
****
**Задание:**
Из требований:
Должен присутствовать URL для получения данных о заказе по его номеру отслеживания. На вход должен подаваться трек-номер заказа. 
Если соответствующий заказ найден, должны вернуться данные о нём. Иначе должна вернуться ошибка.

Автоматизация сценария:
- Клиент создает заказ.
- Проверяется, что по треку заказа можно получить данные о заказе.
  

**Перечень файлов проекта:**

configuration.py - Необходимые url-адреса 

data.py - Заголовки, данные для создания нового заказа

sender_stand_request.py - Запросы, необходимые для проведения автоматического тестирования (создание заказа, запрос на получение данных) 

get_info_test.py - Тестирование ручки на получение данных о заказе по трекеру. 



**Дополнительная информация:**
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest и указанием названия файла с тестами - get_info_test.py
