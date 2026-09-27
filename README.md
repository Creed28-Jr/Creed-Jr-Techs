# Creed-Jr-Techs

Creed Jr Techs brings together accessories, premium phones, foldables, televisions, speakers, and laptops from a range of brands. Clear KSh prices and product information make it easy to compare options.

## Run

```powershell
python Specs.py
```

The program greets the customer and keeps a relaxed conversation. It shows a product table when the customer asks for prices or requests the catalog; a specific price question shows the matching item, while a general price request can show the full catalog. A product question without a price request asks whether the customer wants pricing. If several products match, the customer can specify a brand, model, or tier and receive that item's price as a short reply; `show all prices` lists all matching prices without a table. Phone requests first announce the related models or brands. If a listed model is reported out of stock, it says so and excludes that model from alternatives. If an item isn't in the catalog, it says it isn't stocked and offers relevant alternatives without inventing stock or prices. Ask for `budget`, `entry-level`, or `affordable` phones to see lower-priced models. When adding an ambiguous item with `buy <product> x<quantity>`, the assistant asks which brand, model, or tier the customer wants. Unrelated requests receive a polite redirect to the shop's product categories without displaying a table. Use `bargain` to request a one-time discount of up to KSh 1,000, `cart` to review the subtotal and discount, and `checkout` to pay or record an electronic payment for verification. Use `transactions` to view recent records, `review <feedback>` to submit feedback, `reviews` to view keyword-based review themes, and `directions` to request the shop address. Set `SHOP_ADDRESS` to a verified address to enable directions; without it, the program will say it is not configured.

For tiered accessories, customers can ask for a `good`, `better`, or `best` option (for example, `best keyboard`). Tier rankings guide recommendations but are not shown as a table column. When adding a broad accessory request to the cart, the assistant asks for a brand or tier if needed. The bargain discount applies once per cart, up to KSh 1,000, and is saved with the transaction.

Cash sales, bargain discounts, and item details are saved locally in `transactions.db` between runs. M-Pesa and card selections save a transaction reference with `PENDING VERIFICATION` status; this standalone program does not connect to a payment provider or verify electronic payments. Complete electronic payments only through the official M-Pesa app or a card terminal, and never enter a PIN or card number into the program. The local transaction database is excluded from Git.

Customer reviews are also saved locally. The `reviews` command groups them into simple keyword-based themes; it does not train or modify an AI model. Positive reviews receive "Thank you, we are here to satisfy our customers." Other reviews receive "We will check on that." Product-problem reviews are flagged for warranty follow-up, but exact warranty coverage and eligibility must be checked against the shop's policy.

`inventory_status.md` is the RAG-readable source for availability replies and confirmed out-of-stock items. Update its status table only with verified inventory information; an item missing from that table has unknown availability, not confirmed stock.

## Product Catalog

| Product | Price | Condition |
| --- | ---: | --- |
| Havit Wired Keyboard | KSh 1,200 | New |
| Logitech Wireless Keyboard | KSh 3,500 | New |
| Razer Mechanical Keyboard | KSh 14,500 | New |
| Havit Wired Mouse | KSh 900 | New |
| Logitech Wireless Mouse | KSh 4,800 | New |
| Razer Wireless Gaming Mouse | KSh 14,500 | New |
| SanDisk USB Flash Drive 32GB | KSh 1,000 | New |
| Kingston USB Flash Drive 64GB | KSh 1,900 | New |
| Samsung USB Flash Drive 128GB | KSh 4,500 | New |
| JBL Wired Headphones | KSh 3,500 | New |
| Sony Wireless Headphones | KSh 14,500 | New |
| Bose Noise-Cancelling Headphones | KSh 52,000 | New |
| USB-A to USB-C Cable | KSh 400 | New |
| Anker USB-C to USB-C Cable | KSh 1,200 | New |
| Belkin Braided USB-C Cable | KSh 2,500 | New |
| Lightning Cable | KSh 700 | New |
| Anker Lightning Cable | KSh 1,800 | New |
| Belkin Braided Lightning Cable | KSh 3,200 | New |
| Standard USB-A to Micro-USB Cable | KSh 350 | New |
| Anker Reinforced Micro-USB Cable | KSh 900 | New |
| Belkin Braided Micro-USB Cable | KSh 1,700 | New |
| Generic 65W Laptop Charger | KSh 4,500 | New |
| Dell 90W Laptop Charger | KSh 7,500 | New |
| Anker 100W Laptop Charger | KSh 10,500 | New |
| Clear TPU Screen Protector | KSh 500 | New |
| Ceramic Film Screen Protector | KSh 900 | New |
| Spigen Tempered Glass Screen Protector | KSh 2,200 | New |
| Havit Silicone Phone Case | KSh 700 | New |
| Spigen Clear Protective Phone Case | KSh 1,800 | New |
| OtterBox Rugged Phone Case | KSh 6,500 | New |
| Leather Flip Phone Case | KSh 2,500 | New |
| Power bank | KSh 4,500 | New |
| Wireless earbuds | KSh 3,500 | New |
| Phone stand | KSh 1,200 | New |
| Samsung Galaxy S23 | KSh 65,000 | New |
| Samsung Galaxy S24 | KSh 80,000 | New |
| Samsung Galaxy S25 | KSh 95,000 | New |
| Samsung Galaxy S26 | KSh 110,000 | New |
| Samsung Galaxy A16 | KSh 18,000 | New |
| iPhone 15 Pro | KSh 120,000 | New |
| iPhone 16 Pro | KSh 145,000 | New |
| iPhone 17 Pro | KSh 170,000 | New |
| iPhone 16e | KSh 90,000 | New |
| Google Pixel 9 Pro XL | KSh 150,000 | New |
| Google Pixel 9a | KSh 75,000 | New |
| OnePlus 13 | KSh 140,000 | New |
| OnePlus Nord CE4 Lite | KSh 43,000 | New |
| Huawei Pura 70 Ultra | KSh 175,000 | New |
| Huawei nova 13i | KSh 37,000 | New |
| Sony Xperia 1 VI | KSh 165,000 | New |
| Sony Xperia 10 VI | KSh 60,000 | New |
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
| Infinix SMART 9 HD | KSh 12,000 | New |
| Tecno Phantom V Fold2 | KSh 155,000 | New |
| Tecno Phantom V Flip2 | KSh 105,000 | New |
| Tecno Camon 40 Premier 5G | KSh 90,000 | New |
| Tecno Phantom X2 Pro | KSh 125,000 | New |
| Tecno SPARK 30C | KSh 14,000 | New |
| itel S25 Ultra | KSh 35,000 | New |
| itel S24 | KSh 25,000 | New |
| itel RS4 | KSh 23,000 | New |
| itel P65 | KSh 22,000 | New |
| itel A90 | KSh 10,000 | New |
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
