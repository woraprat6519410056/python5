#รับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้ และคำนวนหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามาเป็นเท่าใดแล้วแสดงผลทางหน้าจอ

#ขอ 4 ฟังก์ชัน ดังนั้นหาให้ได้ 4 feature

#===============================================
#          Program Average 5 Number
#===============================================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
#===============================================
# Sum of 5 number is : <output>
# Average of 5 number is : <output> (ขอทศนิยม 4 ตำแหน่ง)
#===============================================

def inputData( ) :
    n1=int(input('ใส่เลขที่ 1 :'))
    n2=int(input('ใส่เลขที่ 2 :'))
    n3=int(input('ใส่เลขที่ 3 :'))
    n4=int(input('ใส่เลขที่ 4 :'))
    n5=int(input('ใส่เลขที่ 5 :'))
    return n1, n2, n3, n4, n5

def SumoFnuber (n1, n2, n3, n4, n5) :
    SumoFnuber = (n1 + n2 + n3 + n4 + n5)
    return SumoFnuber

def Avergeofnuber (n1, n2, n3, n4, n5) :
    Avergeofnuber = ((n1 + n2 + n3 + n4 + n5)/5)
    return Avergeofnuber

def show(n1, n2, n3, n4, n5,SumoFnuber,Avergeofnuber) :
    print(f'ผลรวมของเลขทั้ง 5 : {SumoFnuber} ')
    print(f'ค่าเฉลื่ยของเลขทั้ง 5 : {Avergeofnuber:.4f} ')

print("===============================================")
print("==========Program Average 5 Number=============")
print("===============================================")
n1, n2, n3, n4, n5 = inputData ( )
print("===============================================")
SumoFnuber  = SumoFnuber (n1, n2, n3, n4, n5)
Avergeofnuber = Avergeofnuber (n1, n2, n3, n4, n5)
show (n1, n2, n3, n4, n5, SumoFnuber, Avergeofnuber)
print("===============================================")