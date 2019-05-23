import datetime
import math
import sys

MAX_DAY = 10000


def is_prime(n):
    '''ref to https://qiita.com/srtk86/items/874639e361917e5016d4'''
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def increment_day(dt):
    return dt + datetime.timedelta(days=1)


def find_full_prime_day():
    d = datetime.datetime.now()
    start_day = d.strftime('%Y/%m/%d')
    full_prime_day_cnt = 0

    for _ in range(MAX_DAY):
        n = d.strftime('%Y%m%d')
        while n != '':
            if not is_prime(int(n)):
                break

            n = n[1:]
        else:
            print(f'{d.strftime("%Y%m%d")} is full prime day!')
            full_prime_day_cnt += 1

        d = increment_day(d)

    end_day = d.strftime('%Y/%m/%d')
    full_prime_day_ratio = full_prime_day_cnt / MAX_DAY * 100

    print('-' * 30)
    print(f'From {start_day} to {end_day}')
    print(f'We find {full_prime_day_cnt} full prime days '
          f'which means {full_prime_day_ratio} %')


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        find_full_prime_day()
    elif len(args) == 2 and str.isdecimal(args[1]):
        MAX_DAY = int(args[1])
        find_full_prime_day()
    else:
        print('Usage: $ python find_full_prime_day.py [MAX_DAY=10000]')
