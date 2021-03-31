import qrcode   #QRコード生成用のパッケージをインポートする
import qrcode.image.svg #QRコードをSVG画像で保存するモジュールをインポートする

class MakeQR:   #クラス定義
    def __init__(self, output): #コンストラクタの引数にoutputを設定
        self.url = ""  #URLの初期値を空にする
        self.output = output  #アウトプットファイル名を直接定義する
    
    def make(self): #makeメソッドの定義
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(self.url, image_factory = factory)
        img.save(self.output)

    def run(self):
        url = input("ここにURLを入力してください:") #コンソールから入力値を受け入れられるように定義
        self.url = url  #入力されたURLをインスタンス属性にする
        self.make() #makeメソッドを実行してQRコード生成と保存

if __name__ == "__main__":  #モジュールが呼ばれたときにTrueとなる決まりの書き方
    import sys  #sysライブラリをインポート
    args = sys.argv #コマンドライン引数を取得する
    output = args[1]    #コマンドライン引数から1つ目の引数をoutput変数に入れる
    app = MakeQR(output)  #MakeQRクラスをインスタンス化する際に、outputを指定する
    app.run()  #runメソッドを実行