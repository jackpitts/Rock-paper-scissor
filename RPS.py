def player(prev_play, opponent_history=[], play_order={}):
    # Se è il primo turno, imposta la mossa dell'avversario su 'R'
    if not prev_play:
        prev_play = 'R'

    # Aggiungi la mossa dell'avversario alla sua cronologia
    opponent_history.append(prev_play)
    
    # Previsione di default
    prediction = 'P'

    # Dopo almeno 5 turni, inizia a cercare pattern
    if len(opponent_history) > 4:
        # Crea una chiave con le ultime 5 mosse dell'avversario
        last_five = "".join(opponent_history[-5:])
        
        # Aggiorna la frequenza di quella sequenza
        play_order[last_five] = play_order.get(last_five, 0) + 1
        
        # Costruisce le tre possibili sequenze future (le ultime 4 mosse + una nuova)
        potential_plays = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]

        # Cerca quale delle 3 sequenze è la più frequente
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }

        # Se trova almeno una sequenza, predice la prossima mossa più probabile
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    # Mappa che dice cosa giocare per battere la mossa prevista
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # Restituisce la mossa che batte quella prevista
    return ideal_response[prediction]
