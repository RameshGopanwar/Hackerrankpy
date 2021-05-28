if __name__ == '__main__':
    def consecutive(x):
        string = ""
        for i in range(1,x+1):
            string = string+str(i)
        return string 
    
    
    n = int(input()) 
    #string = ""
    print(consecutive(n))
    
    
    
