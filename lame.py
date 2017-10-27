#! /usr/bin/python
import time
import signal
import sys
from subprocess import call
def handler(signal, frame):
	print('That\'s very naughty of you')
	
signal.signal(signal.SIGINT, handler)
time.sleep(5)
cmd = ["say","-v","daniel", "Side note: This is what automatically happens when you create a function or class definition, i.e. the times when you really need a new line, so there's never a really good use for that, or at least none that I know of. In other words, Python is smart enough to be aware that you need continuation lines when you are entering a new function definition or other similar constructs (e.g. if:). In these automatic cases, do note that you need to enter an empty line using \ to tell Python that you are done."]
while True:
	call(cmd)
