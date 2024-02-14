# Scrieți un program care afișează datele voastre personale sub forma unei
# cărți de vizită, precum a mea – fiți inventivi

def afisare_carte_vizita():
    nume=input("Numele tau complet:");
    profesie=input("Profesia ta:");
    telefon=input('Numarul de telefon:');
    email=input('Email-ul tau:');
    print("\nCarte de Vizita:");
    print("-" * 30);
    print(f"Nume: {nume}");
    print(f"Profesie: {profesie}");
    print(f"Telefon: {telefon}");
    print(f"Email: {email}");
    print("-" * 30);
afisare_carte_vizita();
