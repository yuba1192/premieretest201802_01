import qrcode
# QRコードを生成
img1 = qrcode.make("http://www.giants.jp/top.html")
img2 = qrcode.make("https://www.amazon.co.jp/dp/B01BHPEC9G")
img3 = qrcode.make("http://www.cosme.net/product/product_id/10023860/top")
# QRコードを保存
img1.save("giants.png")
img2.save("amazon.png")
img3.save("cosme.png")