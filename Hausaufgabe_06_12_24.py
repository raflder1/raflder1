#breite = parameter#775
#höhe = parameter#
def a_rechteck(breite:int,höhe:int) -> int:
    return breite * höhe
rechnung = a_rechteck(775,125)
print(rechnung)

#dreieck

def a_dreieck(länge_grunseite:int,höhe:int) -> float:
    return länge_grunseite * höhe * 0.5
rechnung = a_dreieck(85,205)
print(rechnung)