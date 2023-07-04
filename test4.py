from turtle import*
speed('slowest')
pencolor('red')
pensize(3)
bgcolor('black')

for i in range(5):
    fd(100)
    rt(360/5)
    for i in range(5):
        fd(50)
        rt(360/5)
for i in range(5):
    fd(100)
    lt(360/5)
    for i in range(5):
        fd(50)
        lt(360/5)

hideturtle()
mainloop()