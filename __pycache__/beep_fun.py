import winsound
for freq in range (50,1000,50):
    print('freq :',freq)
    winsound.Beep(freq,500)
