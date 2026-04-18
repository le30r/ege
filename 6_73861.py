#Повтори 2 [Вперёд 20 Направо 90 Вперёд 9 Направо 90]
#Определите максимально возможное количество точек с целочисленными координатами, которые могут оказаться внутри пересечения фигур,
# нарисованных двумя Черепахами. Точки, находящиеся на линиях, не учитывать.

import turtle as t
t.speed(100)
k = 15
t.left(90)
t.down()
for i in range(2):
    t.forward(20 * k)
    t.right(90)
    t.forward(9 * k)
    t.right(90)


t.forward(11.5 * k)
t.right(90)
t.down()
for i in range(2):
    t.forward(20 * k)
    t.right(90)
    t.forward(9 * k)
    t.right(90)
t.up()
t.goto(0, 0)

for i in range(0, 10):
    for y in range(-10, 21):
        t.goto(i * k, y * k)
        t.dot()
t.mainloop()