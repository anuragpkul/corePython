def main():
    x ,y = 100,100
    
    if(x < y):
        result = "x is less than y"
    elif (x == y):
        result = "x is equal to y"
    
    result = "x is less than y" if(x<y) else "x is greater than y"
    

   
    print(result)

if __name__ == "__main__":
    main()