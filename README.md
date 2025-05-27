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

    - ### Установка
    - Через ```git clone```/ ```docker```
      - Установка через ```git clone```
        - Установить python 3.10+
        - Клонировать проект в репозиторий 
        ```bash
          git clone https://github.com/CodderLord/Weather-Forecast.git
        ```
        - Создаём виртуальную среду
            ```bash
            python -m venv .venv
            ```
          - Активируем виртуальную среду:
            - windows
              ```bash
              .venv\Scripts\activate
              ```
            - linux/MacOS
              ```bash
              source .venv/bin/activate
              ```
        - Установить зависимости 
        ```bash
          pip install -r requirements.txt
        ```
        - Запуск через ```python main.py```
        - Установка через Dockerfile 
          - Скачать [Docker](https://www.docker.com/products/docker-desktop/)
          - [Скачать Dockerfile](https://raw.githubusercontent.com/CodderLord/Weather-Forecast/refs/heads/master/Dockerfile)
          - ```bash
            docker build -t weather .
          - ```bash
            docker run --rm -p 8080:8080 weather
            


- #### Структура проекта
```
    weather-app/
    ├── API_documentation/
    │   ├── API_DOC.md
    │   └── get_city_history.py
    ├── APP/
    │   ├── templates
    │   │   └── index.html
    │   ├── app.py
    │   └── roures.py
    ├── Cache/
    │   └── cache.py
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


