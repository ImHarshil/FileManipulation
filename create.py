import win32com.client
import pythoncom
import os

# pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
desktop = r'C:\Users\Nikhil\Desktop' # path to where you want to put the .lnk
path = os.path.join(desktop, 'NameOfShortcut.lnk')
target = r'C:\Users\Nikhil\PycharmProjects\FileManipulation\dist\Test\Test.exe'
#icon = r'C:\path\to\icon\resource.ico' # not needed, but nice

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
#shortcut.IconLocation = icon
shortcut.WindowStyle = 7 # 7 - Minimized, 3 - Maximized, 1 - Normal
shortcut.save()
