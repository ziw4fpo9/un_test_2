
# Число елементів для сортування
while True:
    n_str = input("Введіть кількість розділів (1–20): ")
    try:
        # Перевіряємо, чи є число цілим
        if "." in n_str or "," in n_str:
            raise ValueError("дробове") # Виклик помилки

        n = int(n_str)
        if n <= 0 or n > 20:
            print("Помилка: кількість повинна бути від 1 до 20.")
            continue # ще один повтор
        break # вихід з циклу якщо число не дробове та в діапазоні від 1 до 20
    except ValueError as e: # обробка помилки
        if str(e) == "дробове":
            print("Помилка: введено дробове число. Введіть ціле число.")
        else:
            print("Помилка: введіть ціле число.")



# Вибір методу сортування
print("\nОберіть метод сортування:")
print("1 — за зростанням (A → Z)")
print("2 — за спаданням (Z → A)")
print("3 — за довжиною назви")

while True:
    method = input("Ваш вибір (1/2/3/4): ")
    if method in ("1", "2", "3", "4"):
        break
    else:
        print("Помилка: введіть 1, 2, 3 або 4.")


# Введення назв розділів
sections = []
for i in range(n):
    title = input(f"Введіть назву розділу №{i+1}: ").strip()
    if not title:
        print("Помилка: назва не може бути порожньою.")
        title = input(f"Повторіть введення назви розділу №{i+1}: ").strip()
    sections.append(title)


# --- Прибирання дублікатів ---
sections = list(set(sections))

# Сортування
if method == "1":
    print("Сортування з меньшого до більшого")
    sections.sort()
elif method == "2":
    print("Сортування з більшого до меньшого")
    sections.sort(reverse=True)
elif method == "3":
    print("Сортування за len")
    print("Сортування з меньшого до більшого")
    sections.sort(key=len)
elif method == "4":
    print("Сортування за len")
    print("Сортування з більшого до меньшого")
    sections.sort(key=len,reverse=True)

# Вивід результату
print("\nВідсортовані назви розділів:")
for title in sections:
    print("-", title)
