import votto12 as vt

colors = "1) blue\n2) red\n3) white\n4) green\n5) yellow\n6) cyan\n7) black\n8) magenta"
vt.PrintHor("Эта программа продемонстрирует большую часть возможностей движка Votto 1.2", 0.02)
input()

while True:
	vt.Update()
	print("\nВыберите действие:")
	print("1) Изменить цвет текста\n2) Изменить цвет фона\n3) Сделать цвет светлее\n4) Сделать цвет темнее\n5) Очистить командную строку\n6) Убрать все изменения\n7) Напечатать со скоростью")
	
	mov = input("Действие: ")
	
	if mov == "1":
		vt.PrintHor(colors, 0.02)
		text_color = input("\nВыберите цвет текста: ")
		
		if text_color == "1":
			vt.PrintColor("", "blue")
		
		elif text_color == "2":
			vt.PrintColor("", "red")
		
		elif text_color == "3":
			vt.PrintColor("", "white")
		
		elif text_color == "4":
			vt.PrintColor("", "green")
		
		elif text_color == "5":
			vt.PrintColor("", "yellow")
		
		elif text_color == "6":
			vt.PrintColor("", "cyan")
		
		elif text_color == "7":
			vt.PrintColor("", "black")
		
		elif text_color == "8":
			vt.PrintColor("", "magenta")
	
	elif mov == "2":
		vt.PrintHor(colors, 0.02)
		bg_color = input("\nВыберите цвет фона: ")
		
		if bg_color == "1":
			vt.PrintBg("", "blue")
		
		elif bg_color == "2":
			vt.PrintBg("", "red")
		
		elif bg_color == "3":
			vt.PrintBg("", "white")
			
		elif bg_color == "4":
			vt.PrintBg("", "green")
		
		elif bg_color == "5":
			vt.PrintBg("", "yellow")
		
		elif bg_color == "6":
			vt.PrintBg("", "cyan")
		
		elif bg_color == "7":
			vt.PrintBg("", "black")
		
		elif bg_color == "8":
			vt.PrintBg("", "magenta")
	
	elif mov == "3":
		vt.Bright()
	
	elif mov == "4":
		vt.Dim()
		
	elif mov == "5":
		vt.Update()
	
	elif mov == "6":
		vt.Reset()
	
	elif mov == "7":
		vt.PrintHor("1) Вертикально\n2) Горизонтально")
		how = input("\nКак хотите напечатать: ")
		
		if how == "2":
			txt = input("Текст: ")
			speed = float(input("Скорость: "))
			
			vt.Update()
			vt.PrintHor(txt, speed)
			
			input()
		
		elif how == "1":
			txt2 = input("Текст: ")
			speed2 = float(input("Скорость: "))
			
			vt.Update()
			vt.PrintVert(txt2, speed2)
			
			input()