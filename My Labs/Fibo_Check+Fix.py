from time import sleep
fibo=[1,2,3,8]

for i in range(2,len(fibo)):
    if(fibo[i])!=(fibo[i-1])+(fibo[i-2]):
        if(fibo[i])>(fibo[i-1])+(fibo[i-2]):
            x = (fibo[i-1])+(fibo[i-2])
            y = (fibo[i])
            fibo[i] = x
            print(fibo[i])
            print(fibo[i-1])
            print(fibo[i-2])
            sleep(2)
            print("\n")
            print("Change Fibo List Successfully\nNow It's a Fibo List!")
    else:
        print("It's is a Fibo List")