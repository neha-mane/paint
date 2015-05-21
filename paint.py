from Tkinter import *
import tkFileDialog
import tkSimpleDialog
import tkMessageBox
from PIL import Image, ImageTk
import ImageDraw
from tkColorChooser import askcolor 
class Shape:
	#This is a rectangle class which has the methods to create a rectangle
	#x1, y1 are the coordinates of the left top corner of the rectangle	
	#x2, y2 are the coordinates of the right bottom corner of the rectangle
	def __init__(self):
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
		self.id1 = 0
		self.id2 = 0
	def shapeCreate(self, event):
		#This creates a rectangle depending upon the coordiantes of the mouse dragged.
		self.x2 = event.x
		self.y2 = event.y #these are the coordinates on the canvas after releasing the mouse
		print "In rectCreate, Coordinates: ", self.x1, self.y1, self.x2, self.y2
		#Now lets just create our rectangle

	def shapeCreate2(self, event):
		print("shape create2 mouse began at ", self.x1, self.y1)
		w.bind('<ButtonRelease-1>', self.shapeCreate)

	def shapeCreate1(self, event):
		self.x1 = event.x
		self.y1 = event.y
		print "shape create1 mouse began at ", self.x1, self.y1
		
b = [1]
c = [0, 0]
class Move2:
	def __init__(self):
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
		self.select = 0
	def move1(self, event):
		self.x1 = event.x
		self.y1 = event.y
		w.unbind_all(event)
		self.select = w.find_withtag(CURRENT)
		print "newid" , self.select		

	def move2(self,event):
		if b[0] == 1:
			b[0] = 3
			x2, y2 = ( event.x), ( event.y)
			c[0] = x2
			c[1] = y2
			dx = x2 - self.x1
			dy = y2 - self.y1
			w.move(self.select, dx, dy)			
		
		if b[0] == 3:
			x2, y2 = ( event.x), ( event.y)
			x1 = c[0]
			y1 = c[1]
			dx = x2 - x1
			dy = y2 - y1
			w.move(self.select, dx, dy)
			c[0] = x2
			c[1] = y2			
		
		w.bind('<ButtonRelease-1>', self.move3)
	def move3(self,event):
		print "id", self.select
		self.x2 = event.x
		self.y2 = event.y
		dx = self.x2 - c[0]
		dy = self.y2 - c[1]
		if self.select:
			w.move(self.select, dx, dy)
		b[0] = 1
		c[0] = 0
		c[1] = 0
	

def moveSelect(event):
	m1 = Move2()
	w.bind('<Button-1>', m1.move1)
	w.bind('<B1-Motion>', m1.move2)

class Rectangle(Shape):
	
	def shapeCreate(self, event):
		self.x2 = event.x
		self.y2 = event.y
		w.delete(self.id2)
		w.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = "white")
	
	def shapeCreate2(self, event):
		x = event.x
		y = event.y
		w.delete(self.id1)		
		self.id2 = w.create_rectangle(self.x1, self.y1, x, y, fill = "white")
		self.id1 = self.id2
		w.bind('<ButtonRelease-1>', self.shapeCreate)	
		

class Oval(Shape):
		
	def shapeCreate(self, event):
		self.x2 = event.x
		self.y2 = event.y
		w.delete(self.id2)
		w.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "white")
	
	def shapeCreate2(self, event):
		x = event.x
		y = event.y
		w.delete(self.id1)		
		self.id2 = w.create_oval(self.x1, self.y1, x, y, fill = "white")
		self.id1 = self.id2
		w.bind('<ButtonRelease-1>', self.shapeCreate)	
	
	
class Line():
	def shapeCreate(self, event):
		self.x2 = event.x
		self.y2 = event.y		
		w.create_line( self.x1, self.y1, self.x2, self.y2 )
		x = w.find_withtag(ALL)
		y = list(x)
		z = y.pop()
		w.bind('<ButtonRelease-1>', self.endLine)
		
	def endLine(self, event):		
		w.unbind_all(event)
		
	def shapeCreate1(self, event):
		self.x1 = event.x
		self.y1 = event.y
		
	def shapeCreate2(self, event):
		w.bind('<ButtonRelease-1>', self.shapeCreate)

a = [1]
beg = [0, 0]
t = [0, 0]
class pencil(Shape):
	def shapeCreate(self, event):
		if a[0] == 3:
			x1, y1 = t[0], t[1]
			
		if a[0] == 1:
			x1, y1 = ( event.x - 1), ( event.y - 1)
			beg[0] = x1
			beg[1] = y1
			a[0] = 3
			x2, y2 = ( event.x), ( event.y)
			t[0] = x2
			t[1] = y2
		x2, y2 = ( event.x), ( event.y)
		t[0] = x2
		t[1] = y2
		w.create_line( x1, y1, x2, y2, fill = 'black' )
		w.bind('<ButtonRelease-1>', self.endPencil)
		
	def endPencil(self, event):
		w.unbind_all(event)
		a[0] = 1
		t = [0, 0]
			
class eraseLine(Line):
	def shapeCreate(self, event):
		if a[0] == 3:
			x1, y1 = t[0], t[1]
		if a[0] == 1:
			x1, y1 = ( event.x - 10), ( event.y - 10)
			a[0] = 3
			x2, y2 = (event.x), ( event.y)
			t[0] = x2
			t[1] = y2
		x2, y2 = ( event.x), ( event.y)
		t[0] = x2
		t[1] = y2
		w.create_line( x1, y1, x2, y2, fill = 'white', width = 10.0)
		w.bind('<ButtonRelease-1>', self.endLine)
	
	def endLine(self, event):
		w.unbind_all(event)
		
		a[0] = 1
		t = [0, 0]

def drawSelect(event):
		if(zoom_flag != 0):
			return
		flag = 1
		l1 = Line()
		w.bind('<Button-1>', l1.shapeCreate1)
		w.bind('<B1-Motion>', l1.shapeCreate2)

def pencilSelect(event):
		flag = 1
		w.bind('<Button-1>', endClear)
		flag = 2
		l2 = pencil()
		w.bind('<B1-Motion>', l2.shapeCreate)

		
def rectSelect(event):
	if(zoom_flag != 0):
		return 
	if(flag == 0):
	#Now here we want to create a rectangle on the canvas
	#Wherever the user first clicks, that should be the top most left corner of the rectangle
	#Then, the user should drag the mouse till the point he wants to drag
	#When, he leaves the mouse press, that should be the bottom right corner of the rectangle
		r1 = Rectangle()
		w.bind('<Button-1>', r1.shapeCreate1)
		w.bind('<B1-Motion>', r1.shapeCreate2)

def ovalSelect(event):
	if(zoom_flag != 0):
		return
	s1 = Oval()
	w.bind('<Button-1>', s1.shapeCreate1)
	w.bind('<B1-Motion>', s1.shapeCreate2)
	
def clearScreen():
	global zoom_flag
	x = tkMessageBox.askquestion(title = "New file", message = "Do you want to save your file?")
	print x
	if(x == "yes"):
		saveClick() #in this case we want to save the file
	w.delete("all")
	item = w.create_image(10, 10, anchor = NW)
	zoom_flag = 0
	w.unbind_all("<Button-1>")
	w.bind('<ButtonRelease-1>', endClear)
	w.bind('<B1-Motion>', endClear)
	master.title("untitled")

def endClear(event):
	w.unbind_all(event)

def erase(event):
	if(zoom_flag != 0):
		return
	el1 = eraseLine()
	w.bind('<Button-1>',endClear)
	w.bind('<ButtonRelease-1>',endClear)
	w.bind('<B1-Motion>', el1.shapeCreate)

def click(event):
	global p
	w.bind("<ButtonRelease-1>",endClear)
	w.bind("<B1-Motion>",endClear)
	id = w.find_withtag(CURRENT)
	w.itemconfig(CURRENT, fill=p[1])
	w.bind("<ButtonRelease-1>",endClear)
	w.bind("<B1-Motion>",endClear)

def clearClick(event):
	if(zoom_flag != 0):
		return
	global p
	p = [0,'#ffffff'] 
	p = askcolor() 
	w.bind('<Button-1>', click)

def delete(event):
	w.bind("<ButtonRelease-1>",endClear)
	w.bind("<B1-Motion>",endClear)
	id = w.find_withtag(CURRENT)
	w.delete(CURRENT)
	w.bind("<ButtonRelease-1>",endClear)
	w.bind("<B1-Motion>", endClear)
	

def delClick(event):
	if(zoom_flag != 0):
		return
	w.bind('<Button-1>', delete)

flag_undo = 0
def undoClick(event):
	global beg
	global t
	global flag_undo
	w.bind("<ButtonRelease-1>",endClear)
	w.bind("<B1-Motion>",endClear)
	history = list()
	linecoords = list()
	history = w.find_withtag(ALL)
	print history
	hist = list(history)
	n = len(hist)
	print n
	x = hist.pop()
	print w.type(x)
	if w.type(x) == 'line':
		linecoords = w.coords(x)
		print linecoords
		if (linecoords[2] == t[0] and linecoords[3] == t[1]) or flag_undo == 1:
			print "inside line if"				
			flag_undo = 1
			print "llkdjflsdkjfls\n"
			print "dfsjdlfksjdlk\n\n", beg[0], linecoords[0], beg[1], linecoords[1]
			if int(linecoords[0]) == int(beg[0]) and int(linecoords[1]) == int(beg[1]):
				print "OVER!\n"
				flag_undo = 0
				w.delete(x)
				return	
			w.delete(x)
			undoClick(event)
		if flag_undo == 0:
			w.delete(x)
	else:
		print "other shapes than line"
		w.delete(x)
	print hist
	history = tuple(hist)
	print history	
	print "end of undo"
	w.bind("<ButtonRelease-1>",endClear)
	w.bind("<B1-Motion>", endClear)
	


def getColori():
	global p
	p = [0,'#ffffff'] 
	p = askcolor() 

def saveClick():
	global zoom_flag
	file_name = tkFileDialog.asksaveasfilename(filetypes=myFormats , title="Save the image as...")
	w.update()
	w.postscript(file = file_name, colormode='color')
	master.title(file_name)
	zoom_flag = 0

def openClick():
	global image_open	
	global canvas_height
	global canvas_width
	global zoom_flag
	w.delete("all")
	item = w.create_image(0, 0, anchor = NW)
	file_open = tkFileDialog.askopenfilename(filetypes= myFormats, title ="Open existing file...")

	image_new = Image.open(file_open)
	image_new = image_new.resize((canvas_width, canvas_height), Image.ANTIALIAS)
	image_open = ImageTk.PhotoImage(image_new)

	w.itemconfigure(item, image = image_open)
	master.title(file_open)
	zoom_flag = 0


def clickQuit():
	result = tkMessageBox.askquestion(title = "New file", message = "Do you want to save your file before quitting?")	
	if result == "yes":
		saveClick()
	master.quit()

def zoom_in():
	global zoom_flag
	global zoom_size
	zoom_size = zoom_size * 2
	zoom_flag = zoom_flag + 1
	w.bind("<ButtonRelease-1>", endClear)
	w.bind('<Button-1>', endClear)
	w.bind("<B1-Motion>", endClear)
	w.scale(item, 0, 0, 2, 2)
	w.scale("all", 0, 0, 2, 2) 
	w.configure(scrollregion=(0,0,zoom_size, zoom_size))

def zoom_out():
	global zoom_flag
	global zoom_size
	zoom_size = zoom_size / 2
	zoom_flag = zoom_flag - 1
	print "in zoom out"
	w.bind('<Button-1>', endClear)
	w.bind("<B1-Motion>", endClear)
	w.bind("<ButtonRelease-1>", endClear)
	w.scale("all", 0, 0, 0.5, 0.5)
	w.configure(scrollregion=(0,0,zoom_size, zoom_size))

def image_form(event):
	w.bind('<ButtonRelease-1>', endClear)
	w.bind('<B1-Motion>',endClear)
	global i
	global image_open1	
	image_open1.append('')
	x1 = event.x
	y1 = event.y
	image_new = Image.open(file_open)
	image_new = image_new.resize((100, 100), Image.ANTIALIAS)
	image_open1[i] = ImageTk.PhotoImage(image_new)
	w.create_image(x1, y1, anchor = CENTER, image = image_open1[i])
	i = i + 1

def image_create(event, pathway):
	print "in image create"
	global file_open
	file_open= pathway
	w.bind('<ButtonRelease-1>', endClear)
	w.bind('<B1-Motion>',endClear)
	w.bind('<Button-1>', image_form)


class text():	
	def __init__(self):
		self.x1 = 0
		self.y1 = 0
		self.index1 = 0
		self.index2 = 0
		self.flagi = 0
	def text1(self, event):
		w.bind('<Button-1>', self.text)		
	def text(self,event):
		self.x1 = event.x
		self.y1 = event.y
        # text items with the tag "editable" will inherit these bindings
        	w.create_text(self.x1, self.y1, anchor="nw", tags=("editable",),
                                text="This text is editable", font = ("Times", 14, "normal", "roman"))
		w.bind('<B1-Motion>', endClear)
		w.bind('<ButtonRelease-1>', endClear)
		w.bind('<Button-1>', self.endClear)
		       
	def endClear(self, event):
		w.unbind_all(event)
		w.tag_bind("editable","<Double-Button-1>", self.set_focus)
        	w.tag_bind("editable","<Button-1>", self.set_cursor)
 		w.tag_bind("editable","<Key>", self.do_key)
        	w.tag_bind("editable","<Left>", self.do_left)
        	w.tag_bind("editable","<Right>", self.do_right)
       		w.tag_bind("editable","<BackSpace>", self.do_backspace)
		w.tag_bind("editable","<Delete>", self.do_delete)
        	w.tag_bind("editable","<Return>", self.do_return)

	def set_focus(self, event):
     
	       	if w.type("current") == "text":
            		w.focus_set() 
            		w.focus("current") 
            		w.select_from("current", 0)
            		w.select_to("current", "end")
			w.bind('<Double-ButtonRelease-1>', endClear)
	def set_cursor(self, event):
        	item = w.focus()
		w.select_clear()
        	if item:
            		self.x = w.canvasx(event.x)
            		self.y = w.canvasy(event.y)
            		w.icursor(item, "@%d,%d" % (self.x, self.y))
            		w.select_clear()
			self.index1 = w.index(item, "insert")
			w.bind('<B1-Motion>', self.Select)
	
	def Select(self, event):
		w.bind('<ButtonRelease-1>', self.Select1)
	
	def Select1(self, event):
		item = w.focus() 
		x = w.canvasx(event.x)
            	y = w.canvasy(event.y)
		if item:
			self.index2 = w.index(item, "@%d,%d" % (x, y))
			if w.type("current") == "text":
            			w.focus_set() 
            			w.focus("current") 
            			w.select_from("current", self.index1)
            			w.select_to("current", self.index2)
			
			
	def do_key(self, event):
	        item = w.focus()
        	if item and event.char >= " ":
            		insert = w.index(item, "insert")
            		selection = w.select_item()
            		if selection:
                		w.dchars(item, "sel.first", "sel.last")
                		w.select_clear()
            		w.insert(item, "insert", event.char)
	def do_left(self, event): 
        	item = w.focus()
        	if item:
            		new_index = w.index(item, "insert") - 1
            		w.icursor(item, new_index)

    	def do_right(self, event):
                item = w.focus()
        	if item:
            		new_index = w.index(item, "insert") + 1
            		w.icursor(item, new_index)
            		
	def do_return(self,event):
    	    	w.focus("")
        	w.delete("highlight")
       		w.select_clear()

	def do_delete(self, event):
		item = w.focus()
        	if item:
            		selection = w.select_item()
            		if selection:
                		w.dchars(item, "sel.first", "sel.last")
                		w.select_clear()
            		else:
                		insert = w.index(item, "insert")
                    		w.dchars(item, insert, insert)
	
    	def do_backspace(self, event):
        	item = w.focus()
        	if item:
            		selection = w.select_item()
            		if selection:
                		w.dchars(item, "sel.first", "sel.last")
                		w.select_clear()
            		else:
                		insert = w.index(item, "insert")
                		if insert > 0:
                    			w.dchars(item, insert-1, insert-1)

def bold():
	selection = w.select_item()
	if selection:
		value1 = w.itemconfigure(selection)
		value2 = value1["font"]
		value3 = value2[4]
		word = value3.split()
		if word[2] == "bold" :
			word[2] = "normal"
		else :
			word[2] = "bold"
		value1 = w.itemconfigure(selection, font = (word[0], word[1], word[2], word[3]))
				
				
	
def ital():
	selection = w.select_item()
	if selection:
		value1 = w.itemconfigure(selection)
		value2 = value1["font"]
		value3 = value2[4]
		word = value3.split()
		if word[3] == "italic" :
			word[3] = "roman"
		else :
			word[3] = "italic"
		value1 = w.itemconfigure(selection, font = (word[0], word[1], word[2], word[3]))				
			
def font(fonts):
	selection = w.select_item()
	if selection:
		value1 = w.itemconfigure(selection)
		value2 = value1["font"]
		value3 = value2[4]
		word = value3.split()
		value1 = w.itemconfigure(selection, font = (fonts, word[1], word[2], word[3]))
						
def size(sizes):
	selection = w.select_item()
	if selection:
		value1 = w.itemconfigure(selection)
		value2 = value1["font"]
		value3 = value2[4]
		word = value3.split()
		value1 = w.itemconfigure(selection, font = (word[0], sizes, word[2], word[3]))

	
master = Tk()
master.geometry("1500x750")
flag = 0
zoom_flag = 0;
master.title("Untitled")
canvas_width = 850
canvas_height = 650
canvas_color = "white"
w = Canvas(master,  width=canvas_width, height=canvas_height, bg = canvas_color)
w.pack(expand = NO, fill = NONE) 
p = [0, '#ffffff']


menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="New file", command = clearScreen) #This will be our clear
filemenu.add_separator()
filemenu.add_command(label="Open file", command = openClick) 
filemenu.add_separator()
filemenu.add_command(label="Save file", command = saveClick) #This will be linked to our save
filemenu.add_separator()
filemenu.add_command(label="Quit", command = clickQuit) #This closes the application 
menubar.add_cascade(label="File", menu=filemenu)

viewmenu = Menu(menubar, tearoff = 0)
viewmenu.add_separator()
viewmenu.add_command(label = "Zoom in", command = zoom_in)
viewmenu.add_command(label = "Zoom out", command = zoom_out)
menubar.add_cascade(label = "View", menu = viewmenu)

filemenu2 = Menu(menubar, tearoff=0)
filemenu2.add_separator()
filemenu2.add_command(label="Times", command = lambda : font("Times")) #This will be our clear
filemenu2.add_separator()
filemenu2.add_command(label="Helvetica", command = lambda : font("Helvetica")) 
filemenu2.add_separator()
filemenu2.add_command(label="Ariel", command = lambda : font("Ariel")) #This will be linked to our save
filemenu2.add_separator()
menubar.add_cascade(label="Font", menu=filemenu2)

filemenu1 = Menu(menubar, tearoff=0)
filemenu1.add_command(label="14", command = lambda: size(14)) #This will be our clear
filemenu1.add_separator()
filemenu1.add_command(label="16", command = lambda: size(16)) #This will be our clear
filemenu1.add_separator()
filemenu1.add_command(label="18", command = lambda: size(18)) #This will be our clear
filemenu1.add_separator()
filemenu1.add_command(label="20", command = lambda: size(20)) #This will be our clear
filemenu1.add_separator()
filemenu1.add_command(label="22", command = lambda: size(22)) #This will be our clear
filemenu1.add_separator()
filemenu1.add_command(label="24", command = lambda: size(24)) #This will be our clear
filemenu1.add_separator()
filemenu1.add_command(label="26", command = lambda: size(26)) #This will be our clear
filemenu1.add_separator()
filemenu1.add_command(label="28", command = lambda: size(28)) #This will be our clear
filemenu1.add_separator()
menubar.add_cascade(label="Font size", menu=filemenu1)

filemenu3 = Menu(menubar, tearoff=0)
filemenu3.add_separator()
filemenu3.add_command(label="Bold", command = bold) #This will be our clear
filemenu3.add_separator()
filemenu3.add_command(label="Italics", command = ital) #This will be our clear
filemenu3.add_separator()
menubar.add_cascade(label="Text", menu=filemenu3)

master.config(menu=menubar)
item = w.create_image(0, 0, anchor = NW)
file_open = ""
image_open1 = list()
zoom_size = canvas_width

i = 0
xsb = Scrollbar(orient="horizontal", command = w.xview)
xsb.pack(fill = X)
ysb = Scrollbar(orient="vertical", command = w.yview)
ysb.pack(fill = Y)
w.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)
w.configure(scrollregion=(0,0,1000,1000))
scale = 1
myFormats = [ ('Portable Network Graphics','*.gif'), ('png / JFIF','*.jpg'), ('CompuServer gif','*.gif')]

#Buttons
pensilimg = PhotoImage(file = "pensilicon2.png") 
pencil_butn = Button(master, text = "Pencil", fg = "black", height = 75, width = 75, bg = "white", image = pensilimg, compound = TOP)
pencil_butn.pack(expand = NO, fill = NONE , side = LEFT )
pencil_butn.bind('<Button-1>', pencilSelect)
pencil_butn.place(relx = 0, x=2, y = 2, anchor=NW, bordermode="outside")

eraseimg = PhotoImage(file = "erasericon1.png")
erase_butn = Button(master, text = "Erase", fg = "black", height = 75, width = 75, bg = "white", image = eraseimg, compound = TOP)
erase_butn.pack(expand = NO, fill = NONE , side = LEFT )
erase_butn.bind('<Button-1>', erase)
erase_butn.place(in_= pencil_butn, x=100, anchor=NW, bordermode="outside")

rectimg = PhotoImage(file = "Rectangle-icon1.png")
rect_butn = Button(master, text = "Draw rectangle", bg = "white", height = 75, width = 75, fg = "black", image = rectimg, compound = TOP)
rect_butn.pack(expand = NO, fill = NONE, side = LEFT)
rect_butn.bind('<Button-1>', rectSelect)
rect_butn.place(relx = 0, x = 2, y = 100, anchor = NW)

ovalimg = PhotoImage(file = "oval.png")
oval_butn = Button(master, text = "Draw oval", bg = "white", height = 75, width = 75, fg = "black", image = ovalimg, compound = TOP)
oval_butn.pack(expand = NO, fill = NONE, side = LEFT)
oval_butn.bind('<Button-1>', ovalSelect)
oval_butn.place(in_= rect_butn, x=100, anchor=NW, bordermode="outside")

lineimg = PhotoImage(file = "lineicon.png")
line_butn = Button(master, text = "Draw line", fg = "black", height = 75, width = 75, bg = "white", image = lineimg, compound = TOP)
line_butn.pack(expand = NO, fill = NONE , side = LEFT)
#line_butn.place(in_=oval_butn, x=2, anchor=NE, bordermode="outside")
line_butn.bind(	'<Button-1>', drawSelect)
line_butn.place(relx = 0, x=2, y = 200, anchor=NW, bordermode="outside")

undoimg=PhotoImage(file="undoicon1.png")
undo_butn = Button(master, text = "Undo", fg = "black", height = 75, width = 75, bg = "white", image = undoimg, compound = TOP)
undo_butn.pack(expand = NO, fill = NONE, side = LEFT)
undo_butn.bind('<Button-1>', undoClick)
undo_butn.place(in_=line_butn, x = 100, anchor = NW)

deleteimg = PhotoImage(file = "deleteicon2.png")
delete_butn = Button(master, text = "Delete selected", fg = "black", height = 75, width = 75, bg = "white", image = deleteimg, compound = TOP)
delete_butn.pack(expand = NO, fill = NONE, side = LEFT)
delete_butn.bind('<Button-1>', delClick)
delete_butn.place(relx = 0, x = 2, y = 300, anchor=NW, bordermode="outside")

changeimg = PhotoImage(file = "colorpaletteicon1.png")
change_butn = Button(master, text = "Fill Color", fg = "black", height = 75, width = 75, bg = "white", image = changeimg, compound = TOP)
change_butn.pack(expand = NO, fill = NONE, side = LEFT)
change_butn.bind('<Button-1>', clearClick)
change_butn.place(in_= delete_butn, x=100, anchor=NW, bordermode="outside")

textimg = PhotoImage(file = "a.png")
text_butn = Button(master, text = "text", fg = "black", height = 75, width = 75, bg = "white", compound = TOP, image = textimg)
text_butn.pack(expand = NO, fill = NONE , side = LEFT )
text_butn.place(relx = 0, x =2, y = 400, anchor = NW)
t1 = text()
text_butn.bind('<Button-1>', t1.text1)

movimg = PhotoImage(file = "move.png")
mov_butn = Button(master, text = "move", fg = "black", height = 75, width = 75, bg = "white", compound = TOP,image = movimg)
mov_butn.pack(expand = NO, fill = NONE, side = LEFT)
mov_butn.bind('<Button-1>', moveSelect)
mov_butn.place(in_= text_butn, x=100, anchor = NW, bordermode="outside")


#right-side buttons
houseimg = PhotoImage(file = "house1.png")
image1_butn = Button(master, fg = "black", height = 75, width = 75, bg = "white", image = houseimg)
image1_butn.pack(expand = NO, fill = NONE, side = TOP)
image1_butn.bind('<Button-1>', lambda event : image_create(event, "house.png"))
image1_butn.place(relx = 1, x=-40, y = 2, anchor=NE, bordermode="inside")

catimg = PhotoImage(file = "cat1.png")
image2_butn = Button(master, fg = "black", height = 75, width = 75, bg = "white", image = catimg)
image2_butn.pack(expand = NO, fill = NONE, side = LEFT)
image2_butn.bind('<Button-1>', lambda event: image_create(event,"cat.png"))
image2_butn.place(relx = 1, x=-40, y = 80, anchor=NE, bordermode="inside")

tinkerimg = PhotoImage(file = "tinker1.png")
image3_butn = Button(master, fg = "black", height = 75, width = 75, bg = "white", image = tinkerimg)
image3_butn.pack(expand = NO, fill = NONE, side = LEFT)
image3_butn.bind('<Button-1>', lambda event: image_create(event,"tinker.png"))
image3_butn.place(relx = 1, x=-40, y = 160,  anchor=NE, bordermode="inside")

snakeimg = PhotoImage(file = "snake1.png")
image4_butn = Button(master, fg = "black", height = 75, width = 75, bg = "white", image = snakeimg)
image4_butn.pack(expand = NO, fill = NONE, side = LEFT)
image4_butn.bind('<Button-1>', lambda event: image_create(event, "snake.png"))
image4_butn.place(relx = 1, x=-40, y = 240, anchor=NE, bordermode="inside")


tigerimg = PhotoImage(file = "tiger1.png")
image5_butn = Button(master, fg = "black", height = 75, width = 75, bg = "white", image = tigerimg)
image5_butn.pack(expand = NO, fill = NONE, side = LEFT)
image5_butn.bind('<Button-1>', lambda event: image_create(event,"tiger.png"))
image5_butn.place(relx = 1, x=-40, y = 320, anchor=NE, bordermode="inside")

lionimg = PhotoImage(file = "lion1.png")
image6_butn = Button(master, fg = "black", height = 75, width = 75, bg = "white", image = lionimg)
image6_butn.pack(expand = NO, fill = NONE, side = LEFT)
image6_butn.bind('<Button-1>',lambda event: image_create(event,"lion.png"))
image6_butn.place(relx = 1, x=-40, y = 400, anchor=NE, bordermode = "inside")

burgerimg = PhotoImage(file = "burger1.png")
image7_butn = Button(master, fg = "black", height = 75, width = 75, bg = "white", image = burgerimg)
image7_butn.pack(expand = NO, fill = NONE, side = LEFT)
image7_butn.bind('<Button-1>', lambda event:image_create(event,"burger.png"))
image7_butn.place(relx = 1, x=-40, y = 480, anchor=NE, bordermode="inside")

sunimg = PhotoImage(file = "sun1.png")
image8_butn = Button(master,fg = "black", height = 75, width = 75, bg = "white", image = sunimg)
image8_butn.pack(expand = NO, fill = NONE, side = LEFT)
image8_butn.bind('<Button-1>',lambda event: image_create(event,"sun.png"))
image8_butn.place(relx = 1, x=-40, y = 560, anchor=NE, bordermode="inside")


mainloop()
