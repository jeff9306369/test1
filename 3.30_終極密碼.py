"""
#### 第5題 ####
猜數字 0~100
透過input 的方法輸入一個數字 A
然後透過迴圈的
輸入input 數字Ｂ
並且顯示 數字Ａ 再B 之間的區段
例如 A=80
當Ｂ輸入50
則顯示 “ A在 50 和 100 之間
繼續輸入B 為 90
則顯示 “ A在 50 和 90 之間
繼續輸入B 為 70
則顯示 “ A在 70 和 90 之間
繼續輸入B 為 80
則顯示 “ 答對了A為80“

"""
while True:
    try:
        num3 = int(input("input a number in 1 ~ 100 : "))
        break
    except:
        print("error")
        continue

down = 1
top = 100
userNum = 0
while userNum != num3:
    print("guess a number in", down, "~", top, ": ", end="")
    try:
        userNum = int(input())
    except:
        print("error")
        continue

    if userNum >= top or userNum <= down:
        print("error")
    else:
        if userNum > num3:
            top = userNum
        else:
            down = userNum

print("Congratulations!")

