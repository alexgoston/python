OLVADÁSI_PONT = 1539
FORRÁSI_PONT = 2750
hofok = int(input('Milyen hőfokú a 26Fe?'))
if hofok < OLVADÁSI_PONT:
    print("A 26Fe vas szilárd halmazállapotú.")
elif hofok < FORRÁSI_PONT:
    print("A 26Fe vas folyékony halmazállapotú.")
else:
    print("A 26Fe vas gáz halmazállapotú.")