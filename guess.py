#讓使用者重複輸入數字去猜
import random #輸入別 人寫好的功能

r = random. randint(1, 100) #random + integer (隨機整數)
count = 0
while True:
	count += 1 #count = count + 1 
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print ('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')




