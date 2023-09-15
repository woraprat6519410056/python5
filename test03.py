#คำนวณหาราคาขายสินค้า โดยรับซื้อสินค้า และราคาสินค้า(ต้นทุน) ทางแป้นพิมพ์
#แล้วคำนวณหาราคาของสินค้า โดยราคาขายสินค้าจะคิดเพิ่มจากราคาสินค้า (ต้นทุน) ร้อยละ 10
#สูตร ราคาขายสินค้า = ราคาสินค้า(ต้นทุน) - (ราคาสินค้า(ต้นทุน) * 10 / 100)

#Feature ในการรับค่า การคำนวณ และการแสดงผลแยกจากกัน
#ดังนั้นอย่างน้อยมี 3 ฟังก์ชัน

def inputData( ) :
    product_name = input('ป้อนชื่อสินค้า')
    product_price = float( input('ป้อนราคาสินค้า(ต้นทุน)'))
    return product_name, product_price

def calProductSale( product_price ) :
    product_sale = product_price + (product_price * 10 / 100)
    return product_sale

def showProductsale( product_name, product_price, product_sale) :
    print(f'ชื่อสินค้า{product_name}')
    print(f'ราคาสินค้า(ต้นทุน){product_price:.2f} บาท')
    print(f'ราคาขายสินค้า{product_sale:.2f} บาท')

print('----------------------')
print('--** Product_Sale **--')
print('----------------------')
product_name, product_price = inputData( )
product_sale = calProductSale( product_price )
print('----------------------')
showProductsale( product_name, product_price, product_sale )
print('----------------------')