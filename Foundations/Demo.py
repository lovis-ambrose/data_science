class Father:
    def play(self):
        print("I like playing with my kids")

class Mother(Father):
    def cook(self):
        print("I always cook for my kids")

class child(Mother):
    def run(self):
        print("I like to play")

c = child()
c.play()
c.cook()
c.run()