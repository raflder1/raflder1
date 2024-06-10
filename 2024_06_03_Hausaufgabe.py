# Auf den 10.06.2024 als Hausaufgabe:

# Schreibe eine Funktion fakultät(zahl: int) -> int, die die Fakultät der übergebenen Zahl berechnet und zurückgibt.
# Recherchiere gegebenenfalls im Internet, was die Fakultät einer Zahl ist.
# Beispiel: fakultät(5) == 120.
# Falls eine negative Zahl übergeben wird, soll 0 zurückgegeben werden.

# TODO

def fakultät(zahl: int) -> int:
    
    if zahl < 0:
        return 0
    result = 1
    for i in range(1, zahl + 1):
        result *= i 
    return result


print(fakultät(5))


def fakultät_q(zahl: int) -> int:
    if zahl < 0:
        return 0
    result = 1
    i = 1
    while i <= zahl:
        result *=  i
        i += 1
    return result
print(fakultät_q(5))
 #   Zahl =7
  #  for i in range(18):
   #     print(fakultät)
#