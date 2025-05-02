import pyautogui as autogui


def Iniciar():


    autogui.PAUSE= 2.5
    
    #entra até o somee
    autogui.hotkey("win","r")    
    autogui.write("explorer")
    autogui.press('enter')
    
    autogui.press('win')
    autogui.write("txt")
    autogui.press('enter')
    autogui.hotkey("win","up")    
    autogui.click(x =372, y=300)
    autogui.hotkey("ctrl","a")    
    autogui.hotkey("ctrl","c")   
    autogui.hotkey("alt","f4")         
    autogui.click(x=372, y=60,clicks=2)
    autogui.hotkey("ctrl","a")        
    autogui.hotkey("ctrl","v")    
    autogui.press('enter')
   
    autogui.click(x=372, y=60,clicks=2)
    autogui.hotkey("ctrl","a")        
    autogui.write("cmd")
    autogui.press('enter')
    autogui.click(x =372, y=300)
    autogui.write("code .")
    autogui.press('enter')
    autogui.click(x =372, y=300)
    autogui.hotkey("alt","tab")
    autogui.hotkey("alt","f4")         
    autogui.hotkey("ctrl","shift","e")         
    autogui.scroll(-5,x=181,y=239)
    autogui.click(x=128, y=419)
    autogui.click(x=669, y=286)
    autogui.press('f5')
    autogui.press('enter')
    
    


        
Iniciar()

def mouse_local():
    autogui.sleep(3)
    mouse=str(autogui.position())
 
    mouse=f"{mouse.rsplit("(")[1] .rstrip(")")}"

    #autogui.click(x =650, y=322)
    print(f"autogui.click({mouse})")


#mouse_local()
