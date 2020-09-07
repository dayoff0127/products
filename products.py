products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q' :
		break
	price = input('請輸入商品價格: ')
	'''
	p = []
	p.append(name)
	p.append(price)
	縮減成下面
	'''
	products.append([name, price])
print(products)