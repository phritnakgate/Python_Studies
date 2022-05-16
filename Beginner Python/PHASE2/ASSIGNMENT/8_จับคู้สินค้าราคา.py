#จับคู่สินค้าราคา
goods = ["มะม่วงดอง", "แตงโมปั่น", "ฝรั่งแช่บ๊วย"]
price = [50,30,15]
for x,y in zip(goods,price[::-1]):
    print(x,y)