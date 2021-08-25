import datetime as dt


def year(request):
    """Добавляет в контекст переменную year с годом."""
    date = dt.datetime.today().year
    return {'year': date, }
