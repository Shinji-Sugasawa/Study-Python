import qrcode   #QRコード生成用のパッケージをインポートする
import qrcode.image.svg #QRコードをSVG画像で保存するモジュールをインポートする

class MakeQR:   #クラス定義
    def __init__(self): #コンストラクタを定義
        self.url = "http://www.nao.net.it-chiba.ac.jp"  #URLを直接定義する
        self.output = "python.svg"  #アウトプットファイル名を直接定義する
    
    def make(self): #makeメソッドの定義
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(self.url, image_factory = factory)
        img.save(self.output)

if __name__ == "__main__":  #モジュールが呼ばれたときにTrueとなる決まりの書き方
    app = MakeQR()  #MakeQRクラスをインスタンス化
    app.make()  #makeメソッドを呼び出し、QRコード画像が生成されて保存する