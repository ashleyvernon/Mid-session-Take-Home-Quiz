
'''#1'''

def draw_square(i):
	star = "*"
	for i in range(0,4):
		i = (star + " ")*4
		print i
	

draw_square(4)

'''#2'''

def draw_checkerboard():
	for i in range(0,8):
		i = "x" + " " + "o "
		print i*4


draw_checkerboard()