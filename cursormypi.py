import curses 
import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keyboard(True)

try:
	while True:
		char = screen.getch()
		if char == ord('q'):
			break
		elif char == curses.KEY_UP
		    print ("up")
		    GPIO.output(7,False)
		    GPIO.output(11,True)
		    GPIO.output(13,False)
		    GPIO.output(15,True)
		    GPIO.output(16,False)
		    GPIO.output(18,True)
		    GPIO.output(29,False)
		    GPIO.output(31,True)
		elif char == curses.KEY_DOWN
		    GPIO.output(7,True)
		    GPIO.output(11,False)
		    GPIO.output(13,True)
		    GPIO.output(15,False)
		    GPIO.output(16,True)
		    GPIO.output(18,False)
		    GPIO.output(29,True)
		    GPIO.output(31,False)
		elif char == curses.KEY_RIGHT
		    GPIO.output(7,True)
		    GPIO.output(11,False)
		    GPIO.output(13,False)
		    GPIO.output(15,True)
		    GPIO.output(16,True)
		    GPIO.output(18,False)
		    GPIO.output(29,False)
		    GPIO.output(31,True) 
		elif char == curses.KEY_LEFT
		    GPIO.output(7,False)
		    GPIO.output(11,True)
		    GPIO.output(13,True)
		    GPIO.output(15,False)
		    GPIO.output(16,False)
		    GPIO.output(18,True)
		    GPIO.output(29,True)
		    GPIO.output(31,False) 
		elif char == 10
		    GPIO.output(7,False)
		    GPIO.output(11,False)
		    GPIO.output(13,False)
		    GPIO.output(15,False)
		    GPIO.output(16,False)
		    GPIO.output(18,False)
		    GPIO.output(29,False)
		    GPIO.output(31,False) 
finally 
   curses.nobreak(); screen.keyboard(0);curses.echo()
   curses.endwin()
