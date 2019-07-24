import turtle

# 터틀 객체 세 마리
ggobugi = turtle.Turtle()
unibugi = turtle.Turtle()
turtle_king = turtle.Turtle()

ggobugi.setx(-200)
unibugi.setx(200)
turtle_king.setx(0)

ggobugi.speed(5)
ggobugi.shape('turtle')
ggobugi.color('blue')

unibugi.speed(5)
unibugi.shape('turtle')
unibugi.color('green')

turtle_king.speed(5)
turtle_king.shape('turtle')
turtle_king.color('red')

#make_square 함수의 터틀 인자로 받으면 돌 수 있게끔
# def make_square(turtle):
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)

# 이렇게 쓰니까 동시에 돌아가지 않음
# for i in range(200):
#     make_square(ggobugi)
#     ggobugi.right(5)
    
#     make_square(unibugi)
#     unibugi.right(5)

#     make_square(turtle_king)
#     turtle_king.right(5)

def make_star(turtle):
    for i in range(20):
        turtle.forward(i * 10)
        turtle.right(144)



make_star(ggobugi)




    