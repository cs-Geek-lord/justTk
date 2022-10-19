# UI

## Tkinter window

```python
from tkinter import *
window=Tk()
# add widgets here

window.title('Hello Python')
window.geometry("300x200+10+20")
window.mainloop()
```

## Buttons

> Button(window, attributes)

```python
from tkinter import *
window=Tk()
btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()
```
## Labels
Label(window, attributes)

```python
from tkinter import *
window=Tk()
lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()
```

## Entry

```python
from tkinter import *
window=Tk()
txtfld=Entry(window, text="This is Entry Widget", bg='black',fg='white', bd=5)
txtfld.place(x=10, y=20, width=100, height=30)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()
```

## Selection Widgets

### RadioButtons

```python
from tkinter import *
window=Tk()
r1=Radiobutton(window, text="male", variable=v0,value=1)
r2=Radiobutton(window, text="female", variable=v0,value=2)
r1.place(x=100,y=50)
r2.place(x=180, y=50)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()
```

### CheckButtons 

```python
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Cricket", variable = v1)
C2 = Checkbutton(window, text = "Tennis", variable = v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)
```

### Combobox

```python
var = StringVar()
var.set("one")
data=("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=60, y=150)
```

## Events

| Event       | Modifier    | Type          | Qualifier |       Action               |
| :---        |    :----:   |     :---:     |  :-----:  |         :----:             |
| Header      | Title       | Here's this   |           |  Left mouse button click.  |
| Paragraph   | Text        | And more      |           |  Middle mouse button click.|  
