question_date = input("Nenne das Datum, was geprüft werden soll. jjjj.mm.tt = ")

# winterferien 24 23.12.24 - 02.01.25
# Osterferien 25 17.04.25 - 22.04.25
# Sommerferien 25 08.08.25 - 20.08.25
# Winterferien 25 23.12.25 - 02.01.26

WinterHolidaysStart24 = "2024.12.23"
WinterHolidaysEnd24 = "2025.01.02"
EasterHolidaysStart25 = "2025.04.17"
EasterHolidaysEnd25 = "2025.04.22"
SummerHolidaysStart25 = "2025.08.08"
SummerHolidaysEnd25 = "2025.08.20"
WinterHolidaysStart25 = "2025.12.23"
WinterHolidaysEnd25 = "2026.01.02"

if WinterHolidaysStart24 <= question_date <= WinterHolidaysEnd24:
    print("Das Datum befindet sich in den Winterferien 2024.")
elif EasterHolidaysStart25 <= question_date <= EasterHolidaysEnd25:
    print("Das Datum befindet sich in den Osterferien 2025.")
elif SummerHolidaysStart25 <= question_date <= SummerHolidaysEnd25:
    print("Das Datum befindet sich in den Sommerferien 2025.")
elif WinterHolidaysStart25 <= question_date <= WinterHolidaysEnd25:
    print("Das Datum befindet sich in den Winterferien 2025.")
else:
    print("Es geht handelt sich um einen Regulären Schlungstag , wenn es gerade ein  Monatg, Dienstag ,Mittwoch, Donnerstag oder Freitag ist 🧐")
