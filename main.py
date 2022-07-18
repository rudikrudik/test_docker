import time
import random


def log():
    while True:
        random_data = random.randint(100, 20000)
        time_get = format_time = time.strftime("%Y-%m-%d %H:%M:%S")
        file = open('log.txt', 'a')
        file.write(f'{time_get} {random_data}\n')
        file.close()
        time.sleep(60)


if __name__ == '__main__':
    log()

