# Automatic Relay Control using Python

print("=== Automatic Relay Control System ===")

temperature_limit = 30

temperature = float(input("Enter temperature in °C: "))

if temperature > temperature_limit:
    print("Temperature is high.")
    print("Relay Status: ON")
    print("Fan/Load is turned ON automatically.")
else:
    print("Temperature is normal.")
    print("Relay Status: OFF")
    print("Fan/Load is turned OFF automatically.")

print("=== System Completed ===")
