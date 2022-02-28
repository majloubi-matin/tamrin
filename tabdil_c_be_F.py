try:
    celsius = int(input('Enter the temperature '))
    
    if celsius < -273:
        raise ValueError('adad koochek tar az -273')
except ValueError as e:
    print(e)
else:
    farenhait = celsius * 9.5 + 32
    print("temperature = ", farenhait)
    