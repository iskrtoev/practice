# Template Matcher

Сопоставление данных по заданному шаблону.
## Установка

1. Убедитесь, что у вас установлен Python.
2. Установите зависимости:
   ```bash
   pip install tinydb
## Использование
```python data_processor.py ```   
Запуск через командную строку:

```bash
python find_data.py find --field=value --field2=value2
```
Пример:

```bash
python find_data.py find --email="user@example.com" --phone="+7 123 456 78 90"
```
``` python template_matcher.py ```

Автоматически тестирует заданные примеры. Запуск:

```bash
python match.py
```
## Формат данных
Поддерживаемые типы полей:

```email``` 

```phone``` 

```date``` 

```string``` 

## Примеры шаблонов
См. templates_data.json:

json
{
    "1": {
        "title": "User profile",
        "username": "email",
        "mobile": "phone"
    }
}