import qrcode   #QRコード生成用のパッケージをインポートする
import qrcode.image.svg #QRコードをSVG画像で保存するモジュールをインポートする

class MakeQR:   #クラス定義
    def __init__(self): #コンストラクタを定義
        self.url = "http://www.nao.net.it-chiba.ac.jp"  #URLを直接定義する
        self.output = "python.svg"  #アウトプットファイル名を直接定義する
    