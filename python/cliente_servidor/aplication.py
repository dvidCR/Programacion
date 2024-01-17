import sys
import random

while (True):
    try:
        from AppOpener import open, close, mklist, give_appnames
        import pyautogui
        break
    except ImportError as e:
        instalar = input(f"{e}, ¿quieres instalarla?(y/n): ")
        if instalar == "y":
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "AppOpener"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
            print("Se ha instalado correctamente")
            break
        else:
            print(e)
            quit()
            
class Aplication:
    
    def abrir(self, app, vip = 0):
        if vip == 0:
            open(app)
        elif vip == 999:
            open(app, output = False)
    
    def cerrar(self, app, vip = 0):
        if vip == 0:
            close(app)
        elif vip == 999:
            close(app, output = False)
            
    def comprobarPantalla(self):
        self.size = []
        for i in pyautogui.size():
            if not int:
                pass
            else:
                self.size.append(i - 1)
                
    def moverMouse(self):
        self.comprobarPantalla()
        x = random.randint(0, self.size[0])
        y = random.randint(0, self.size[1])
        
        pyautogui.moveTo(x, y)