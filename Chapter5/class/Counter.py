class Counter:
    def __init__(self):
        self.value = 0
    def count_up(self):
        self.value +=1
        
c = Counter()
print(c.value)

c.count_up()
print(c.value)