from pathlib import Path, PureWindowsPath

forrásfájl = PureWindowsPath("C:\\Users\\agostonaf\\Desktop\\raspberries.txt")
hely = Path(forrásfájl)
fájl = open(forrásfájl, "w", encoding = "utf-8")
rpik = []
for sor in fájl:
    rpik.append(sor.strip().split(";"))
fájl.close()