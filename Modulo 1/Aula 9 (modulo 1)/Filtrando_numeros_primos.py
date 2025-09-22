class Primo:
    def __init__(self):
        self.primos=[2,3,4,5,6,7,8,9,10]
        primo=[]
        for i in self.primos:
            e_primo=True
            for j in range(2,i):
                if i%j==0:
                    e_primo=False
                    break
            if e_primo:
                primo.append(i)
                
        print(primo)
a=Primo()