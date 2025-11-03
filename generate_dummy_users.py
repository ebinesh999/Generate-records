import csv
import random
from faker import Faker

fake = Faker('en_IN')  # Indian-style names and cities
rows = 10_000_000  # 1 crore
output_file = "dummy_users.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Age", "City", "Email"])

    for i in range(1, rows + 1):
        name = fake.name()
        age = random.randint(18, 65)
        city = fake.city()
        email = fake.email()
        writer.writerow([i, name, age, city, email])

print(f"✅ Done! File saved as {output_file}")
