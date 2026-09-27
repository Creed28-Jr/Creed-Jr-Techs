items = [
	("Keyboard", 1500),
	("Mouse", 800),
	("Flash disk", 1200),
	("Headphones", 2500),
	("USB cables", 500),
]

print("Hi, how are you?")
customer_response = input()
print("How may I assist you?")

subtotal = sum(price for _, price in items)

print("=" * 34)
print("          SALES RECEIPT")
print("=" * 34)
print(f"{'Item':<16}{'Qty':>5}{'Price':>7}{'Amount':>8}")
print("-" * 34)

for item, price in items:
	print(f"{item:<16}{1:>5}{price:>7,}{price:>8,}")

print("-" * 34)
print(f"{'TOTAL':<22}{subtotal:>10,}")
print("=" * 34)

