'''gehalt_von_der_uni = 1000
gehalt_von_der_arbeit = 20
gehalt_insgesamt = gehalt_von_der_uni + gehalt_von_der_arbeit #arithmetische addition 

print("Mein Gehalt beträgt " + str(gehalt_insgesamt))

print("Mein Gehalt beträgt", gehalt_insgesamt,"€")
'''


gehalt_von_der_uni = input("Gebe bitte dein Gehalt von der Uni ein ")
gehalt_von_dem_schwarzmarkt = input("Gebe bitte dein Gehalt vom Schwatzmarkt ein ")
gehalt_insgesamt = int(gehalt_von_der_uni) + int(gehalt_von_dem_schwarzmarkt)
print("Insgesamtes Gehalt beträgt", gehalt_insgesamt,"€")

