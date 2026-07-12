# Django Store

Домашняя работа по созданию Django-проекта интернет-магазина.

## Что реализовано

- Создан Django-проект.
- Создано приложение `catalog`.
- Приложение `catalog` зарегистрировано в `INSTALLED_APPS`.
- Создан файл маршрутов `catalog/urls.py`.
- URL-файл приложения подключен в основном `config/urls.py` через `include`.
- Создан HTML-шаблон главной страницы.
- Создан HTML-шаблон страницы контактов.
- Для стилизации используется Bootstrap.
- Контроллер главной страницы рендерит шаблон через `render`.
- Контроллер страницы контактов рендерит шаблон через `render`.
- Главная страница доступна по адресу `/`.
- Страница контактов доступна по адресу `/contacts/`.
- Все URL-адреса заканчиваются на `/`.
- Реализована форма обратной связи на странице контактов.
- При отправке формы данные выводятся в консоль.
- После отправки формы отображается сообщение об успешной отправке.

## Структура проекта

```text
django_store/
├── catalog/
│   ├── templates/
│   │   └── catalog/
│   │       ├── contacts.html
│   │       └── home.html
│   ├── urls.py
│   └── views.py
├── config/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── README.md
├── .gitignore
├── pyproject.toml
└── poetry.lock

## Домашняя работа: PostgreSQL, модели, фикстуры

В проект добавлена работа с базой данных PostgreSQL.

### Реализовано

- Настройки базы данных вынесены в `.env`.
- Добавлен шаблон переменных окружения `.env.sample`.
- Подключена PostgreSQL через настройки `DATABASES`.
- Добавлены зависимости:
  - `psycopg2-binary`;
  - `python-dotenv`;
  - `Pillow`;
  - `ipython`.
- Создана модель `Category`.
- Создана модель `Product`.
- Модель `Product` связана с моделью `Category` через `ForeignKey`.
- Для моделей добавлены `verbose_name` и `verbose_name_plural`.
- Для моделей реализованы методы `__str__`.
- Созданы и применены миграции.
- Настроены `MEDIA_URL` и `MEDIA_ROOT`.
- Настроено отображение медиафайлов в режиме `DEBUG`.
- Модели зарегистрированы в админке.
- Для `Category` в админке отображаются `id` и `name`.
- Для `Product` в админке отображаются `id`, `name`, `price`, `category`.
- Для `Product` добавлены фильтр по категории и поиск по `name`, `description`.
- Созданы фикстуры:
  - `catalog/fixtures/categories.json`;
  - `catalog/fixtures/products.json`.
- Создана кастомная команда:

```bash
poetry run python manage.py load_catalog_data
