class Myclass:
    a = 5

    def say_hello(self):
        return "Hello world"

my_class = Myclass()
print(my_class.a)
print(Myclass.a)
print(my_class.say_hello())

v = 1
class A:
    v = 2

a = A()
a.v = 3
print(v)