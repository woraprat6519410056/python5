#คำนวณภาษีที่ต้องจ่าย และเงินเดือนสุทธิของพนักงาน แล้วแสดงผลหน้าจอ โดยรับค่ารหัสพนักงาน ชื่อพนักงาน 
#และเงินเดือนปกติของพนักงานทางแป้นพิมพ์ ทั้งนี้เงินเดือนสุทธิของพนักงานนั้นจะต้องหักค่าภาษี และเบี้ยประกันสังคมออกจากเงินเดือนกติเสียก่อน
#โดยที่พนักงานต้องเสียภาษา 7% ของเงินเดือนปกติ และจ่ายค่าเบี้ยประกันสังคม 500 บาท

#ขอ 5 ฟังก์ฃัน ดังนั้นต้องหาให้ได้ 5 feture

#===============================================
#            คำนวณเงินเดือนพนักงาน
#===============================================
# ป้อนรหัสพนักงาน : <input>
# ป้อนชื่อพนักงาน : <input>
# ป้อนเงินเดือนพนักงาน : <input> บาท
#===============================================
# ภาษีเป็นเงิน : <output> บาท (ขอทศนิยม 2 ตำแหน่ง)
# เงินเดือนสุทธิเป็นเงิน : <output> บาท (ขอทศนิยม 2 ตำแหน่ง)
#===============================================

def A():
    ID = input ("ป้อนรหัสพนักงาน: ")
    NAME = input ("ป้อนชื่อพนักงาน: ")
    ML = float(input("ป้อนเงินเดือนปกติของพนักงาน: "))
    return ID, NAME, ML

def B(ML):
    PC = 7
    TAX = (ML * PC ) / 100
    return TAX

def C() :
    SSF = 500
    return SSF

def D(ML, TAX, SSF) :
    NS = ML - TAX - SSF
    return NS

def E(ID, NAME, ML, TAX, SSF,NS) :
    print (f"ป้อนรหัสพนักงาน : {ID}")
    print (f"ป้อนชื่อพนักงาน : {NAME}")
    print (f"ป้อนเงินเดือนพนักงาน : {ML:.2f} บาท")
    print (f"ภาษีเงินเดือน : {TAX:.2f} บาท")
    print (f"ค่าเบี้ยประกันสังคม : {SSF:.2f} บาท")
    print (f"เงินเดือนสุทธิเป็นเงิน : {NS:.2f} บาท")

print("===============================================")
print("==========คำนวณเงินเดือนพนักงาน===================")
print("===============================================")
ID, NAME, ML = A()
print("===============================================")
TAX = B(ML)
SSF = C()
NS = D(ML, TAX, SSF)
E(ID, NAME, ML, TAX, SSF, NS)
print("===============================================")