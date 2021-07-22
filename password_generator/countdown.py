import time

a = 10
while True:
    a -= 1
    print("TTL: ", a)
    time.sleep(1)
    if a == 0:
        print('We\'re done')
        break

# Nothing to do with this
