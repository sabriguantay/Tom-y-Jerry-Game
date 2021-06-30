
'''El siguiente programa consiste en la representación de Tom, 
la cual mediante la función Random elige el peso y distancia de ratones cercanos a Tom de manera aleatoria. 
Una vez elegidos, selecciona al ratón que le aporta mayor energía y se encuentra a una distancia más cercana. 
Este proceso se repetirá hasta que Tom se quede sin energía o si supera los 150 joules, 
en este caso el personaje no podrá comer más ratones'''

# ACLARACIONES A TENER EN CUENTA
# En la linea 107, se ejecuta un elif en el caso de que las energias y distancias sean iguales entre los 2 ratones
# Dentro de ese elif: se utiliza las variables "energía1" y "distancia1"
# Ya que es indistinto, si elegimos las variables del ratón 2

import random 
import definir

energía_inicial_tom = int (40)
peso_ratón = [50, 20, 23, 19, 44]
distancia_ratón = [5, 10, 20, 30, 40]
energía_acum = float = 0
contador = 0
print("|-----------------------------------|")
print("|Bienvenidos al juego de Tom y Jerry|")
print("|-----------------------------------|")
print("                                     ")
print("                                     ")
print("       _..---...,""-._    ,/}/)           ")
print("     .''        ,      ``..'(/-<            ")
print("    /   _      {      )         \           ")
print("   ;   _ `.     `.   <         a(             ")
print(" ,'   ( \  )      `.  \ __.._ .: y        (( )_, ")
print("(  <\_-) )'-.____...\  `._   //-'  .--.    \ '/   ")
print(" `. `-' /-._)))      `-._)))           )   / \=   ")
print("   `...'                              ( __/ _/     ")
print("                                     `-|   )_    ")
print("                                     ")
print("                                     ")

while energía_inicial_tom <= 40:
    peso_elegido1 = random.choice(peso_ratón)
    distancia_elegida1 = random.choice(distancia_ratón)

    peso_elegido2 = random.choice(peso_ratón)
    distancia_elegida2 = random.choice(distancia_ratón)

    energía1 = definir.obtener_energía_ganada(peso_elegido1)
    energía2 = definir.obtener_energía_ganada(peso_elegido2)
    energia_gastada1 = 0.5 * distancia_elegida1
    energia_gastada2 = 0.5 * distancia_elegida2
    energia_obtenida1 = energía1 - energia_gastada1
    energia_obtenida2 = energía2 - energia_gastada2

    print(" RATONES CERCANOS: \n  \n Ratón 1 = Peso: ", peso_elegido1, " - Distancia: ", distancia_elegida1, "\n Ratón 2 = "
                                                                                                        "Peso: ",
          peso_elegido2, " - Distancia: ", distancia_elegida2)
    print("----------------------------------------------------------------------")
    print(f"Ratón 1: Energia Ganada = {energía1} Energía gastada ={energia_gastada1}")
    print(f"Ratón 2: Energia Ganada = {energía2} Energía gastada ={energia_gastada2}" )
    print("         ")
    print(f"Si corre y come al ratón 1, obtiene {energia_obtenida1} de energía")
    print(f"Si corre y come al ratón 2, obtiene {energia_obtenida2} de energía")


    if energía1 > energía2 and distancia_elegida1 <= distancia_elegida2 or energía1 == energía2 and distancia_elegida1 < distancia_elegida2 or energia_obtenida1 > energia_obtenida2 :

        print("----------------------------------------------------------------------")
        print("         Le conviene comerse al ratón 1")
        if contador == 0:
            energía_antes_correr = energía_acum + energía_inicial_tom
            segundos_recorridos1 = definir.correr(energía_antes_correr, distancia_elegida1)
            print("----------------------------------------------------------------------")
            print("         Tom acaba de comerse al ratón que le da más energía")
            print("----------------------------------------------------------------------")
            print(" RESUMEN:")
            print("  Segundos recorridos: ", round (segundos_recorridos1,2))
            energía_acum = energía_acum + energía_inicial_tom + energía1 - energia_gastada1
            print("  Energia antes de correr:", energía_antes_correr)
            print("  Energia ganada:", energía1)
            print("  Energia gastada:", energia_gastada1)
            print("  Energia acum:", energía_acum)
            print("         ")
            print("#####################################################################")
            print("         ")
            contador =+ 1
        else:
            print("----------------------------------------------------------------------")
            print("         Tom acaba de comerse al ratón al ratón que le da más energía")
            print("----------------------------------------------------------------------")
            print(" RESUMEN:")
            energía_antes_correr = energía_acum
            segundos_recorridos1 = definir.correr(energía_antes_correr, distancia_elegida1)   
            print("  Segundos recorridos: ", round (segundos_recorridos1,2))
            energía_acum = energía_acum + energía1 - energia_gastada1
            print("  Energia antes de correr:", energía_antes_correr)
            print("  Energia ganada:", energía1)
            print("  Energia gastada:", energia_gastada1)
            print("  Energia acum:", energía_acum)
            print("         ")
            print("#####################################################################")
            print("         ")
            contador =+ 1

    elif energía1 == energía2 and distancia_elegida1 == distancia_elegida2:
        print("----------------------------------------------------------------------")
        print("  Estos ratones tienen el mismo peso y están a la misma distancia. \n  Por lo tanto, se va a generar la misma energía ganada y gastada \n  sin importar si se come al ratón 1 ó 2.")
        if contador == 0:
            energía_antes_correr = energía_acum + energía_inicial_tom
            segundos_recorridos1 = definir.correr(energía_antes_correr, distancia_elegida1)
            print("--------------------------------------------------------------------")
            print("         Tom acaba de comerse al ratón")
            print("--------------------------------------------------------------------")
            print(" RESUMEN:")
            print("  Segundos recorridos: ", round (segundos_recorridos1,2))
            energía_acum = energía_acum + energía_inicial_tom + energía1 - energia_gastada1
            print("  Energia antes de correr:", energía_antes_correr)
            print("  Energia ganada:", energía1)
            print("  Energia gastada:", energia_gastada1)
            print("  Energia acum:", energía_acum)
            print("         ")
            print("#####################################################################")
            print("         ")
            contador =+ 1

        else:
            energía_antes_correr = energía_acum
            segundos_recorridos1 = definir.correr(energía_antes_correr, distancia_elegida1)
            print("--------------------------------------------------------------------")
            print("         Tom acaba de comerse al ratón")
            print("--------------------------------------------------------------------")
            print("  Segundos recorridos: ", round (segundos_recorridos1,2))
            energía_acum = energía_acum + energía1 - energia_gastada1
            print("  Energia antes de correr:", energía_antes_correr)
            print("  Energia ganada:", energía1)
            print("  Energia gastada:", energia_gastada1)
            print("  Energia acum:", energía_acum)
            print("         ")
            print("#####################################################################")
            print("         ")
            contador =+ 1


    else:
        print("----------------------------------------------------------------------")
        print("         Le conviene comerse al ratón 2")
        if contador == 0: 
            print("----------------------------------------------------------------------")
            print("         Tom acaba de comerse al ratón que le da más energía")
            print("----------------------------------------------------------------------")
            print(" RESUMEN:")
            energía_antes_correr = energía_acum + energía_inicial_tom
            segundos_recorridos2 = definir.correr(energía_antes_correr, distancia_elegida2)
            print("  Segundos recorridos: ", round (segundos_recorridos2,2))
            energía_acum = energía_acum + energía_inicial_tom + energía2 - energia_gastada2
            print("  Energia antes de correr:", energía_antes_correr)
            print("  Energia ganada:", energía2)
            print("  Energia gastada:", energia_gastada2)
            print("  Energia acum:", energía_acum)
            print("         ")
            print("#####################################################################")
            print("         ")
            contador =+ 1

        else:
            print("--------------------------------------------------------------------")
            print("         Tom acaba de comerse al ratón que le da más energía")
            print("--------------------------------------------------------------------")
            print(" RESUMEN:")
            energía_antes_correr = energía_acum
            segundos_recorridos2 = definir.correr(energía_antes_correr, distancia_elegida2)
            print("  Segundos recorridos: ", round (segundos_recorridos2,2))
            energía_acum = energía_acum  + energía2 - energia_gastada2
            print("  Energia antes de correr:", energía_antes_correr)
            print("  Energia ganada:", energía2)
            print("  Energia gastada:", energia_gastada2)
            print("  Energia acum:", energía_acum)
            print("         ")
            print("#####################################################################")
            print("         ")
            contador =+ 1

    if energía_acum >= 150:
        print(" ")
        print("----------------------------------------------")
        print("  Fin del juego: [[Tom ya está muy gordo]]")
        print("----------------------------------------------")  

        print("  ________                                                  ")
        print(" /  _____/_____    _____   ____     _______  __ ___________ ")
        print("/   \  ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \ ")
        print("\    \_\  \/ __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/")
        print(" \______  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   ")
        break
    elif energía_acum <= 0:
        print("                                           ")
        print("-------------------------------------------")
        print("Fin del juego: [[Tom se quedó sin energía]]")
        print("-------------------------------------------")  
        print("  ________                                                  ")
        print(" /  _____/_____    _____   ____     _______  __ ___________ ")
        print("/   \  ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \ ")
        print("\    \_\  \/ __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/")
        print(" \______  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   ")
        break
