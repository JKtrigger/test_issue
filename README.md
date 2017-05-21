# Django 


## Тестовое задание

* База Сотрудников компании
* Django aдминка для редактирования отделов и людей.
* Страница списка людей с пагинацией и фильтрами по:
    >Отделу

    >Работает в компании

* Страница просмотра данных человека 


## Requirements
 
* Python 2.7
* Django 1.11

## Установка
   [Install + activate virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

    pip install -r requirements/base.txt
    python ./manage.py makemigrations employees
    python ./manage.py migrate
    python ./manage.py createsuperuser
    python ./manage.py runserver
    
Запустить [Admin Page](http://localhost:8000/admin/) и создать отделы

## Заполнение тестовыми данными:
    предварительно создайте отделы 
    python ./manage.py fill_data_base --count 300
 
 