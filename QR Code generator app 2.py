import PySimpleGUI as sg
import qrcode
import os

layout = [ [sg.Input(size=(25,1),key='LINK')],[sg.Button('Generate QR Code')],
    [sg.Image(size=(300,300),key= 'IMAGE')]
          ]

window = sg.Window('QR Code Generator App',layout)
  
def generate_qr_code(link):
    qr=qrcode.QRCode(version=1,box_size=10,border=5,)
    qr.add_data(link)
    qr.make(fit=True)
    img= qr.make_image(fill="black",back_color="red") 
    file_name= "qr_code" + ".png"
    path= os.path.join(os.getcwd(),file_name)
    img.save(path)
    return path

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Generate QR Code':
        link = values['LINK']
        qrcode_image_path=generate_qr_code(link)
        window['IMAGE'].update(filename=qrcode_image_path)

window.close()        