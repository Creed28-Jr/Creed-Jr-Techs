# Creed-Jr-Techs

Creed Jr Techs brings together accessories, premium phones, foldables, televisions, speakers, and laptops from a range of brands. Clear KSh prices and product information make it easy to compare options.

## Run

```powershell
python Specs.py
```

The program greets the customer, handles multiple product questions in one conversation, and displays matching products with prices in Kenyan shillings (KSh) and their condition. When an item is unavailable, it says so and offers alternatives from the listed catalog. Use `buy <product> x<quantity>` to add an item, `cart` to review it, and `checkout` to pay or record an electronic payment for verification. Use `transactions` to view recent records, `review <feedback>` to submit feedback, `reviews` to view keyword-based review themes, and `directions` to request the shop address. Set `SHOP_ADDRESS` to a verified address to enable directions; without it, the program will say it is not configured.

Cash sales and item details are saved locally in `transactions.db` between runs. M-Pesa and card selections save a transaction reference with `PENDING VERIFICATION` status; this standalone program does not connect to a payment provider or verify electronic payments. Complete electronic payments only through the official M-Pesa app or a card terminal, and never enter a PIN or card number into the program. The local transaction database is excluded from Git.

Customer reviews are also saved locally. The `reviews` command groups them into simple keyword-based themes; it does not train or modify an AI model. Reviews receive the response "We will check on that." Product-problem reviews are flagged for warranty follow-up, but exact warranty coverage and eligibility must be checked against the shop's policy.

## Product Catalog

| Product | Price | Condition |
| --- | ---: | --- |
| Keyboard | KSh 1,500 | New |
| Mouse | KSh 800 | New |
| Flash disk | KSh 1,200 | New |
| Headphones | KSh 2,500 | New |
| USB cables | KSh 500 | New |
| Wall charger | KSh 1,800 | New |
| Phone case | KSh 1,000 | New |
| Screen protector | KSh 700 | New |
| Power bank | KSh 4,500 | New |
| Wireless earbuds | KSh 3,500 | New |
| Phone stand | KSh 1,200 | New |
| Samsung Galaxy S23 | KSh 65,000 | New |
| Samsung Galaxy S24 | KSh 80,000 | New |
| Samsung Galaxy S25 | KSh 95,000 | New |
| Samsung Galaxy S26 | KSh 110,000 | New |
| iPhone 15 Pro | KSh 120,000 | New |
| iPhone 16 Pro | KSh 145,000 | New |
| iPhone 17 Pro | KSh 170,000 | New |
| Google Pixel 9 Pro XL | KSh 150,000 | New |
| OnePlus 13 | KSh 140,000 | New |
| Huawei Pura 70 Ultra | KSh 175,000 | New |
| Sony Xperia 1 VI | KSh 165,000 | New |
| iPhone Duo Foldable | KSh 320,000 | New |
| Samsung Galaxy Z Fold7 | KSh 290,000 | New |
| Samsung Galaxy Z Flip7 | KSh 175,000 | New |
| Google Pixel 9 Pro | KSh 140,000 | New |
| Google Pixel 9 Pro Fold | KSh 250,000 | New |
| OnePlus Open | KSh 215,000 | New |
| OnePlus 13s | KSh 140,000 | New |
| Huawei Mate X6 | KSh 275,000 | New |
| Huawei Mate 70 Pro+ | KSh 205,000 | New |
| Sony Xperia 1 VII | KSh 210,000 | New |
| Sony Xperia 5 V | KSh 135,000 | New |
| Infinix ZERO 40 5G | KSh 78,000 | New |
| Infinix NOTE 50 Pro+ 5G | KSh 95,000 | New |
| Infinix GT 30 Pro | KSh 90,000 | New |
| Infinix ZERO Flip | KSh 115,000 | New |
| Tecno Phantom V Fold2 | KSh 155,000 | New |
| Tecno Phantom V Flip2 | KSh 105,000 | New |
| Tecno Camon 40 Premier 5G | KSh 90,000 | New |
| Tecno Phantom X2 Pro | KSh 125,000 | New |
| itel S25 Ultra | KSh 35,000 | New |
| itel S24 | KSh 25,000 | New |
| itel RS4 | KSh 23,000 | New |
| itel P65 | KSh 22,000 | New |
| Samsung 55-inch Crystal UHD Smart TV | KSh 125,000 | New |
| Hisense 55-inch QLED Smart TV | KSh 155,000 | New |
| Vitron 55-inch Smart TV | KSh 70,000 | New |
| TCL 55-inch QLED Smart TV | KSh 135,000 | New |
| Samsung Q-Series Soundbar | KSh 180,000 | New |
| Hisense 3.1 Channel Soundbar | KSh 70,000 | New |
| Vitron 5.1 Home Theatre System | KSh 35,000 | New |
| JBL PartyBox Club 120 Speaker | KSh 85,000 | New |
| Dell XPS 14 Laptop | KSh 320,000 | New |
| HP Spectre x360 14 Laptop | KSh 300,000 | New |
| Lenovo ThinkPad X1 Carbon Laptop | KSh 350,000 | New |
| Apple MacBook Pro 14-inch Laptop | KSh 390,000 | New |

Only products listed above are offered by the program. If a requested product is missing from the catalog, it reports that the product is unavailable rather than inventing a price or stock status.

The newly added models and prices are suggested catalog entries, not verified stock or supplier quotes. Confirm exact models, availability, condition, and supplier pricing before sale.
