# Auf den 17.06.2024 als Hausaufgabe:

# Schreibe eine Funktion aufsteigend_sortiert(liste: list) -> bool, die eine Liste von Integern erhält und
# zurückgibt, ob diese aufsteigend sortiert ist oder nicht.
# Z.B.: aufsteigend_sortiert([1, 4, 6, 6, 9, 10]) == True, aufsteigend_sortiert([10, 13, 4, 9]) == False.



def aufsteigend_sortiert(liste: list) -> bool:
  i = 0 
  while i < len(liste):
    if liste[i] > liste[i + 1]:
        return False
    i +=1
  return True

print(aufsteigend_sortiert([1, 4, 6, 6, 9, 11]))
    
    #    if aufsteigend_sortiert <= 11:
   #         print("Ja")
    #    else:
    #        print("Nein")
#
#
 #       

    #aufsteigenortiert([10, 13, 4, 9])