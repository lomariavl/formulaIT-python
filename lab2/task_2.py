salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен

money = spend - salary

for i in range(months - 1):
    spend *= increase
    money += spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money:.2f}")
