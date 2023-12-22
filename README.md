# Flasker

### Автор
1. https://github.com/CapitainFan - backend + frontend;

### Технологии
Jinja2 ;  
HTML ;  
CSS ;  
Python 3.7  - https://docs.python.org/release/3.7.0/;  
Flask - 1.1.2 - https://flask.palletsprojects.com/en/1.1.x/  
Bootstrap - https://getbootstrap.com/docs/5.3/getting-started/introduction/  

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
- В папке с кодом выполните команду:
```
python -m venv virt
source virt/bin/activate

pip install -r requirements.txt

export FLASK_ENV=development
export FLASK_APP=app.py
flask run
```