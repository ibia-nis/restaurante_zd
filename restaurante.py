menus = {
    
  "lunes_1": "Sancocho",
  "p_lunes_1":3.00,
  "lunes_2": "Molleja",
  "p_lunes_2":0.50,
  "lunes_3": "Ensaladita",
  "p_lunes_3":2.00,
    
  "martes_1": "Corazón",
  "p_martes_1":0.30,
  "martes_2": "Hígado",
  "p_martes_2":0.80,
  "martes_3": "Carimañola",
  "p_martes_3":1.00,
    
  "miercoles_1": "Empanada de pollo",
  "p_miercoles_1":1.50,
  "miercoles_2": "Muslito",
  "p_miercoles_2":1.10,
  "miercoles_3": "Chicha de guanabana",
  "p_miercoles_3":1.00,
    
  "jueves_1": "Empanada de carne",
  "p_jueves_1":1.50,
  "jueves_2": "Chorizo",
  "p_jueves_2":0.90,
  "jueves_3": "Yuca frita",
  "p_jueves_3":0.50,
  
  "viernes_1": "Harina",
  "p_viernes_1":1.00,
  "viernes_2": "Salchicha guisada",
  "p_viernes_2":1.30,
  "viernes_3": "Tortilla frita",
  "p_viernes_3":0.50,
    
  "sabado_1": "Arepita",
  "p_sabado_1":0.75,
  "sabado_2": "Milanesa",
  "p_sabado_2":0.75,
  "sabado_3": "Tequeño",
  "p_sabado_3":0.55,
    
  "domingo_1": "Nuggets",
  "p_domingo_1":2.00,
  "domingo_2": "Avena",
  "p_domingo_2":1.00,
  "domingo_3": "Carne asada",
  "p_domingo_3":2.50
    
}
ordenar=1
valor=3
c_platillo=[0,0,0]

print("¡Bienvenid@ al Restaurant ZD! \nEscriba el número del día para ver el menú:\n1. Lunes\n2. Martes\n3. Miércoles\n4. Jueves\n5. Viernes\n6. Sábado\n7. Domingo\n")
while(ordenar==1):
    dia = input()
    if dia == "1":
        print(f'Platillos:\n1.{menus["lunes_1"]}({menus["p_lunes_1"]}$)\n2.{menus["lunes_2"]}({menus["p_lunes_2"]}$)\n3.{menus["lunes_3"]}({menus["p_lunes_3"]}$)\n')
        while(ordenar==1):
            platillo = input("¿Qué desea ordenar?\n")

            if platillo =="1":
                try:
                    c_platillo[0] = c_platillo[0]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            elif platillo =="2":
                try:
                    c_platillo[1] = c_platillo[1]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.') 
            elif platillo =="3":
                try:
                    c_platillo[2] = c_platillo[2]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            else:
                print("Escriba una opción del 1 al 3\n")

            while valor not in (0, 1):
                try:
                    valor = int(input("¿Desea seguir ordenando? Escriba 1 para seguir pidiendo, escriba 0 para imprimir su orden.\n"))

                    if valor not in (0,1):
                        print("Por favor, escriba una opción existente.\n")
                    else:
                        ordenar = valor
                except ValueError:
                    valor = print("Por favor escriba una opción existente.\n")
            valor = 3
        
        print(f'Va a ordenar:')
        if c_platillo[0] !=0:
            print(f'{c_platillo[0]} de {menus["lunes_1"]}({c_platillo[0]*menus["p_lunes_1"]:.2f}$)\n')
        if c_platillo[1] !=0:
            print(f'{c_platillo[1]} de {menus["lunes_2"]}({c_platillo[1]*menus["p_lunes_2"]:.2f}$)\n')
        if c_platillo[2] !=0:
            print(f'{c_platillo[2]} de {menus["lunes_3"]}({c_platillo[2]*menus["p_lunes_3"]:.2f}$)\n')
        total = c_platillo[0]*menus["p_lunes_1"] + c_platillo[1]*menus["p_lunes_2"]+c_platillo[2]*menus["p_lunes_3"]
        print(f'Total: {total:.2f}$\n')

        confirmar = 1

        while confirmar ==1:
            conf = input("Presiona 1 para confirmar o 2 para cancelar.\n")
            if conf=="1":
                print("¡Gracias por su compra!\n")
                confirmar = 0
            elif conf=="2":
                print("Pedido cancelado.\n")
                confirmar = 0
            else:
                print("Por favor, escribir una opción existente.\n")
                
    elif dia == "2":
        print(f'Platillos:\n1.{menus["martes_1"]}({menus["p_martes_1"]}$)\n2.{menus["martes_2"]}({menus["p_martes_2"]}$)\n3.{menus["martes_3"]}({menus["p_martes_3"]}$)\n')
        while(ordenar==1):
            platillo = input("¿Qué desea ordenar?\n")

            if platillo =="1":
                try:
                    c_platillo[0] = c_platillo[0]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            elif platillo =="2":
                try:
                    c_platillo[1] = c_platillo[1]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.') 
            elif platillo =="3":
                try:
                    c_platillo[2] = c_platillo[2]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            else:
                print("Escriba una opción del 1 al 3\n")

            while valor not in (0, 1):
                try:
                    valor = int(input("¿Desea seguir ordenando? Escriba 1 para seguir pidiendo, escriba 0 para imprimir su orden.\n"))

                    if valor not in (0,1):
                        print("Por favor, escriba una opción existente.\n")
                    else:
                        ordenar = valor
                except ValueError:
                    valor = print("Por favor escriba una opción existente.\n")
            valor = 3
        
        print(f'Va a ordenar:')
        if c_platillo[0] !=0:
            print(f'{c_platillo[0]} de {menus["martes_1"]}({c_platillo[0]*menus["p_martes_1"]:.2f}$)\n')
        if c_platillo[1] !=0:
            print(f'{c_platillo[1]} de {menus["martes_2"]}({c_platillo[1]*menus["p_martes_2"]:.2f}$)\n')
        if c_platillo[2] !=0:
            print(f'{c_platillo[2]} de {menus["martes_3"]}({c_platillo[2]*menus["p_martes_3"]:.2f}$)\n')
        total = c_platillo[0]*menus["p_martes_1"] + c_platillo[1]*menus["p_martes_2"]+c_platillo[2]*menus["p_martes_3"]
        print(f'Total: {total:.2f}$\n')

        confirmar = 1

        while confirmar ==1:
            conf = input("Presiona 1 para confirmar o 2 para cancelar.\n")
            if conf=="1":
                print("¡Gracias por su compra!\n")
                confirmar = 0
            elif conf=="2":
                print("Pedido cancelado.\n")
                confirmar = 0
            else:
                print("Por favor, escribir una opción existente.\n")
                
    elif dia == "3":
        print(f'Platillos:\n1.{menus["miercoles_1"]}({menus["p_miercoles_1"]}$)\n2.{menus["miercoles_2"]}({menus["p_miercoles_2"]}$)\n3.{menus["miercoles_3"]}({menus["p_miercoles_3"]}$)\n')
        while(ordenar==1):
            platillo = input("¿Qué desea ordenar?\n")

            if platillo =="1":
                try:
                    c_platillo[0] = c_platillo[0]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            elif platillo =="2":
                try:
                    c_platillo[1] = c_platillo[1]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.') 
            elif platillo =="3":
                try:
                    c_platillo[2] = c_platillo[2]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            else:
                print("Escriba una opción del 1 al 3\n")

            while valor not in (0, 1):
                try:
                    valor = int(input("¿Desea seguir ordenando? Escriba 1 para seguir pidiendo, escriba 0 para imprimir su orden.\n"))

                    if valor not in (0,1):
                        print("Por favor, escriba una opción existente.\n")
                    else:
                        ordenar = valor
                except ValueError:
                    valor = print("Por favor escriba una opción existente.\n")
            valor = 3
        
        print(f'Va a ordenar:')
        if c_platillo[0] !=0:
            print(f'{c_platillo[0]} de {menus["miercoles_1"]}({c_platillo[0]*menus["p_miercoles_1"]:.2f}$)\n')
        if c_platillo[1] !=0:
            print(f'{c_platillo[1]} de {menus["miercoles_2"]}({c_platillo[1]*menus["p_miercoles_2"]:.2f}$)\n')
        if c_platillo[2] !=0:
            print(f'{c_platillo[2]} de {menus["miercoles_3"]}({c_platillo[2]*menus["p_miercoles_3"]:.2f}$)\n')
        total = c_platillo[0]*menus["p_miercoles_1"] + c_platillo[1]*menus["p_miercoles_2"]+c_platillo[2]*menus["p_miercoles_3"]
        print(f'Total: {total:.2f}$\n')

        confirmar = 1

        while confirmar ==1:
            conf = input("Presiona 1 para confirmar o 2 para cancelar.\n")
            if conf=="1":
                print("¡Gracias por su compra!\n")
                confirmar = 0
            elif conf=="2":
                print("Pedido cancelado.\n")
                confirmar = 0
            else:
                print("Por favor, escribir una opción existente.\n")
                
    elif dia == "4":
        print(f'Platillos:\n1.{menus["jueves_1"]}({menus["p_jueves_1"]}$)\n2.{menus["jueves_2"]}({menus["p_jueves_2"]}$)\n3.{menus["jueves_3"]}({menus["p_jueves_3"]}$)\n')
        while(ordenar==1):
            platillo = input("¿Qué desea ordenar?\n")

            if platillo =="1":
                try:
                    c_platillo[0] = c_platillo[0]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            elif platillo =="2":
                try:
                    c_platillo[1] = c_platillo[1]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.') 
            elif platillo =="3":
                try:
                    c_platillo[2] = c_platillo[2]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            else:
                print("Escriba una opción del 1 al 3\n")

            while valor not in (0, 1):
                try:
                    valor = int(input("¿Desea seguir ordenando? Escriba 1 para seguir pidiendo, escriba 0 para imprimir su orden.\n"))

                    if valor not in (0,1):
                        print("Por favor, escriba una opción existente.\n")
                    else:
                        ordenar = valor
                except ValueError:
                    valor = print("Por favor escriba una opción existente.\n")
            valor = 3
        
        print(f'Va a ordenar:')
        if c_platillo[0] !=0:
            print(f'{c_platillo[0]} de {menus["jueves_1"]}({c_platillo[0]*menus["p_jueves_1"]:.2f}$)\n')
        if c_platillo[1] !=0:
            print(f'{c_platillo[1]} de {menus["jueves_2"]}({c_platillo[1]*menus["p_jueves_2"]:.2f}$)\n')
        if c_platillo[2] !=0:
            print(f'{c_platillo[2]} de {menus["jueves_3"]}({c_platillo[2]*menus["p_jueves_3"]:.2f}$)\n')
        total = c_platillo[0]*menus["p_jueves_1"] + c_platillo[1]*menus["p_jueves_2"]+c_platillo[2]*menus["p_jueves_3"]
        print(f'Total: {total:.2f}$\n')

        confirmar = 1

        while confirmar ==1:
            conf = input("Presiona 1 para confirmar o 2 para cancelar.\n")
            if conf=="1":
                print("¡Gracias por su compra!\n")
                confirmar = 0
            elif conf=="2":
                print("Pedido cancelado.\n")
                confirmar = 0
            else:
                print("Por favor, escribir una opción existente.\n")
    
    elif dia == "5":
        print(f'Platillos:\n1.{menus["viernes_1"]}({menus["p_viernes_1"]}$)\n2.{menus["viernes_2"]}({menus["p_viernes_2"]}$)\n3.{menus["viernes_3"]}({menus["p_viernes_3"]}$)\n')
        while(ordenar==1):
            platillo = input("¿Qué desea ordenar?\n")

            if platillo =="1":
                try:
                    c_platillo[0] = c_platillo[0]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            elif platillo =="2":
                try:
                    c_platillo[1] = c_platillo[1]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.') 
            elif platillo =="3":
                try:
                    c_platillo[2] = c_platillo[2]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            else:
                print("Escriba una opción del 1 al 3\n")

            while valor not in (0, 1):
                try:
                    valor = int(input("¿Desea seguir ordenando? Escriba 1 para seguir pidiendo, escriba 0 para imprimir su orden.\n"))

                    if valor not in (0,1):
                        print("Por favor, escriba una opción existente.\n")
                    else:
                        ordenar = valor
                except ValueError:
                    valor = print("Por favor escriba una opción existente.\n")
            valor = 3
        
        print(f'Va a ordenar:')
        if c_platillo[0] !=0:
            print(f'{c_platillo[0]} de {menus["viernes_1"]}({c_platillo[0]*menus["p_viernes_1"]:.2f}$)\n')
        if c_platillo[1] !=0:
            print(f'{c_platillo[1]} de {menus["viernes_2"]}({c_platillo[1]*menus["p_viernes_2"]:.2f}$)\n')
        if c_platillo[2] !=0:
            print(f'{c_platillo[2]} de {menus["viernes_3"]}({c_platillo[2]*menus["p_viernes_3"]:.2f}$)\n')
        total = c_platillo[0]*menus["p_viernes_1"] + c_platillo[1]*menus["p_viernes_2"]+c_platillo[2]*menus["p_viernes_3"]
        print(f'Total: {total:.2f}$\n')

        confirmar = 1

        while confirmar ==1:
            conf = input("Presiona 1 para confirmar o 2 para cancelar.\n")
            if conf=="1":
                print("¡Gracias por su compra!\n")
                confirmar = 0
            elif conf=="2":
                print("Pedido cancelado.\n")
                confirmar = 0
            else:
                print("Por favor, escribir una opción existente.\n")
    
    elif dia == "6":
        print(f'Platillos:\n1.{menus["sabado_1"]}({menus["p_sabado_1"]}$)\n2.{menus["sabado_2"]}({menus["p_sabado_2"]}$)\n3.{menus["sabado_3"]}({menus["p_sabado_3"]}$)\n')
        while(ordenar==1):
            platillo = input("¿Qué desea ordenar?\n")

            if platillo =="1":
                try:
                    c_platillo[0] = c_platillo[0]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            elif platillo =="2":
                try:
                    c_platillo[1] = c_platillo[1]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.') 
            elif platillo =="3":
                try:
                    c_platillo[2] = c_platillo[2]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            else:
                print("Escriba una opción del 1 al 3\n")

            while valor not in (0, 1):
                try:
                    valor = int(input("¿Desea seguir ordenando? Escriba 1 para seguir pidiendo, escriba 0 para imprimir su orden.\n"))

                    if valor not in (0,1):
                        print("Por favor, escriba una opción existente.\n")
                    else:
                        ordenar = valor
                except ValueError:
                    valor = print("Por favor escriba una opción existente.\n")
            valor = 3
        
        print(f'Va a ordenar:')
        if c_platillo[0] !=0:
            print(f'{c_platillo[0]} de {menus["sabado_1"]}({c_platillo[0]*menus["p_sabado_1"]:.2f}$)\n')
        if c_platillo[1] !=0:
            print(f'{c_platillo[1]} de {menus["sabado_2"]}({c_platillo[1]*menus["p_sabado_2"]:.2f}$)\n')
        if c_platillo[2] !=0:
            print(f'{c_platillo[2]} de {menus["sabado_3"]}({c_platillo[2]*menus["p_sabado_3"]:.2f}$)\n')
        total = c_platillo[0]*menus["p_sabado_1"] + c_platillo[1]*menus["p_sabado_2"]+c_platillo[2]*menus["p_sabado_3"]
        print(f'Total: {total:.2f}$\n')

        confirmar = 1

        while confirmar ==1:
            conf = input("Presiona 1 para confirmar o 2 para cancelar.\n")
            if conf=="1":
                print("¡Gracias por su compra!\n")
                confirmar = 0
            elif conf=="2":
                print("Pedido cancelado.\n")
                confirmar = 0
            else:
                print("Por favor, escribir una opción existente.\n")
    
    elif dia == "7":
        print(f'Platillos:\n1.{menus["domingo_1"]}({menus["p_domingo_1"]}$)\n2.{menus["domingo_2"]}({menus["p_domingo_2"]}$)\n3.{menus["domingo_3"]}({menus["p_domingo_3"]}$)\n')
        while(ordenar==1):
            platillo = input("¿Qué desea ordenar?\n")

            if platillo =="1":
                try:
                    c_platillo[0] = c_platillo[0]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            elif platillo =="2":
                try:
                    c_platillo[1] = c_platillo[1]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.') 
            elif platillo =="3":
                try:
                    c_platillo[2] = c_platillo[2]+int(input("¿Cuantos quiere?\n"))
                except ValueError:
                    print('Por favor escriba un número.')
            else:
                print("Escriba una opción del 1 al 3\n")

            while valor not in (0, 1):
                try:
                    valor = int(input("¿Desea seguir ordenando? Escriba 1 para seguir pidiendo, escriba 0 para imprimir su orden.\n"))

                    if valor not in (0,1):
                        print("Por favor, escriba una opción existente.\n")
                    else:
                        ordenar = valor
                except ValueError:
                    valor = print("Por favor escriba una opción existente.\n")
            valor = 3
        
        print(f'Va a ordenar:')
        if c_platillo[0] !=0:
            print(f'{c_platillo[0]} de {menus["domingo_1"]}({c_platillo[0]*menus["p_domingo_1"]:.2f}$)\n')
        if c_platillo[1] !=0:
            print(f'{c_platillo[1]} de {menus["domingo_2"]}({c_platillo[1]*menus["p_domingo_2"]:.2f}$)\n')
        if c_platillo[2] !=0:
            print(f'{c_platillo[2]} de {menus["domingo_3"]}({c_platillo[2]*menus["p_domingo_3"]:.2f}$)\n')
        total = c_platillo[0]*menus["p_domingo_1"] + c_platillo[1]*menus["p_domingo_2"]+c_platillo[2]*menus["p_domingo_3"]
        print(f'Total: {total:.2f}$\n')

        confirmar = 1

        while confirmar ==1:
            conf = input("Presiona 1 para confirmar o 2 para cancelar.\n")
            if conf=="1":
                print("¡Gracias por su compra!\n")
                confirmar = 0
            elif conf=="2":
                print("Pedido cancelado.\n")
                confirmar = 0
            else:
                print("Por favor, escribir una opción existente.\n")
    else:
        print("Por favor escriba una opción válida.\n")
