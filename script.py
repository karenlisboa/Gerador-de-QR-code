import qrcode

data = ['javascript', 'python', 'ruby', 'go', 'c++']

file_name = "my_qrcode.png"

img = qrcode.make(data=data)

img.save(file_name)