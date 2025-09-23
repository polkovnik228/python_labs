# python_labs

## Лабораторная работа 1

### Задание 1

```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![image 1](./images/lab01/01_greeting.png)

### Задание 2

```python
a = float(input("a: ").replace(",", "."))
b = float(input("b: ").replace(",", "."))

s = a + b
avg = s / 2

print(f"sum={s:.2f}; avg={avg:.2f}")
```
![image 2](./images/lab01/02_sum_avg.png)

### Задание 3

```python
price = float(input())
discount = float(input())
vat = float(input())

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС: {vat_amount:.2f} ₽")
print(f"Итого к оплате: {total:.2f} ₽")
```
![image 3](./images/lab01/03_discount_vat.png)

### Задание 4

```python
def minutes_to_hhmm(m):
    hours = m // 60
    remaining_minutes = m % 60
    return f"{hours}:{remaining_minutes:02d}"

m = int(input("Минуты: "))
result = minutes_to_hhmm(m)
print(f"{result}")
```
![image 4](./images/lab01/04_minutes_to_hhmm.png)
