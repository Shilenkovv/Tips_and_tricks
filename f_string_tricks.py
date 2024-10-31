# разделители для больших чисел
n: int = 1000000000000
print(f'{n:_}')
print(f'{n:,}')
# -------------------------
# автоматическое заполнение для str формата
var: str = 'var'
print(f'{var:_>20}')
print(f'{var:#<20}')
print(f'{var:-^20}')
# -------------------------
# специфаеры для даты и времени
from datetime import datetime
now: datetime = datetime.now()
print(f'{now:%d.%m.%y}')
print(f'{now:%d.%m.%y (%H:%M:%S)}')
print(f'{now:%c}')
print(f'{now:%I%p}')
# -------------------------
# специфаеры для даты и времени
from datetime import datetime
now: datetime = datetime.now()
date_spec: str = '%d.%m.%y'
print(f'{now:{date_spec}}')
# -------------------------
# запись в scientific нотации
big_number: int = 1620000000000000
print(f'{big_number:.3e}')
# -------------------------
# разделители + флоат
number: float = 1000000.1234567
spec: str = ',.2f'
print(f'{number:{spec}}')
# -------------------------
# r позвоняет избежать исключений за счёт / или \
path: str = r'\Users\Shilenkovv'
print(path)

# динамический путь
custom_folder: str = 'Indently'
path: str = fr'\Users\Shilenkovv\Documents\{custom_folder}'
print(path)
# -------------------------
# одновременное использование debug mode {a+b=} с форматированием
a: float = 0.1
b: float = 0.2
print(f'{a + b = :.2f}')
# -------------------------
# подавление кавычек
name: str = 'Bob'
print(f'{name = }')
print(f'{name = !s}')
# -------------------------
# переменные
from datetime import datetime, date
plt.plot()
banana: str = '🍌'
name: str = 'Bob'
today: date = datetime.now().date()

print(f'[{today!s} {name!s} says: {banana!s}]')
print(f'[{today!r} {name!r} says: {banana!r}]')
print(f'[{today!a} {name!a} says: {banana!a}]')