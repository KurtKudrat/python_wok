
'''
list = []

names = ['alim','max','ehson','jun','kaysar','kaysar']


for name in names:
    if name =='kaysar':
        list.append(name)

num = len(list)

if num > 0:
    print("there are " + str(num) + "kaysar.")
elif num == 0:
    print("there is no kaysar")


'''


products_price = {
    'book':2,
    'pen':5,
    'penile': 1,
    'remote':6,
    'xbox':2
}

products_sale_counts = {
    'book': 2,
    'pen': 2,
    'penile': 3,
    'remote': 1,
    'xbox': 5
}

Sale_report = {

}

for product, price in products_price.items():

    for product_sale , product_count in products_sale_counts.items():

        if product == product_sale:
            total_sale = price * product_count
            Sale_report.update({product:total_sale})

            #print(product.title() + " total sale is " + str(total_sale) )
print(Sale_report)