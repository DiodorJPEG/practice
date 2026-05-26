from pathlib import Path
from colorama import init, Fore, Style
init(autoreset=True)

def process_students(input_path: Path, output_path: Path):
    ages = []
    try:
        with input_path.open('r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 2:
                    print(f"{Fore.YELLOW}Строка {line_num} имеет неверный формат: {line}")
                    continue
                name = parts[0].strip()
                try:
                    age = int(parts[1].strip())
                    ages.append(age)
                except ValueError:
                    print(f"{Fore.YELLOW}Невозможно преобразовать возраст в строке {line_num}: {line}")
    except FileNotFoundError:
        print(f"{Fore.RED}Файл {input_path} не найден!")
        return
    except Exception as e:
        print(f"{Fore.RED}Ошибка при чтении файла: {e}")
        return

    if not ages:
        print(f"{Fore.RED}Ошибка в данных")
        return

    average = sum(ages) / len(ages)

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(f"Средний возраст: {average:.2f}\n", encoding='utf-8')
        print(f"{Fore.GREEN}Обработка завершена. Средний возраст: {average:.2f}. Результат сохранён в {output_path}")
    except Exception as e:
        print(f"{Fore.RED}Ошибка при записи результата: {e}")

if __name__ == "__main__":
    input_file = Path('data') / 'students.txt'
    output_file = Path('data') / 'average_age.txt'
    process_students(input_file, output_file)
input("\nНажмите Enter для выхода...")