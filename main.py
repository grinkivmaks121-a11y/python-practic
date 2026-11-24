# Практична робота: облік успішності групи

results = []  # загальний список кортежів (name, avg_score)

print("=== Облік успішності групи ===")
print('Щоб завершити введення, напишіть "кінець" замість імені.\n')

# Зчитуємо дані у циклі while до введення "кінець"
while True:
    name = input("Ім'я студента: ").strip()

    if name.lower() == "кінець":
        break
    if name == "":
        print("Ім'я не може бути порожнім. Спробуйте ще раз.\n")
        continue

    marks_str = input("Три оцінки через пробіл (наприклад, 85 90 78): ")

    # Перетворюємо рядок з оцінками у список чисел
    try:
        marks = [float(m) for m in marks_str.split()]
    except ValueError:
        print("Помилка: оцінки мають бути числами. Спробуйте ще раз.\n")
        continue

    if len(marks) != 3:
        print("Помилка: потрібно рівно 3 оцінки. Спробуйте ще раз.\n")
        continue

    if any(m < 0 or m > 100 for m in marks):
        print("Помилка: оцінки мають бути від 0 до 100. Спробуйте ще раз.\n")
        continue

    avg_score = sum(marks) / len(marks)
    results.append((name, avg_score))
    print(f"Додано: {name}, середній бал {avg_score:.2f}\n")

# Підсумковий звіт
print("\n=========== ПІДСУМКОВИЙ ЗВІТ ===========")

if len(results) == 0:
    print("Дані не введено.")
else:
    for name, avg_score in results:
        if avg_score >= 90:
            status = "Відмінник"
        elif avg_score >= 60:
            status = "Успішний"
        else:
            status = "Потребує уваги"

        print(f"{name:<20} {avg_score:>6.2f}   {status}")

    group_avg = sum(avg for _, avg in results) / len(results)
    print("----------------------------------------")
    print(f"Студентів: {len(results)}")
    print(f"Середній бал групи: {group_avg:.2f}")
