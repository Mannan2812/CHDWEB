import qrcode
import random
import math
def genTicket():
    val = math.ceil(random.random()*1000000000000000+1)
    qr = qrcode.make(val)
    qr.save('myqr.jpg')
