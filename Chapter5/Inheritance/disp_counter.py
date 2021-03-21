class Counter:  #objectを継承する場合は、(object)は省略できる
    """親クラス"""
    
    def __init__(self):
        self.value = 0
    def count_up(self):
        self.value += 1
        
class DisplayCounter(Counter):  #Counterクラスを継承
    """子クラス"""
    def display(self):
        print(f"value = {self.value} ")
        
from disp_counter import DisplayCounter

c1 = DisplayCounter()   #親クラスのCounterの__init__()メソッドが呼ばれる
c1.count_up()   #親クラスのCounterのcount_up()メソッド
c1.display() #DisplayCOunterクラスのdisplay()メソッド
