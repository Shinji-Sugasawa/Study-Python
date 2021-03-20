class Counter:
    def __init__(self, initial = 0):#コンストラクタ(スペシャルメソッド)
        self.value = initial    #initial引数をvalueの初期値として使う
    
    def count_up(self):#通常のメソッド
        self.value +=1
        
    def __str__(self):#文字列表現を返すメソッド
        return f"Counter({self.value})"
    
    def __add__(self,other):# +演算子と呼ばれるスペシャルメソッド
        return Counter(self.value + other.value)#Counterを新たに生成して返す
    
    
    #"""
    c1 = Counter(10)    #コンストラクタ(__init__メソッド)がよばれている
    c1.count_up()#count_upメソッドを呼び出している
    str(c1)#文字列表現(__str__メソッド)が呼び出されている
    #'Counter(11)'が出力
    c2 = Counter(1)
    c3 = c1 + c2 #通常の+演算子で計算
    str(c3)#'Counter(12)'が出力
    
    c4 = c1.__add__(c2)#c1 + c2と同じ意味
    #"""