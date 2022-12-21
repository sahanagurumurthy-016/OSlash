from sys import argv

def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    Price = 0.00
    discount = 0.00
    Total_price = 0.00
    F = 0
    for line in lines:
        l = line.split(' ')
        if(l[0] == 'ADD_ITEM'):
            n = int(l[2])
            if( l[1] == 'TSHIRT' or l[1] == 'JACKET' or l[1] == 'CAP'):
                if(n <= 2):
                    if(l[1] == 'TSHIRT'):
                        pp = 1000
                        d = 0.1
                    if(l[1] == 'JACKET'):
                        pp = 2000
                        d = 0.05
                    if(l[1] == 'CAP'):
                        pp = 500
                        d = 0.2
                    discount = discount + n*pp*d
                    Total_price = Total_price + n*pp
                    Price = Price + (n*pp - n*pp*d)
                    print("ITEM_ADDED")
                else:
                    print("ERROR_QUANTITY_EXCEEDED")  
            elif(l[1] == 'NOTEBOOK' or l[1] == 'PENS' or l[1] == 'MARKERS'):
                if( n <= 3):
                    if(l[1] == 'NOTEBOOK'):
                        pp = 200
                        d = 0.2
                    if(l[1] == 'PENS'):
                        pp = 300
                        d = 0.1
                    if(l[1] == 'MARKERS'):
                        pp = 500
                        d = 0.05
                    discount = discount + n*pp*d
                    Total_price = Total_price + n*pp
                    Price = Price + (n*pp - n*pp*d)
                    print("ITEM_ADDED")
                else :
                    print("ERROR_QUANTITY_EXCEEDED")
        else:
            if(Total_price < 1000) :
                discount = 0.0
                Price = Total_price + Total_price * 0.1 
            elif(Price >= 3000):
                discount = discount + Price * 0.05
                Price = Price - Price * 0.05 
                Price = Price + Price * 0.1
            else :
                discount = discount 
                Price = Price + Price * 0.1
            print("TOTAL_DISCOUNT " , discount)
            print("TOTAL_AMOUNT_TO_PAY ",Price)
if __name__ == "__main__":
    main()