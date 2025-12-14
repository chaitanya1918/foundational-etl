import csv
import random
from faker import Faker
from uuid import uuid4

fake = Faker()

DATE_FORMATS = [
    "%Y-%m-%d",        # YYYY-MM-DD
    "%m/%d/%Y",        # MM/DD/YYYY
    "%B %d, %Y"        # Month D, YYYY
]

def generate_raw_users(output_file="raw_users.csv", total_rows=10_000):
    emails = []

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "user_id",
            "name",
            "email",
            "phone_number",
            "address",
            "signup_date"
        ])

        for i in range(total_rows):
            user_id = str(uuid4())
            name = fake.name()

            # Introduce duplicate emails (~5%)
            if i % 20 == 0 and emails:
                email = random.choice(emails)
            else:
                email = fake.email()
                emails.append(email)

            # Introduce missing phone numbers (~5%)
            phone_number = fake.phone_number()
            if i % 20 == 1:
                phone_number = ""

            address = fake.address().replace("\n", ", ")

            signup_date = fake.date_object()
            signup_date = signup_date.strftime(
                random.choice(DATE_FORMATS)
            )

            writer.writerow([
                user_id,
                name,
                email,
                phone_number,
                address,
                signup_date
            ])

    print(f"Generated {total_rows} records in {output_file}")
