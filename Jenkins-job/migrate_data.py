# migrate_data.py
import logging

def migrate_data(source_db, destination_db):
    logging.info(f"Migrating data from {source_db} to {destination_db}.")
    # Simulate data migration
    print(f"Data migrated from {source_db} to {destination_db}.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    source_db = "source_database"
    destination_db = "destination_database"
    migrate_data(source_db, destination_db)
