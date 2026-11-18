#Exercise 2/3

import csv
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)

#Exercise 4

total_revenue = 0 
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        product = row [0]
        price = float(row[1])
        quantity = int(row[2])
        revenue = price * quantity
        total_revenue += revenue
        print(f"{product}: {quantity} units * ${price:.2f} = ${revenue:.2f}")
print(f" Total Revenue: ${total_revenue:.2f}")

#Exercise 5
with open("data/sales.csv", "r", encoding="utf-8") as f:
    with open("data/cleaned.csv", "w" , newline="", encoding="utf-8") as out:
        reader = csv.reader(f)
        writer = csv.writer(out)
        header = next(reader)
        writer.writerow([header[0],header[1], header[2], "total"])

        for row in reader:
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, f"{total:.2f}"])

#Exercise 6

total_revenue_dict = 0
with open("data/sales.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        revenue = price * quantity
        total_revenue_dict += revenue
        print(f"{product}: {quantity} units * ${price:.2f} = ${revenue:.2f}")
print(f"Total Revenue (DictReader): ${total_revenue_dict:.2f}")