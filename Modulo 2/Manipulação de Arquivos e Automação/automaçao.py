import pyautogui as pg

#pg.mouseInfo()


pg.press("win")

pg.sleep(1)
pg.write("chrome",interval=0.5)
pg.press("enter")
pg.sleep(1)
pg.write("www.youtube.corm")
pg.sleep(1)
pg.press("enter")

#move o mouse para a caixa de pesquisa do youtube
pg.moveTo(1592,177, duration=0.5)

pg.sleep(2)

pg.click()
pg.write("messi", interval=0.5)
pg.press("enter")

