from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    
    main_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], 
            "Thursday" : [], "Friday": []}
    
    finish_dict = {}
    # перші 7 днів нового року виведено окремо, щоб уникнути проблеми невходження їх в потрібний період
    promlemni_dni = [datetime(2023, 1, 1).date(), datetime(2023, 1, 2).date(), 
                     datetime(2023, 1, 3).date(), datetime(2023, 1, 4).date(), 
                     datetime(2023, 1, 5).date(), datetime(2023, 1, 6).date(), datetime(2023, 1, 7).date()]
    if not users:
        return {}
    
    start_date = datetime(2023, 12, 26).date()
    period = []
    for i in range(7):      
        period.append((start_date+timedelta(i)))
    have_bd = []

    for user in users:
        bd:date = user["birthday"]
        bd = bd.replace(year = start_date.year)

        # якщо змінений рік ДН входить в перші 7 днів нового року то збільшуємо рік на 1,
        # виняток - якщо день розсилки входить в перші 7 днів нового року, тоді залишаємо як є
        if bd in promlemni_dni and start_date not in promlemni_dni:
            bd = bd.replace(year = start_date.year + 1)

        if bd in period:
            #додаємо значення входженого елементу в окремй список,щоб вивести потім лише потрібні дні в словнику
            have_bd.append(user["name"])
            #робимо перевірку і наповнюємо відповідний ключ словника
            if bd.weekday() == 1:
                main_dict["Tuesday"].append(user["name"])
            elif bd.weekday() == 2:
                main_dict["Wednesday"].append(user["name"])
            elif bd.weekday() == 3:
                main_dict["Thursday"].append(user["name"])
            elif bd.weekday() == 4:
                main_dict["Friday"].append(user["name"])
            elif bd.weekday() == 0:
                main_dict["Monday"].append(user["name"])
            elif bd.weekday() == 5 and bd not in period[5:]:
                main_dict["Monday"].append(user["name"])
            elif bd.weekday() == 6 and bd not in period[6:]:
                main_dict["Monday"].append(user["name"])
    if have_bd == []:
        return {}
    for day, names in main_dict.items():
        if names == []:
            continue # прибираю дні тижня коли немає ДН
        else:
            finish_dict.update({day: names}) # наповнюю кінцевий словник лише заповненими днями тижня
            
    return finish_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
