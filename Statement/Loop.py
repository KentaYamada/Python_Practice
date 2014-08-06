# -*-coding: utf-8 -*-

#Loop処理の確認
#この例はCやjavaでいうfor(int i=0; i < 10; i++)と同等
def ForLoop():
    for i in range(10):
        print(i)

def WhileLoop():
    i = 0;
    while i <=100:
        print(i)
        i += 1
 
if __name__ == "__main__":
    ForLoop()
    
    WhileLoop()
