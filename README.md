# Kokoa Friends Golf Backend

A clone project of [Kakao Friends Golf]('https://www.kakaofriendsgolf.com')

## REQUIREMENTS
- Python 3.8
- Django
- MySQL
  
## HOW TO RUN
Setup python 3.8 environment + installed local SQL

### Setup MySQL DB
```mysql
# in mysql shell,
# CREATE MySQL DB
create database KokoaFriendsGolf character set utf8mb4 collate utf8mb4_general_ci;
```

### Setup Python Env & Run with Python
```shell
# in project root
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

