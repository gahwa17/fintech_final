import qrcode
from random import randint
import os 
#qr = qrcode.make('hello world')
#qr.save('myQR.png')

def QRcode():
    qr = qrcode.QRCode(version = 1,box_size = 14,border = 3)
    a = randint(10000000, 99999999)
    DIR = 'server/src/qrimg'  #要統計的資料夾
    num = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    data = str(a)
    text = str(num) #要抽換的字
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill = 'black', back_color = 'white')
    loc = ('server/src/qrimg/test{}.png'.format(text))
    img.save(loc)

def qrPath():
    DIR = 'server/src/qrimg'  #要統計的資料夾
    num = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])-1
    text = str(num) #要抽換的字
    loc = ('server/src/qrimg/test{}.png'.format(text))
    return loc
#QRcode()
print(qrPath())
