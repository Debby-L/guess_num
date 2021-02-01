#讓使用者重複輸入數字去猜
import random #輸入別 人寫好的功能

r = random. randint(1, 100) #random + integer (隨機整數)
while True:
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print ('終於猜對了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')




