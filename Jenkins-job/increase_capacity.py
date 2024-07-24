# increase_capacity.py
import logging

def increase_capacity(service_name, amount):
    logging.info(f"Increasing capacity of {service_name} by {amount} units.")
    # Simulate increasing capacity
    print(f"Capacity of {service_name} increased by {amount} units.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    service_name = "example_service"
    amount = 10  # Increase capacity by 10 units
    increase_capacity(service_name, amount)
