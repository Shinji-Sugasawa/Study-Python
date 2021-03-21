class Counter:
    def __init__(self):
        self.value = 0
    def count_up(self):
        self.value += 1
        
class DoubleCounter(Counter):   #Counterクラスを継承
    """count_uoで２倍カウントするクラス"""
    def count_up(self):
        #   count_up()を２回呼ぶ
        super().count_up()  #Counterクラスのcount_up()を呼ぶ
        super().count_up()
        
"""
from dbl_counter import DoubleCounter
c = DoubleCounter()
print(c.value)

c.count_up()
print(c.value)
"""