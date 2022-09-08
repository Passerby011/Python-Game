
'''
ken = int(input("จำนวนไก่ย่าง:"))
ps = int(input("จำนวนส้มตำ:"))
sr = int(input("จำนวนข้าวเหนียว:"))
result = ไก่ย่าง*100+ps*30+sr*10
print("ราคารวมทั้งหมด",result,"บาท")



salary = int (input("input salary:"))
result = ((salary - (salary*12/100)-10000- 3000- 1250) /5)
print("เงินเหลือ:",result)


degree = int(input("โปรดป้อนอุณหภูมิ:"))
if degree > 28 :
    print("อากาศร้อนมากเลย วันนี้")
else:
    print("เย็นพอตัว แต่ฝนตก")

number = int(input("ป้อนตัวเลข:"))
if number%2 == 0:
    print("เป็นเลขคู่")
else:
    print("เป็นเลขคี่")

num = int(input("ป้อนยอดรวมสินค้า:"))
if num < 1000:
    print(num,"ไม่มีส่วนลด")
elif num > 1000 and num < 4999:
    result = num - num/100*5
    print("สินค้า:",num,"มีส่วนลด 5% ลดเหลือ:",result)
elif num > 5000 and num < 9999:
    result = num - num/100*10
    print("สินค้า:",num,"มีส่วนลด 10% ลดเหลือ:",result)
elif num > 10000 and num < 29999:
    result = num - num/100*15
    print("สินค้า:",num,"มีส่วนลด 15% ลดเหลือ:",result)
else:
    result = num - num/100*20
    print("สินค้า:",num,"มีส่วนลด 20% ลดเหลือ:",result)



print("ข้อแรก")
result = 0
for i in range(3,3999,3):
    result = result + i
print("แบบที่1:",result)

print("แบบที่2:",(100*(100+1))/2)

print("ข้อสอง")
sum1 = 0
count = 0
while True:
    number = int(input("input Number:"))
    sum1 = sum1 + number
    count+=1
    print("รอบที่",count,"ผลรวม:",sum1)
    if sum1 > 100:
        break
'''
print("ข้อสาม")
import random
boss = 99999
result = 0
count = 0
print("Boss เลือด 99999")
while True:
    cris = ["A","B","C","D"]
    cri = random.choice(cris)
    attack = int(input("input attack:"))
    if cri == "A":
        attack = attack * 2
        boss =  boss - attack
        count+=1
        print("โจมตีคริติคอล:",attack,"\nรอบที่",count)
        print("Boss เลือดเหลือ:",boss,"\n")
    else:
        boss =  boss - attack
        count+=1
        print("โจมตี:",attack,"\nรอบที่",count)
        print("Boss เลือดเหลือ:",boss,"\n")
    if boss <= 0:
        print("Boss ตาย!")
        break


























    
