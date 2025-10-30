
# Число елементів для сортування
while True:
    n_str = input("Введіть кількість розділів (1–20): ")
    try:
        # Перевіряємо, чи є число цілим
        if "." in n_str or "," in n_str:
            raise ValueError("дробове")

        n = int(n_str)
        if n <= 0 or n > 20:
            print("Помилка: кількість повинна бути від 1 до 20.")
            continue
        break
    except ValueError as e:
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
    method = input("Ваш вибір (1/2/3): ")
    if method in ("1", "2", "3"):
        break
    else:
        print("Помилка: введіть 1, 2 або 3.")


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
    sections.sort()
elif method == "2":
    sections.sort(reverse=True)
elif method == "3":
    sections.sort(key=len)

# Вивід результату
print("\nВідсортовані назви розділів:")
for title in sections:
    print("-", title)
