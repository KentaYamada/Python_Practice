# -*- coding: utf-8 -*-

import time

def main():
    i = 0
    while i <= 10000:
        print (i)
        i += 1

if __name__ == "__main__":
    
    #簡単に処理時間を計測してみる
    start = time.time()
    
    main()

    elapsedTime = time.time() - start

    print("処理速度:{0}".format(elapsedTime))
