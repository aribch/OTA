from time import sleep

def loop():
    num = 0;
    while num < 3:
        print('working on A')
        num = num + 1
        sleep(1)


print('NEW 4 version booting from A...')
loop()
