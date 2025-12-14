# Foundational ETL Pipeline

This project implements a foundational ETL (Extract, Transform, Load) pipeline using Python and SQLite.

## Overview
- Generates 10,000 synthetic user records using the Faker library
- Introduces intentional data quality issues (duplicate emails, missing values, inconsistent dates)
- Cleans and deduplicates data
- Loads cleaned data into a SQLite database with enforced constraints
- Provides a CLI to run each ETL step or the full pipeline

## Project Structure
- etl/data_generator.py – Data generation
- etl/pipeline.py – Extract and transform logic
- etl/database.py – SQLite loading
- cli.py – Command-line interface

## How to Run
```bash
pip install faker
python cli.py full-pipeline
