from ctypes import windll
import time

def start_winforeground_daemon():
	import threading
	t=threading.Thread(target=window_foreground_loop)
	t.daemon=True
	t.start()

def window_foreground_loop(timeout=20):
	""" set the windows python console to the foreground (for example when you are working with a fullscreen program) """
	hwnd = windll.kernel32.GetConsoleWindow()
	HWND_TOPMOST 	= -1 
	SWP_NOMOVE 		= 2
	SWP_NOSIZE 		= 1
	while True:
		windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0,0,0,0, SWP_NOMOVE | SWP_NOSIZE)
		time.sleep(timeout)
	