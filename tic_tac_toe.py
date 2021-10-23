from tkinter import *
from PIL import Image, ImageTk
from random import choice
from tkinter import messagebox

free_move = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

move_p = ''
move_b = ''

move = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

cord = [
		[[100, 100], [100, 200], [100, 300]],
		[[200, 100], [200, 200], [200, 300]],
		[[300, 100], [300, 200], [300, 300]],
											]

root = Tk()
root.title("Построение графиков без смс и регистрации")
canvas = Canvas(width=400, height=400)
answer = None

def imprec_comp(a, b):
	if b[0] in a and b[1] in a and b[2] in a:
		return True
	else:
		return False

def search_winner():
	global move_p, move_b, answer

	if imprec_comp(move_p, '123') or imprec_comp(move_p, '456') or imprec_comp(move_p, '789') or imprec_comp(move_p, '147') or imprec_comp(move_p, '258') or imprec_comp(move_p, '369') or imprec_comp(move_p, '159') or imprec_comp(move_p, '357'):
		answer = True
		messagebox.showinfo("","Вы выйграли.")
	if imprec_comp(move_b, '123') or imprec_comp(move_b, '456') or imprec_comp(move_b, '789') or imprec_comp(move_b, '147') or imprec_comp(move_b, '258') or imprec_comp(move_b, '369') or imprec_comp(move_b, '159') or imprec_comp(move_b, '357'):
		answer = True
		messagebox.showinfo("","Вы проиграли.")

	if answer:
		exit()


def move_bot():
	global free_move, move, cord, move_b
	try:
		a = choice(free_move)
		move_b += a

		free_move.pop(free_move.index(a))

		for i in range(len(move)):
			for j in range(len(move[i])):
				if str(move[i][j]) == a:
					canvas.create_oval(cord[i][j][1]-40, cord[i][j][0]-40, cord[i][j][1]+40, cord[i][j][0]+40, width=2, fill='red')
					break

	except Exception as e:
		messagebox.showinfo("","Ничья.")
		exit()

	search_winner()


def click(event):
	global free_move, move, cord, move_p

	x, y = event.x, event.y

	move_player = 0
	line_g = 0
	line_v = 0

	if x > 50 and y > 50 and x < 350 and y < 350:
		if x > 50 and x < 150:
			line_v = 0
		elif x > 150 and x < 250:
			line_v = 1
		elif x > 250 and x < 350:
			line_v = 2

		if y > 50 and y < 150:
			line_g = 0
		elif y > 150 and y < 250:
			line_g = 1
		elif y > 250 and y < 350:
			line_g = 2
		
		move_p += str(move[line_g][line_v])

		free_move.pop(free_move.index(str(move[line_g][line_v]))) 

		canvas.create_oval(cord[line_g][line_v][1]-40, cord[line_g][line_v][0]-40, cord[line_g][line_v][1]+40, cord[line_g][line_v][0]+40, width=2, fill='green')

		search_winner()

		move_bot()


for x in range(50, 400, 100):
	canvas.create_line(x, 50, x, 350, width=2)

for y in range(50, 400, 100):
	canvas.create_line(50, y, 350, y, width=2)

canvas.pack()


canvas.bind('<1>',click)
root.mainloop()