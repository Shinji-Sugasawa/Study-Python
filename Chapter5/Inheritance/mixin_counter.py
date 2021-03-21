class Counter:  #self.valueをカウントする機能を持つクラス
    def __init__(self):
        self.value = 0
    def count_up(self):
        self.value += 1
        
class DisplayValue: #self.valueをprintするメソッドを持つクラス
    def display(self):
        print(f"value is {self.value}")
        
class DisplayCounter(Counter, DisplayValue):  
    #CounterとDisplayCounterクラスを多重継承
    pass    #特にメソッドの追加はしないのでpass 
    
"""
from mixin_counter import DisplayCounter
c = DisplayCounter()
c.count_up()    #Counterクラスのcount_up()メソッド
c.display() #DisplayValueクラスのdisplay()メソッド
"""