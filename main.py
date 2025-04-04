import qrcode as qr
 img = qr.make('https://web.whatsapp.com/')
 img.save('whatsapp_qr.png')

