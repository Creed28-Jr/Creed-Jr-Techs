import os
import sqlite3
from pathlib import Path


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
	("Google Pixel 9 Pro XL", 150000, "New", "google", ("google pixel 9 pro xl", "pixel 9 pro xl")),
	("OnePlus 13", 140000, "New", "oneplus", ("oneplus 13", "one plus 13")),
	("Huawei Pura 70 Ultra", 175000, "New", "huawei", ("huawei pura 70 ultra", "pura 70 ultra")),
	("Sony Xperia 1 VI", 165000, "New", "sony", ("sony xperia 1 vi", "xperia 1 vi")),
	("iPhone Duo Foldable", 320000, "New", "iphone", ("iphone duo", "iphone fold", "foldable iphone")),
	("Samsung Galaxy Z Fold7", 290000, "New", "samsung", ("samsung z fold7", "galaxy z fold7")),
	("Samsung Galaxy Z Flip7", 175000, "New", "samsung", ("samsung z flip7", "galaxy z flip7")),
	("Google Pixel 9 Pro", 140000, "New", "google", ("google pixel 9 pro", "pixel 9 pro")),
	("Google Pixel 9 Pro Fold", 250000, "New", "google", ("google pixel 9 pro fold", "pixel 9 pro fold")),
	("OnePlus Open", 215000, "New", "oneplus", ("oneplus open", "one plus open")),
	("OnePlus 13s", 140000, "New", "oneplus", ("oneplus 13s", "one plus 13s")),
	("Huawei Mate X6", 275000, "New", "huawei", ("huawei mate x6", "mate x6 foldable phone")),
	("Huawei Mate 70 Pro+", 205000, "New", "huawei", ("huawei mate 70 pro+", "mate 70 pro+")),
	("Sony Xperia 1 VII", 210000, "New", "sony", ("sony xperia 1 vii", "xperia 1 vii")),
	("Sony Xperia 5 V", 135000, "New", "sony", ("sony xperia 5 v", "xperia 5 v")),
	("Infinix ZERO 40 5G", 78000, "New", "infinix", ("infinix zero 40 5g", "zero 40 5g")),
	("Infinix NOTE 50 Pro+ 5G", 95000, "New", "infinix", ("infinix note 50 pro+ 5g", "note 50 pro+")),
	("Infinix GT 30 Pro", 90000, "New", "infinix", ("infinix gt 30 pro", "gt 30 pro")),
	("Infinix ZERO Flip", 115000, "New", "infinix", ("infinix zero flip", "zero flip")),
	("Tecno Phantom V Fold2", 155000, "New", "tecno", ("tecno phantom v fold2", "phantom v fold2")),
	("Tecno Phantom V Flip2", 105000, "New", "tecno", ("tecno phantom v flip2", "phantom v flip2")),
	("Tecno Camon 40 Premier 5G", 90000, "New", "tecno", ("tecno camon 40 premier 5g", "camon 40 premier")),
	("Tecno Phantom X2 Pro", 125000, "New", "tecno", ("tecno phantom x2 pro", "phantom x2 pro")),
	("itel S25 Ultra", 35000, "New", "itel", ("itel s25 ultra", "s25 ultra")),
	("itel S24", 25000, "New", "itel", ("itel s24", "s24")),
	("itel RS4", 23000, "New", "itel", ("itel rs4", "rs4")),
	("itel P65", 22000, "New", "itel", ("itel p65", "p65")),
	("Samsung 55-inch Crystal UHD Smart TV", 125000, "New", "tv", ("samsung 55-inch crystal uhd smart tv", "samsung tv")),
	("Hisense 55-inch QLED Smart TV", 155000, "New", "tv", ("hisense 55-inch qled smart tv", "hisense tv")),
	("Vitron 55-inch Smart TV", 70000, "New", "tv", ("vitron 55-inch smart tv", "vitron tv")),
	("TCL 55-inch QLED Smart TV", 135000, "New", "tv", ("tcl 55-inch qled smart tv", "tcl tv")),
	("Samsung Q-Series Soundbar", 180000, "New", "speaker", ("samsung q-series soundbar", "samsung soundbar")),
	("Hisense 3.1 Channel Soundbar", 70000, "New", "speaker", ("hisense 3.1 channel soundbar", "hisense soundbar")),
	("Vitron 5.1 Home Theatre System", 35000, "New", "speaker", ("vitron 5.1 home theatre system", "vitron speakers")),
	("JBL PartyBox Club 120 Speaker", 85000, "New", "speaker", ("jbl partybox club 120", "jbl speaker")),
	("Dell XPS 14 Laptop", 320000, "New", "laptop", ("dell xps 14 laptop", "dell xps 14", "dell laptop")),
	("HP Spectre x360 14 Laptop", 300000, "New", "laptop", ("hp spectre x360 14 laptop", "hp spectre x360", "hp laptop")),
	("Lenovo ThinkPad X1 Carbon Laptop", 350000, "New", "laptop", ("lenovo thinkpad x1 carbon laptop", "thinkpad x1 carbon", "lenovo laptop")),
	("Apple MacBook Pro 14-inch Laptop", 390000, "New", "laptop", ("apple macbook pro 14-inch laptop", "macbook pro 14", "macbook")),
]

phone_categories = ("samsung", "iphone", "google", "oneplus", "huawei", "sony", "infinix", "tecno", "itel")
database_path = Path(os.environ.get("SHOP_DATABASE_PATH", str(Path(__file__).with_name("transactions.db"))))


def initialize_database():
	with sqlite3.connect(database_path) as connection:
		connection.execute("PRAGMA foreign_keys = ON")
		connection.execute(
			"""CREATE TABLE IF NOT EXISTS transactions (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
				payment_method TEXT NOT NULL,
				status TEXT NOT NULL,
				total_ksh INTEGER NOT NULL,
				amount_received_ksh INTEGER,
				change_ksh INTEGER,
				reference TEXT
			)"""
		)
		connection.execute(
			"""CREATE TABLE IF NOT EXISTS transaction_items (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				transaction_id INTEGER NOT NULL REFERENCES transactions(id),
				product TEXT NOT NULL,
				quantity INTEGER NOT NULL,
				unit_price_ksh INTEGER NOT NULL
			)"""
		)
		connection.execute(
			"""CREATE TABLE IF NOT EXISTS reviews (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
				review_text TEXT NOT NULL,
				topic TEXT NOT NULL,
				transaction_reference TEXT
			)"""
		)


def save_transaction(cart, payment_method, status, amount_received=None, reference=None):
	total = sum(product[1] * quantity for product, quantity in cart.items())
	change = amount_received - total if amount_received is not None else None
	with sqlite3.connect(database_path) as connection:
		connection.execute("PRAGMA foreign_keys = ON")
		cursor = connection.execute(
			"""INSERT INTO transactions
				(payment_method, status, total_ksh, amount_received_ksh, change_ksh, reference)
				VALUES (?, ?, ?, ?, ?, ?)""",
			(payment_method, status, total, amount_received, change, reference),
		)
		transaction_id = cursor.lastrowid
		connection.executemany(
			"""INSERT INTO transaction_items
				(transaction_id, product, quantity, unit_price_ksh)
				VALUES (?, ?, ?, ?)""",
			[
				(transaction_id, product[0], quantity, product[1])
				for product, quantity in cart.items()
			],
		)
	return transaction_id


def display_transactions():
	with sqlite3.connect(database_path) as connection:
		transactions = connection.execute(
			"""SELECT id, created_at, payment_method, status, total_ksh, reference
				FROM transactions ORDER BY id DESC LIMIT 10"""
		).fetchall()
		transaction_items = {
			transaction_id: connection.execute(
				"SELECT product, quantity FROM transaction_items WHERE transaction_id = ?",
				(transaction_id,),
			).fetchall()
			for transaction_id, *_ in transactions
		}

	if not transactions:
		print("No saved transactions yet.")
		return

	for transaction_id, created_at, method, status, total, reference in transactions:
		print(f"Transaction #{transaction_id} | {created_at} | {method} | {status} | KSh {total:,}")
		for product, quantity in transaction_items[transaction_id]:
			print(f"  {product} x {quantity}")
		if reference:
			print(f"  Reference: {reference}")


def show_directions():
	address = os.environ.get("SHOP_ADDRESS", "").strip()
	if not address:
		print("I don't have a verified shop address configured, so I can't give reliable directions yet. Please ask shop staff for the address.")
		return
	print(f"Shop address: {address}")
	print("For turn-by-turn directions, search this address in your preferred maps app.")


def classify_review(review_text):
	text = review_text.casefold()
	problem_terms = ("broken", "not working", "damaged", "faulty", "defect", "problem", "issue", "warranty", "cracked", "stopped working")
	positive_terms = ("good", "great", "excellent", "happy", "love", "satisfied", "thank")
	service_terms = ("service", "staff", "delivery", "wait", "support")
	if any(term in text for term in problem_terms):
		return "product_problem"
	if any(term in text for term in positive_terms):
		return "positive"
	if any(term in text for term in service_terms):
		return "service"
	return "general"


def submit_review(review_text):
	topic = classify_review(review_text)
	reference = None
	if topic == "product_problem":
		reference = input("Optional receipt or transaction ID for warranty follow-up (press Enter to skip): ").strip() or None
	with sqlite3.connect(database_path) as connection:
		connection.execute(
			"INSERT INTO reviews (review_text, topic, transaction_reference) VALUES (?, ?, ?)",
			(review_text, topic, reference),
		)
	if topic == "positive":
		print("Thank you, we are here to satisfy our customers.")
	else:
		print("We will check on that.")
	if topic == "product_problem":
		print("We can review the item's warranty. Please keep your receipt and share its transaction ID with shop staff. Coverage and eligibility follow the shop's warranty terms.")


def display_review_summary():
	with sqlite3.connect(database_path) as connection:
		review_count = connection.execute("SELECT COUNT(*) FROM reviews").fetchone()[0]
		topics = connection.execute(
			"SELECT topic, COUNT(*) FROM reviews GROUP BY topic ORDER BY topic"
		).fetchall()
	if not review_count:
		print("No customer reviews have been saved yet.")
		return
	print(f"Saved customer reviews: {review_count}")
	print("Review themes are grouped using simple keywords; this does not train an AI model.")
	for topic, count in topics:
		print(f"{topic.replace('_', ' ').title()}: {count}")


def display_products(products):
	item_width = max(len("Product"), *(len(product[0]) for product in products))
	price_width = 14
	table_width = item_width + price_width + 13
	print("=" * table_width)
	print(f"{'Product':<{item_width}}  {'Price (KSh)':>{price_width}}  {'Condition':<9}")
	print("-" * table_width)

	for item, price, condition, _, _ in products:
		print(f"{item:<{item_width}}  {'KSh ' + format(price, ','):>{price_width}}  {condition:<9}")

	print("=" * table_width)


def display_cart(cart):
	if not cart:
		print("Your cart is empty.")
		return 0

	item_width = max(len("Product"), *(len(product[0]) for product in cart))
	line_width = item_width + 45
	total = 0
	print("=" * line_width)
	print(f"{'Product':<{item_width}}  {'Qty':>5}  {'Unit price':>14}  {'Amount':>14}")
	print("-" * line_width)

	for product, quantity in cart.items():
		price = product[1]
		line_amount = price * quantity
		total += line_amount
		print(f"{product[0]:<{item_width}}  {quantity:>5}  {'KSh ' + format(price, ','):>14}  {'KSh ' + format(line_amount, ','):>14}")

	print("-" * line_width)
	print(f"{'TOTAL':<{item_width + 9}}  {'KSh ' + format(total, ','):>29}")
	print("=" * line_width)
	return total


def checkout(cart):
	total = display_cart(cart)
	if total == 0:
		return False

	while True:
		payment_method = input("Payment method (cash / M-Pesa / card / cancel): ").strip().casefold()
		if payment_method == "cash":
			while True:
				amount_text = input("Cash received in KSh: ").strip().replace(",", "")
				if not amount_text.isdigit():
					print("Enter the cash amount as a whole number.")
					continue

				amount_received = int(amount_text)
				if amount_received < total:
					print(f"That is not enough. The total is KSh {total:,}.")
					continue

				try:
					transaction_id = save_transaction(cart, "Cash", "PAID", amount_received)
				except sqlite3.Error:
					print("Cash received, but the transaction could not be saved. Please keep a manual record and contact the shop administrator.")
					return "paid"
				print(f"Cash received: KSh {amount_received:,}")
				print(f"Change: KSh {amount_received - total:,}")
				print(f"Saved transaction #{transaction_id}.")
				return "paid"
		if payment_method in ("m-pesa", "mpesa", "card"):
			method_name = "M-Pesa" if payment_method in ("m-pesa", "mpesa") else "Card"
			payment_location = "the official M-Pesa app" if method_name == "M-Pesa" else "a card terminal"
			print(f"Complete {method_name} payment using {payment_location}. Do not enter a PIN or card number here.")
			reference = input("Payment reference from the provider, or 'cancel': ").strip()
			if reference.casefold() == "cancel":
				print("Checkout cancelled. Your cart is still available.")
				return None
			if not reference:
				print("A provider reference is required to save this as pending verification.")
				continue
			try:
				transaction_id = save_transaction(cart, method_name, "PENDING VERIFICATION", reference=reference)
			except sqlite3.Error:
				print("The transaction could not be saved. No payment was verified by this program.")
				return None
			print(f"Saved transaction #{transaction_id} as pending verification. This program cannot verify or process electronic payments.")
			return "pending"
		elif payment_method == "cancel":
			print("Checkout cancelled. Your cart is still available.")
			return False
		else:
			print("Please choose cash, M-Pesa, card, or cancel.")


initialize_database()
print("Hi, how are you?")
customer_response = input()
print("Thanks for sharing. What product can I help you find today?")
cart = {}
sale_completed = False
pending_payment = False

while True:
	raw_request = input("> ").strip()
	customer_request = raw_request.casefold()
	if customer_request == "review" or customer_request.startswith(("review ", "review:")):
		review_text = raw_request[7:].strip() if customer_request.startswith(("review:", "review ")) else ""
		if not review_text:
			review_text = input("Please enter your review: ").strip()
		if review_text:
			submit_review(review_text)
		else:
			print("No review was entered.")
		continue
	if customer_request in ("review summary", "review trends", "reviews"):
		display_review_summary()
		continue
	if any(term in customer_request for term in ("direction", "address", "location", "where are you", "where is the shop", "how do i get to", "how do i get there", "how to get there", "navigate", "map to")):
		show_directions()
		continue
	if customer_request in ("done", "no thanks", "exit", "quit"):
		if cart:
			print("Your cart still has items. Type 'checkout' to purchase them or 'leave' to exit without buying.")
			continue
		if sale_completed:
			print("Thanks for shopping with us. Have a blessed day!")
		elif pending_payment:
			print("Your electronic payment is pending manual verification. Please keep your provider reference. Thank you for visiting.")
		else:
			print("I'm sorry we couldn't help you find what you wanted today. We hope we can help next time. Thanks for visiting, please come again, and feel free to bring your friends!")
		break
	if customer_request == "leave":
		cart.clear()
		if sale_completed:
			print("Thanks for shopping with us. Have a blessed day!")
		elif pending_payment:
			print("Your electronic payment is pending manual verification. Please keep your provider reference. Thank you for visiting.")
		else:
			print("I'm sorry we couldn't help you find what you wanted today. We hope we can help next time. Thanks for visiting, please come again, and feel free to bring your friends!")
		break
	if customer_request == "cart":
		display_cart(cart)
		continue
	if customer_request == "transactions":
		display_transactions()
		continue
	if customer_request == "checkout":
		checkout_result = checkout(cart)
		if checkout_result == "paid":
			sale_completed = True
			cart.clear()
			print("Thanks for shopping with us. Have a blessed day!")
			break
		if checkout_result == "pending":
			pending_payment = True
			cart.clear()
			print("The order is saved, but it is not marked paid until the provider verifies the reference.")
		continue
	if customer_request.startswith(("buy ", "add ")):
		purchase_request = customer_request.split(maxsplit=1)[1]
		quantity = 1
		if " x" in purchase_request:
			product_request, quantity_text = purchase_request.rsplit(" x", 1)
			if quantity_text.isdigit():
				purchase_request = product_request.strip()
				quantity = int(quantity_text)
		if quantity < 1:
			print("Please choose a quantity greater than zero.")
			continue

		matching_items = [
			product for product in items
			if any(alias in purchase_request for alias in product[4])
		]
		if len(matching_items) == 1:
			product = matching_items[0]
			cart[product] = cart.get(product, 0) + quantity
			print(f"Added {quantity} x {product[0]} to your cart.")
			display_cart(cart)
		elif matching_items:
			print("Please add one exact product at a time. Matching products:")
			display_products(matching_items)
		else:
			print("That product is not in our catalog. Ask about a listed product to see its price and condition.")
		continue

	requested_items = [
		product
		for product in items
		if any(alias in customer_request for alias in product[4])
	]
	catalog_request_words = ("catalog", "list", "products", "items", "available", "sell")
	show_catalog = any(word in customer_request for word in catalog_request_words)
	has_model_number = any(character.isdigit() for character in customer_request)

	if requested_items:
		response_items = requested_items
		response_message = "Here are the matching products from our catalog:"
		if "iphone" in customer_request and "pro" in customer_request and not has_model_number:
			response_items = [product for product in items if product[3] == "iphone"]
	elif any(term in customer_request for term in ("fold", "flip", "foldable")):
		response_items = [
			product for product in items
			if any(term in product[0].casefold() or any(term in alias for alias in product[4]) for term in ("fold", "flip", "open"))
		]
		response_message = "Here are the foldable and flip phones in our catalog:"
	elif ("samsung" in customer_request or "galaxy" in customer_request or "s series" in customer_request) and (not has_model_number or "series" in customer_request or "models" in customer_request):
		response_items = [product for product in items if product[3] == "samsung"]
		response_message = "Here are our Samsung Galaxy S-series models:"
	elif ("iphone" in customer_request or "apple" in customer_request) and (not has_model_number or "models" in customer_request):
		response_items = [product for product in items if product[3] == "iphone"]
		response_message = "Here are our Pro iPhone models:"
	elif ("google" in customer_request or "pixel" in customer_request) and (not has_model_number or "models" in customer_request):
		response_items = [product for product in items if product[3] == "google"]
		response_message = "Here is our premium Google Pixel model:"
	elif ("oneplus" in customer_request or "one plus" in customer_request) and (not has_model_number or "models" in customer_request):
		response_items = [product for product in items if product[3] == "oneplus"]
		response_message = "Here is our premium OnePlus model:"
	elif "huawei" in customer_request and (not has_model_number or "models" in customer_request):
		response_items = [product for product in items if product[3] == "huawei"]
		response_message = "Here is our premium Huawei model:"
	elif "sony" in customer_request and (not has_model_number or "models" in customer_request):
		response_items = [product for product in items if product[3] == "sony"]
		response_message = "Here is our premium Sony model:"
	elif "infinix" in customer_request and (not has_model_number or "models" in customer_request):
		response_items = [product for product in items if product[3] == "infinix"]
		response_message = "Here are our Infinix models:"
	elif "tecno" in customer_request and (not has_model_number or "models" in customer_request):
		response_items = [product for product in items if product[3] == "tecno"]
		response_message = "Here are our Tecno models:"
	elif "itel" in customer_request and (not has_model_number or "models" in customer_request):
		response_items = [product for product in items if product[3] == "itel"]
		response_message = "Here are our itel models:"
	elif any(term in customer_request for term in ("tv", "television")) and not has_model_number:
		response_items = [product for product in items if product[3] == "tv"]
		brand = next((brand for brand in ("samsung", "hisense", "vitron", "tcl") if brand in customer_request), None)
		if brand:
			response_items = [product for product in response_items if brand in product[0].casefold()]
		response_message = "Here are the televisions in our catalog:"
	elif any(term in customer_request for term in ("speaker", "speakers", "soundbar", "home theatre")) and not has_model_number:
		response_items = [product for product in items if product[3] == "speaker"]
		brand = next((brand for brand in ("samsung", "hisense", "vitron", "jbl") if brand in customer_request), None)
		if brand:
			response_items = [product for product in response_items if brand in product[0].casefold()]
		response_message = "Here are the speakers and sound systems in our catalog:"
	elif "laptop" in customer_request and not has_model_number:
		response_items = [product for product in items if product[3] == "laptop"]
		brand = next((brand for brand in ("dell", "hp", "lenovo", "apple") if brand in customer_request), None)
		if brand:
			response_items = [product for product in response_items if brand in product[0].casefold()]
		response_message = "Here are the laptops in our catalog:"
	elif "accessor" in customer_request:
		response_items = [product for product in items if product[3] == "accessory"]
		response_message = "Here are the accessories currently in our catalog:"
	elif "phone" in customer_request and any(word in customer_request for word in ("phones", "all", "models")):
		response_items = [product for product in items if product[3] in phone_categories]
		response_message = "Here are the phone models currently in our catalog:"
	elif show_catalog:
		response_items = items
		response_message = "Here is our current product catalog:"
	else:
		response_message = f"Sorry, we don't currently have '{customer_request}' in our catalog. Here are some available alternatives:"
		if any(word in customer_request for word in ("phone", "samsung", "galaxy", "iphone", "apple", "mobile", "google", "pixel", "oneplus", "one plus", "huawei", "sony", "xperia", "infinix", "tecno", "itel")):
			response_items = [product for product in items if product[3] in phone_categories]
		elif any(word in customer_request for word in ("tv", "television")):
			response_items = [product for product in items if product[3] == "tv"]
		elif any(word in customer_request for word in ("speaker", "soundbar", "home theatre")):
			response_items = [product for product in items if product[3] == "speaker"]
		elif "laptop" in customer_request:
			response_items = [product for product in items if product[3] == "laptop"]
		elif any(word in customer_request for word in ("accessory", "charger", "case", "cable", "disk", "flash", "ear", "headphone", "power", "keyboard", "mouse", "protector", "stand")):
			response_items = [product for product in items if product[3] == "accessory"]
		else:
			response_items = items

	print(response_message)
	display_products(response_items)
	print("Ask about another product, use 'buy <product> x<quantity>' to add it, or try 'directions' or 'review <your feedback>'.")

