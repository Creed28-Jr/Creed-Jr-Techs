items = [
	("Keyboard", 1500, "New", "accessory", ("keyboard",)),
	("Mouse", 800, "New", "accessory", ("mouse",)),
	("Flash disk", 1200, "New", "accessory", ("flash disk", "flash drive")),
	("Headphones", 2500, "New", "accessory", ("headphones", "headphone")),
	("USB cables", 500, "New", "accessory", ("usb cables", "usb cable")),
	("Wall charger", 1800, "New", "accessory", ("wall charger", "charger")),
	("Phone case", 1000, "New", "accessory", ("phone case", "case")),
	("Screen protector", 700, "New", "accessory", ("screen protector",)),
	("Power bank", 4500, "New", "accessory", ("power bank",)),
	("Wireless earbuds", 3500, "New", "accessory", ("wireless earbuds", "earbuds")),
	("Phone stand", 1200, "New", "accessory", ("phone stand",)),
	("Samsung Galaxy S23", 65000, "New", "samsung", ("samsung galaxy s23", "samsung s23", "galaxy s23")),
	("Samsung Galaxy S24", 80000, "New", "samsung", ("samsung galaxy s24", "samsung s24", "galaxy s24")),
	("Samsung Galaxy S25", 95000, "New", "samsung", ("samsung galaxy s25", "samsung s25", "galaxy s25")),
	("Samsung Galaxy S26", 110000, "New", "samsung", ("samsung galaxy s26", "samsung s26", "galaxy s26")),
	("iPhone 15 Pro", 120000, "New", "iphone", ("iphone 15 pro", "15 pro")),
	("iPhone 16 Pro", 145000, "New", "iphone", ("iphone 16 pro", "16 pro")),
	("iPhone 17 Pro", 170000, "New", "iphone", ("iphone 17 pro", "17 pro")),
]

print("Hi, how are you?")
customer_response = input()
print("How may I assist you?")
customer_request = input().strip().casefold()

requested_items = [
	product
	for product in items
	if any(alias in customer_request for alias in product[4])
]

catalog_request_words = ("catalog", "list", "products", "items", "available", "sell")
show_catalog = any(word in customer_request for word in catalog_request_words)

if requested_items:
	response_items = requested_items
	response_message = ""
	if "iphone" in customer_request and "pro" in customer_request:
		response_items = [product for product in items if product[3] == "iphone"]
elif "samsung" in customer_request or "galaxy" in customer_request or "s series" in customer_request:
	response_items = [product for product in items if product[3] == "samsung"]
	response_message = ""
elif "iphone" in customer_request or "apple" in customer_request:
	response_items = [product for product in items if product[3] == "iphone"]
	response_message = ""
elif "accessor" in customer_request:
	response_items = [product for product in items if product[3] == "accessory"]
	response_message = ""
elif "phone" in customer_request and any(word in customer_request for word in ("phones", "all", "models")):
	response_items = [product for product in items if product[3] in ("samsung", "iphone")]
	response_message = ""
elif show_catalog:
	response_items = items
	response_message = ""
else:
	response_message = "Sorry, that product is not available. Here is our current product list:"
	response_items = items

if response_message:
	print(response_message)

item_width = max(len("Product"), *(len(product[0]) for product in response_items))
price_width = 14
table_width = item_width + price_width + 13
print("=" * table_width)
print(f"{'Product':<{item_width}}  {'Price (KSh)':>{price_width}}  {'Condition':<9}")
print("-" * table_width)

for item, price, condition, _, _ in response_items:
	print(f"{item:<{item_width}}  {'KSh ' + format(price, ','):>{price_width}}  {condition:<9}")

print("=" * table_width)

