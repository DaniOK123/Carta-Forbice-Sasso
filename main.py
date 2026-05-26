import random

gesto = ['carta', 'forbice', 'sasso']

def game():

    punteggio_mio = 0
    punteggio_computer = 0

    print('Benvenuti alla nuova sfida di carta, forbice, sasso')
    

    while True:

        scelta = input('Vuoi iniziare un nuovo round? (y/n): ')

        if scelta == 'n':
            print('Grazie per aver giocato!')
            break
        
        elif scelta == 'y':

            while True:
                       
                if punteggio_mio == 5:  #non funziona
                    print("Hai vinto la partita!!!")  
                    return

                elif punteggio_computer == 5: #non funziona
                    print("Hai perso la partita!!!")
                    return
            
                risultato = f"Il risultato è: io - {punteggio_mio} : {punteggio_computer} - computer"
                print(risultato)

                scelta = input(f"Ora inizia il gioco, scegli la tua mossa tra {gesto}: ")

                if scelta != 'carta' and scelta != 'forbice' and scelta != 'sasso':
                    print('Devi scegliere tra questi tre!')

                elif scelta == 'carta' or scelta == 'forbice' or scelta == 'sasso':

                    caso = random.choice(gesto)
                    print(f'Il computer ha scelto {caso}!')

                    if scelta == caso:
                        print("Pareggio!")
                        print(f"Il risultato è: io - {punteggio_mio} : {punteggio_computer} - computer")
                        

                    elif scelta == 'carta' and caso == 'forbice':
                        print('Hai perso!')
                        punteggio_computer += 1
                        print(f"Il risultato è: io - {punteggio_mio} : {punteggio_computer} - computer")
                        

                    elif scelta == 'carta' and caso == 'sasso':
                        print('Hai vinto!')
                        punteggio_mio += 1
                        print(f"Il risultato è: io - {punteggio_mio} : {punteggio_computer} - computer")
                        

                    elif scelta == 'forbice' and caso == 'carta':
                        print('Hai vinto!')
                        punteggio_mio += 1
                        print(f"Il risultato è: io - {punteggio_mio} : {punteggio_computer} - computer")
                        

                    elif scelta == 'forbice' and caso == 'sasso':
                        print('Hai perso!')
                        punteggio_computer += 1
                        print(f"Il risultato è: io - {punteggio_mio} : {punteggio_computer} - computer")
                        

                    elif scelta == 'sasso' and caso == 'carta':
                        print('Hai perso!')
                        punteggio_computer += 1
                        print(f"Il risultato è: io - {punteggio_mio} : {punteggio_computer} - computer")
                        
                    
                    elif scelta == 'sasso' and caso == 'forbice':
                        print('Hai vinto!')
                        punteggio_mio += 1
                        print(f"Il risultato è: io - {punteggio_mio} : {punteggio_computer} - computer")
                        
                        
                    
                    if punteggio_mio > punteggio_computer:
                        print("Stai vincendo!")
                        break
                    
                    elif punteggio_mio < punteggio_computer:
                        print("Stai perdendo!")
                        break

                    elif punteggio_mio == punteggio_computer:
                        print("Stai pareggiando!")
                        break
            
        else:
            print('Deve essere una scelta tra y e n')

        

game()