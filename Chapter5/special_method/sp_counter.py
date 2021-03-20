class Counter:
    def __init__(self, initial = 0):#コンストラクタ(スペシャルメソッド)
        self.value = initial    #initial引数をvalueの初期値として使う
    
    def count_up(self):#通常のメソッド
        self.value +=1
        
    def __str__(self):#文字列表現を返すメソッド
        return f"Counter({self.value})"
    
    def __add__(self,other):# +演算子と呼ばれるスペシャルメソッド
        return Counter(self.value + other.value)#Counterを新たに生成して返す