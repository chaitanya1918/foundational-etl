import csv
from datetime import datetime

DATE_FORMATS = [
    "%Y-%m-%d",        # YYYY-MM-DD
    "%m/%d/%Y",        # MM/DD/YYYY
    "%B %d, %Y"        # Month D, YYYY
]

def extract(csv_path):
    """
    Read entire CSV file and return list of dictionaries
    """
    with open(csv_path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def _parse_date(date_str):
    """
    Convert multiple date formats into YYYY-MM-DD
    """
    if not date_str:
        return None

    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return None


def transform(records):
    """
    Clean data, remove duplicate emails, standardize fields
    """
    cleaned_records = []
    seen_emails = set()

    for row in records:
        email = row["email"].strip().lower()

        # Remove duplicates based on email
        if email in seen_emails:
            continue
        seen_emails.add(email)

        cleaned_records.append({
            "user_id": row["user_id"].strip(),
            "name": row["name"].strip(),
            "email": email,
            "phone_number": row["phone_number"].strip() or None,
            "address": row["address"].strip(),
            "signup_date": _parse_date(row["signup_date"])
        })

    return cleaned_records


def write_csv(records, output_file="clean_users.csv"):
    """
    Write transformed records to CSV
    """
    if not records:
        print("No records to write")
        return

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

    print(f"Transformed data written to {output_file}")
