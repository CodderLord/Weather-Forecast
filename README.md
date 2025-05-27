## Weather Forecast Application
#### ![Docker-ready-blue.svg](icons/Docker-ready-blue.svg)
#### ![Flask-2.0-green.svg](icons/Flask-2.0-green.svg)
#### ![Python-3.9+-blue.svg](icons/Python-3.9%2B-blue.svg)

### Проект предоставляет API и веб-интерфейс для получения прогноза погоды в городах России с использованием данных от Open-Meteo и DaData.

- #### Реализовано 
  - #### Docker контейнер
  - #### Автодополнение (подсказки) при вводе города
  - #### Предложено смотреть последний введённый этим пользователем город для повторного просмотра
  - #### История поиска для каждого поиска
  - #### История количества ввода городов
  - #### Внешний API, и минимальная документация к нему, для просмотра сколько раз вводили какой город 


- #### Основные возможности 
    - #### _Поиск погоды по городам России_
    - #### _Автодополнение при вводе названия города_
    - #### _Подробный прогноз на текущий день и неделю_
    - #### _История поиска для пользователей_
    - #### _Статистика популярности городов_

- #### Технологии
  - #### Backend: Python, Flask
  - #### Frontend: HTML, CSS, JS
  - #### API: Open-Meteo, DaData
  - #### Инфраструктура: Docker


- #### Структура проекта
```commandline
    weather-app/
    ├── API_documentation/
    │   ├── API_DOC.md
    │   └── get_city_history.py
    ├── APP/
    │   ├── templates
    │   │   └── index.html
    │   ├── app.py
    │   └── roures.py
    ├── Cashe/
    │   └── cashe.py
    ├── City/
    │   └── city.py
    ├── Config/
    │   ├── config.py   
    │   └── log_config.py
    ├── icons/
    ├── UserManager/
    │   └── user_data.py
    ├── Weather/
    │   └── weather.py
    ├── logs/
    │   └── weathers.py
    ├── DB/
    │   ├── user_history.json
    │   └── city_stats.json
    ├── Dockerfile           
    ├── requirements.txt     
    └── README.md            
```

## Лицензия
Проект создавался как тестовый. Проект распространяется под лицензией MIT.


#### Email:
```
verevkin0909@gmail.com
```
#### Telegram: 
```
@kail_inv
```

