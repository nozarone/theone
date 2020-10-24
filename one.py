doubleClick("1602795011371.png")
wait("1602798230471.png")
click("1602798230471.png")
type("qa.jtalks.org/jcommune" + Key.ENTER)
if exists("1602796334646.png"):
    click(Pattern("1602796334646.png").targetOffset(14,-1))
    wait("1602796422443.png")
    click("1602797087642.png")
click(Pattern("1602795689793.png").targetOffset(1,1))
wait("1602795736250.png")
click("1602795758054.png")
type("nozar")
click("1602795794262.png")
type("admin")
click("1602795891251.png")
if exists("1602797412183.png"):
    click(Pattern("1602797412183.png").targetOffset(-121,-9))
else:
    while not exists("1602797412183.png"):
        type(Key.PAGE_DOWN)
   

