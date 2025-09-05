import gamepie
if __name__ == "__main__":
    w1 = gamepie.Window.spawn(title="První okno", size=(400, 300))
    w2 = gamepie.Window.spawn(title="Druhé okno", size=(600, 400))
    
    gamepie.Window.join()


