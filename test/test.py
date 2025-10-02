def calculate_love_score(name1, name2):
    # Definiamo le due parole dove cercare le lettere
    parola_dove_cercare = "TRUE"
    parola_dove_cercare2 = "LOVE"

    # Convertiamo entrambe in minuscolo per fare un confronto case-insensitive
    parola_da_cercare = name1.lower()
    parola_da_cercare2 = name2.lower()
    parola_dove_cercare = parola_dove_cercare.lower()
    parola_dove_cercare2 = parola_dove_cercare2.lower()

    # Dizionario per memorizzare il conteggio delle corrispondenze per ogni lettera
    corrispondenze = {}
    corrispondenze1 = {}
    corrispondenze2 = {}
    corrispondenze3 = {}
    conteggio_name1 = 0
    conteggio_name2 = 0
    conteggio_name3 = 0
    conteggio_name4 = 0
    # Controlliamo ogni lettera di "Kanye West"
    for lettera in parola_da_cercare:
        conteggio = parola_dove_cercare.count(lettera)  # conta quante volte 'lettera' è in 'TRUE'
        corrispondenze[lettera] = conteggio
        if conteggio != 0:
            conteggio_name1 += conteggio
        # Stampiamo il risultato
        print("Corrispondenze trovate:")
        for lettera, count in corrispondenze.items():
            print(f"Lettera '{lettera}': {count} volta/e in 'true'")
        
    # Controlliamo ogni lettera di "Kanye West"
    for lettera in parola_da_cercare:
        conteggio1 = parola_dove_cercare2.count(lettera)  # conta quante volte 'lettera' è in 'LOVE'
        corrispondenze1[lettera] = conteggio1
        if conteggio1 != 0:
            conteggio_name2 += conteggio1
        # Stampiamo il risultato
        print("Corrispondenze trovate:")
        for lettera, count in corrispondenze1.items():
            print(f"Lettera '{lettera}': {count} volta/e in 'true'")
    
    # Controlliamo ogni lettera di "Kim Kardashian"
    for lettera in parola_da_cercare2:
        conteggio = parola_dove_cercare.count(lettera)  # conta quante volte 'lettera' è in 'TRUE'
        corrispondenze2[lettera] = conteggio
        if conteggio != 0:
            conteggio_name3 += conteggio
        # Stampiamo il risultato
        print("Corrispondenze trovate:")
        for lettera, count in corrispondenze2.items():
            print(f"Lettera '{lettera}': {count} volta/e in 'true'")
        
    # Controlliamo ogni lettera di "Kim Kardashian"
    for lettera in parola_da_cercare2:
        conteggio1 = parola_dove_cercare2.count(lettera)  # conta quante volte 'lettera' è in 'LOVE'
        corrispondenze3[lettera] = conteggio1
        if conteggio1 != 0:
            conteggio_name4 += conteggio1
        # Stampiamo il risultato
        print("Corrispondenze trovate:")
        for lettera, count in corrispondenze3.items():
            print(f"Lettera '{lettera}': {count} volta/e in 'true'")
    # Sommiamo i conteggi
    conteggio_tot1 = str(conteggio_name1) + str(conteggio_name2)
    conteggio_tot2 = str(conteggio_name3) + str(conteggio_name4)
    conteggio_tot = int(conteggio_tot1) + int(conteggio_tot2)   
    # Stampiamo il risultato
    print(f"Love score {conteggio_tot}")

calculate_love_score("Kanye West", "Kim Kardashian")