import argparse
from etl.data_generator import generate_raw_users
from etl.pipeline import extract, transform, write_csv
from etl.database import init_db, load_data

def main():
    parser = argparse.ArgumentParser(description="Foundational ETL Pipeline")
    parser.add_argument(
        "command",
        choices=["generate", "extract", "transform", "load", "full-pipeline"]
    )

    args = parser.parse_args()

    if args.command == "generate":
        generate_raw_users()

    elif args.command == "extract":
        data = extract("raw_users.csv")
        print(f"Extracted {len(data)} records")

    elif args.command == "transform":
        data = extract("raw_users.csv")
        cleaned = transform(data)
        write_csv(cleaned)

    elif args.command == "load":
        data = extract("clean_users.csv")
        init_db()
        load_data(data)

    elif args.command == "full-pipeline":
        print("Starting full pipeline...")
        generate_raw_users()

        raw = extract("raw_users.csv")
        print(f"Extracted {len(raw)} records")

        cleaned = transform(raw)
        write_csv(cleaned)

        init_db()
        load_data(cleaned)

        print("Full pipeline completed successfully!")

if __name__ == "__main__":
    main()
