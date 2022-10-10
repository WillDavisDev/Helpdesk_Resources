import webbrowser
from tkinter import *
master = Tk()
master.geometry("300x130")
master['background'] = '#0C2608'
master.wm_title("Helpdesk Resources")
def ServiceNow():
    webbrowser.open('https://auburn.service-now.com/now/workspace/agent/home')

def PeopleFinder():
    webbrowser.open('http://peoplefinder.auburn.edu/peoplefinder/')

def AcesDirectory():
    webbrowser.open('https://ssl.acesag.auburn.edu/directory-new/')

def ISPList():
    webbrowser.open('https://sites.aces.edu/group/it/ForITstaff/Lists/Office_Network_ACESDB/AllItems.aspx?InplviewHashb288e353-b7f3-41e9-94f9-579a22a39d46=FilterField1%3DPhone%255Fx0020%255FProvider-FilterValue1%3DISP')
    
def Kronos():
    webbrowser.open('https://autime.auburn.edu/wfc/htmlnavigator/logon')

def nagios():
    webbrowser.open('https://nag.acesag.auburn.edu/nagios/')

def NamingConvention():
    webbrowser.open('https://sites.aces.edu/group/it/ForITstaff/wiki/Wiki%20Pages/Naming%20Convention%20for%20ACES-Ag%20Computers.aspx')

def ITHandbook():
    webbrowser.open('https://tigermailauburn-my.sharepoint.com/personal/snydess_auburn_edu/_layouts/15/Doc.aspx?sourcedoc={4c4f411e-a502-49b7-903b-1c46d1a77cc5}&action=edit&wd=target%28General%20Reference.one%7Cd62f4af1-32c6-44f4-beec-a1a2ac0b19e6%2FLogins%7C26bbd88e-aec5-428e-8135-d2cad1e9fab1%2F%29&wdorigin=NavigationUrl')

button0 = Button(master, text = ' Auburn People Finder ', fg = 'DarkSeaGreen2', bg = '#503611', command = PeopleFinder)
button0.grid(row = 0, column = 2, padx = 10, pady = 3)

button1 = Button(master, text = '      ACES Directory      ', fg = 'DarkSeaGreen2', bg = 'dark slate gray', command = AcesDirectory)
button1.grid(row = 1, column = 2, padx = 10, pady = 3)

button2 = Button(master, text = '         Service Now        ', fg = 'DarkSeaGreen2', bg = 'black', command = ServiceNow)
button2.grid(row = 2, column = 2, padx = 10, pady = 3)

button7 = Button(master, text = '  ACES-Ag Handbook  ', fg = 'DarkSeaGreen2', bg = 'grey22', command = ITHandbook)
button7.grid(row = 3, column = 2, padx = 10, pady = 3)

button3 = Button(master, text = '             ISP List             ', fg = 'DarkSeaGreen2', bg = 'grey2', command = ISPList)
button3.grid(row = 0, column = 3, padx = 10, pady = 3)

button4 = Button(master, text = '             Kronos             ', fg = 'DarkSeaGreen2', bg = 'grey34', command = Kronos)
button4.grid(row = 1, column = 3, padx = 10, pady = 3)

button5 = Button(master, text = '             Nagios             ', fg = 'DarkSeaGreen2', bg = 'grey42', command = nagios)
button5.grid(row = 2, column = 3, padx = 10, pady = 3)

button6 = Button(master, text = ' Naming Conventions ', fg = 'DarkSeaGreen2', bg = 'LemonChiffon4', command = NamingConvention)
button6.grid(row = 3, column = 3, padx = 10, pady = 3)

#button0.pack()
#button1.pack()
#button2.pack()
#button3.pack()
#button5.pack()
#button6.pack()
#button4.pack()
mainloop()