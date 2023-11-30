from forex_python.converter import CurrencyRates # from forex_python.converter ( c'est mon placard qui contient mes outils )


def convertir_monnaie(somme, unitesource, unitefinale): # definir ma fonction
    c = CurrencyRates() # c'est le moulle que je vais utiliser  
    
    result = c.convert(unitesource, unitefinale, somme) # les ingredients utiliser ( parametre)

    return result



somme = int(input("Somme a convertir : "))
unitesource = input("Monnaie d'origine : ").upper() # upper met notre string en majuscules
unitefinale = input("Monnaie à échanger : ").upper()

resultat = convertir_monnaie(somme, unitesource, unitefinale) # resultat et le return de ma fonction

print(resultat) # j'appelle ma fonction