# api_final
api final


### Описание проекта:
Тренировочный проект на django framework для разработки REST API.
Проект представляет собой простую социальную сеть (без интерфейса) включающую следующие возможности:

 - Работа с постами 
 - Работа с группами (сообщества) 
 - Работа с   комментариями к постам 
 - Подписка на авторов

Документация к API проекта доступна по адресу /redoc/

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/UberVasya/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры:
#### Получение публикаций. 
Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией. Параметры:

 - limit - Количество публикаций на страницу
 - offset - Номер страницы после которой начинать выдачу

Запрос GET
     
    http://domen/api/v1/posts/?limit=5&offset=0


Ответ
```
{

	"count": 2,

	"next": null,

	"previous": null,

	"results": [

		{

			"id": 1,

			"author": "agrit",

			"text": "Текст тестового поста, частичное изменение",

			"pub_date": "2022-06-07T06:07:54.967119Z",

			"image": null,

			"group": null

	},

	{

		"id": 2,

		"author": "vasya",

		"text": "Текст поста Васи",

		"pub_date": "2022-06-07T06:07:54.967119Z",

		"image": null,

		"group": null

	}

	]

}
```