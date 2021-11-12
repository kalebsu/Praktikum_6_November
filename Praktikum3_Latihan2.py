import time
def main():
    # siapkan list untuk menampung input dari user
    n = []
 
    # counter
    count = '1'
 
    # logika
    while count == '1':
        print('Data List Sekarang: ', n)
 
        bilangan = int(input('Masukan bilangan (0 untuk berakhir): '))
        n.append(bilangan)
     
        if bilangan == 0:
            
            
            print("Bilangan terbesar adalah:" ,max(n))
            time.sleep(1.5)
            
            break
        
 
if __name__=='__main__':
    main()
