import datetime

WinterHolidaysStart24 = datetime.datetime(2024, 12, 23)
WinterHolidaysEnd24 = datetime.datetime(2025, 1, 2)
EasterHolidaysStart25 = datetime.datetime(2025, 4, 17)
EasterHolidaysEnd25 = datetime.datetime(2025, 4, 22)
SummerHolidaysStart25 = datetime.datetime(2025, 8, 8)
SummerHolidaysEnd25 = datetime.datetime(2025, 8, 20)
WinterHolidaysStart25 = datetime.datetime(2025, 12, 23)
WinterHolidaysEnd25 = datetime.datetime(2026, 1, 2)

DayOfGermanUnity2024 = datetime.datetime(2024, 10, 3)
EasterMonday2025 = datetime.datetime(2025, 4, 21)
LaborDay2025 = datetime.datetime(2025, 5, 1)
AscensionDay2025 = datetime.datetime(2025, 5, 29)
PentecostMonday2025 = datetime.datetime(2025, 6, 9)
DayOfGermanUnity2025 = datetime.datetime(2025, 10, 3)
ReformationDay2025 = datetime.datetime(2025, 10, 31)

question_date_str = input("Nenne das Datum, was geprüft werden soll. jjjj.mm.tt = ")

try:
    question_date = datetime.datetime.strptime(question_date_str, "%Y.%m.%d")
except ValueError:
    print("Das eingegebene Datum ist ungültig. Bitte im Format jjjj.mm.tt eingeben.")
    exit()

if WinterHolidaysStart24 <= question_date <= WinterHolidaysEnd24:
    print("Das Datum befindet sich in den Winterferien 2024.")
elif EasterHolidaysStart25 <= question_date <= EasterHolidaysEnd25:
    print("Das Datum befindet sich in den Osterferien 2025.")
elif SummerHolidaysStart25 <= question_date <= SummerHolidaysEnd25:
    print("Das Datum befindet sich in den Sommerferien 2025.")
elif WinterHolidaysStart25 <= question_date <= WinterHolidaysEnd25:
    print("Das Datum befindet sich in den Winterferien 2025.")
elif question_date == DayOfGermanUnity2024:
    print("Das Datum ist der Tag der deutschen Einheit 2024.")
elif question_date == EasterMonday2025:
    print("Das Datum ist Ostermontag 2025.")
elif question_date == LaborDay2025:
    print("Das Datum ist der Tag der Arbeit 2025.")
elif question_date == AscensionDay2025:
    print("Das Datum ist Christi Himmelfahrt 2025.")
elif question_date == PentecostMonday2025:
    print("Das Datum ist Pfingstmontag 2025.")
elif question_date == DayOfGermanUnity2025:
    print("Das Datum ist der Tag der deutschen Einheit 2025.")
elif question_date == ReformationDay2025:
    print("Das Datum ist der Reformationstag 2025.")
else:
    print("Es handelt sich um einen regulären Schultag, wenn es gerade ein Montag, Dienstag, Mittwoch, Donnerstag oder Freitag ist 😉")

