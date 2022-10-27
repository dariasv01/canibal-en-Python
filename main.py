def checkEstado(estadoAct, estadoHis):
    if (estadoAct[0][0] >= estadoAct[0][1]) or (estadoAct[0][0] == 0):
        if (estadoAct[1][0] >= estadoAct[1][1]) or (estadoAct[1][0] == 0):
            if estadoAct not in estadoHis:
                return True
    return False


def viaje(estadoAct, estadoHis):
    orillaIzquierdaM = estadoAct[0][0]
    orillaDerechaM = estadoAct[1][0]
    orillaIzquierdaC = estadoAct[0][1]
    orillaDerechaC = estadoAct[1][1]
    barca: bool = estadoAct[2]
    estadoHis.append([[orillaIzquierdaM, orillaIzquierdaC], [orillaDerechaM, orillaDerechaC], barca])
    if orillaDerechaM == 3 and orillaDerechaC == 3:
        print("SOLUTION:")
        for n in estadoHis:
            if n[2]:
                print(f"{n[0]} \__/---> {n[1]}")
            else:
                print(f"{n[0]} <---\__/ {n[1]}")
    else:
        if barca:
            # Misionero
            if orillaIzquierdaM >= 2:
                estadoAct[0][0] -= 2
                estadoAct[1][0] += 2
                estadoAct[2] = False
                if checkEstado(estadoAct, estadoHis):
                    viaje(estadoAct, estadoHis)
            estadoAct = [[orillaIzquierdaM, orillaIzquierdaC], [orillaDerechaM, orillaDerechaC], barca]

            # Canival
            if orillaIzquierdaC >= 2:
                estadoAct[0][1] -= 2
                estadoAct[1][1] += 2
                estadoAct[2] = False
                if checkEstado(estadoAct, estadoHis):
                    viaje(estadoAct, estadoHis)
            estadoAct = [[orillaIzquierdaM, orillaIzquierdaC], [orillaDerechaM, orillaDerechaC], barca]

            # Misionero Canival
            if orillaIzquierdaM >= 1 and orillaIzquierdaC >= 1:
                estadoAct[0][0] -= 1
                estadoAct[0][1] -= 1
                estadoAct[1][0] += 1
                estadoAct[1][1] += 1
                estadoAct[2] = False
                if checkEstado(estadoAct, estadoHis):
                    viaje(estadoAct, estadoHis)
            estadoAct = [[orillaIzquierdaM, orillaIzquierdaC], [orillaDerechaM, orillaDerechaC], barca]
        else:
            # Misionero
            if orillaDerechaM >= 1:
                estadoAct[1][0] -= 1
                estadoAct[0][0] += 1
                estadoAct[2] = True
                if checkEstado(estadoAct, estadoHis):
                    viaje(estadoAct, estadoHis)
            estadoAct = [[orillaIzquierdaM, orillaIzquierdaC], [orillaDerechaM, orillaDerechaC], barca]

            if orillaDerechaM >= 2:
                estadoAct[1][0] -= 2
                estadoAct[0][0] += 2
                estadoAct[2] = True
                if checkEstado(estadoAct, estadoHis):
                    viaje(estadoAct, estadoHis)
            estadoAct = [[orillaIzquierdaM, orillaIzquierdaC], [orillaDerechaM, orillaDerechaC], barca]

            # Canival
            if orillaDerechaC >= 1:
                estadoAct[1][1] -= 1
                estadoAct[0][1] += 1
                estadoAct[2] = True
                if checkEstado(estadoAct, estadoHis):
                    viaje(estadoAct, estadoHis)
            estadoAct = [[orillaIzquierdaM, orillaIzquierdaC], [orillaDerechaM, orillaDerechaC], barca]

            if orillaDerechaC >= 2:
                estadoAct[1][1] -= 2
                estadoAct[0][1] += 2
                estadoAct[2] = True
                if checkEstado(estadoAct, estadoHis):
                    viaje(estadoAct, estadoHis)
            estadoAct = [[orillaIzquierdaM, orillaIzquierdaC], [orillaDerechaM, orillaDerechaC], barca]

            # Misionero Canival
            if orillaDerechaC >= 1 and orillaDerechaM >= 1:
                estadoAct[1][1] -= 1
                estadoAct[0][1] += 1
                estadoAct[1][0] -= 1
                estadoAct[0][0] += 1
                estadoAct[2] = True
                if checkEstado(estadoAct, estadoHis):
                    viaje(estadoAct, estadoHis)
            estadoAct = [[orillaIzquierdaM, orillaIzquierdaC], [orillaDerechaM, orillaDerechaC], barca]


viaje([[3, 3], [0, 0], True], [])
