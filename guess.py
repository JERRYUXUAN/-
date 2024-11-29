from random import randint

print("来一起猜数字吧！")
a=randint(1,100)
shu=float(input("随机输入一个一到一百的数："))
while shu!=a:
  if  shu>a:
    print("小笨蛋猜大啦！")
    shu = float(input("随机输入一个一到一百的数："))
  else:
    print("大笨蛋猜小啦！")
    shu = float(input("随机输入一个一到一百的数："))
if  shu==a:
    print("猜对啦!")
   