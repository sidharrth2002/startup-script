import webbrowser
from gcalAPI import connect

def openTabs():
    webbrowser.open_new('https://mmls.mmu.edu.my')
    webbrowser.open('https://calendar.google.com/u/1')
    webbrowser.open('https://classroom.google.com/u/1/h')
    webbrowser.open('https://mail.google.com/mail/u/1/')

if __name__ == '__main__':
    openTabs()
    connect()