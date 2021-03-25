# Russian coin detector

**Russian coin detector** - простейший веб-сервер на базе Flask. Сервер состоит из одной страницы с формой загрузки файлов картинок с русскими монетами.
После загрузки сервер обрабатывает картинку и выводит следующую информацию:

- метаданные файла картинки (ширина/высота)
- средний цвет картинки (выводить в виде RGB и прямоугольника соотвествующего цвета)
- количество монет на подложке
- общая сумма монет

## Требования

Python 3.8.5+

## Запуск

Для начала склонируйте данный репозиторий:

    $ git clone https://github.com/opodryadov/coin_detector
	
Откройте проект в PyCharm

Установите все зависимости

	pip install -r requirements

Запустите проект

Сервер будет доступен по следующему адресу:

	http://127.0.0.1:5000/