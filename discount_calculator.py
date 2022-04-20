import datetime


def discount_calculator(value: float, due_date: datetime.date, discount: float, days: int) -> float:
    diff = due_date - datetime.date.today()
    if datetime.timedelta() <= diff < datetime.timedelta(days=days):
        return value * (1.0 - discount)
    else:
        return value
