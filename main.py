import random

GESTI = ['carta', 'forbice', 'sasso']
PUNTEGGIO_VITTORIA = 5

# Dizionario che definisce chi batte chi:
# chiave = mossa del giocatore, valore = mossa che il giocatore batte
VINCE_CONTRO = {
    'carta':   'sasso',
    'forbice': 'carta',
    'sasso':   'forbice',
}


def benvenuto():
    print('Benvenuti alla nuova sfida di carta, forbice, sasso!')
    print(f'Il primo a raggiungere {PUNTEGGIO_VITTORIA} punti vince la partita.\n')


def chiedi_mossa():
    """Chiede al giocatore la sua mossa finché non è valida."""
    while True:
        scelta = input(f"Scegli la tua mossa tra {GESTI}: ").strip().lower()
        if scelta in GESTI:
            return scelta
        print('Devi scegliere tra carta, forbice e sasso!')


def valuta_round(mossa_giocatore, mossa_computer):
    """
    Restituisce:
      1  se vince il giocatore
     -1  se vince il computer
      0  in caso di pareggio
    """
    if mossa_giocatore == mossa_computer:
        return 0
    if VINCE_CONTRO[mossa_giocatore] == mossa_computer:
        return 1
    return -1


def mostra_punteggio(mio, computer):
    print(f"Punteggio  →  Tu: {mio}  |  Computer: {computer}")


def gioca_round(punteggio_mio, punteggio_computer):
    """Gioca un singolo round e restituisce i punteggi aggiornati."""
    mossa_giocatore = chiedi_mossa()
    mossa_computer  = random.choice(GESTI)
    print(f'Il computer ha scelto: {mossa_computer}')

    esito = valuta_round(mossa_giocatore, mossa_computer)

    if esito == 0:
        print('Pareggio!')
    elif esito == 1:
        print('Hai vinto questo round!')
        punteggio_mio += 1
    else:
        print('Hai perso questo round!')
        punteggio_computer += 1

    mostra_punteggio(punteggio_mio, punteggio_computer)
    return punteggio_mio, punteggio_computer


def gioca_partita():
    """Gestisce una partita completa (fino a PUNTEGGIO_VITTORIA punti)."""
    punteggio_mio       = 0
    punteggio_computer  = 0

    while punteggio_mio < PUNTEGGIO_VITTORIA and punteggio_computer < PUNTEGGIO_VITTORIA:

        continua = input('\nVuoi giocare un round? (y/n): ').strip().lower()

        if continua == 'n':
            print('Partita interrotta. Arrivederci!')
            return
        elif continua != 'y':
            print("Risposta non valida. Inserisci 'y' per continuare o 'n' per uscire.")
            continue

        punteggio_mio, punteggio_computer = gioca_round(punteggio_mio, punteggio_computer)

        # Stato intermedio della partita
        if punteggio_mio > punteggio_computer:
            print('Stai vincendo!')
        elif punteggio_mio < punteggio_computer:
            print('Stai perdendo!')
        else:
            print('Siete in parità!')

    # Risultato finale
    if punteggio_mio == PUNTEGGIO_VITTORIA:
        print('\n🎉 Hai vinto la partita!')
    else:
        print('\n💀 Hai perso la partita!')


def game():
    benvenuto()
    gioca_partita()


if __name__ == '__main__':
    game()