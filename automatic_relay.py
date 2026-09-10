```python
# Automatic Relay Control using Python

print("=== Automatic Relay Control System ===")

# Set temperature limit
temperature_limit = 30

# Get sensor value from user
temperature = float(input("Enter temperature in °C: "))

# Automatic relay control
if temperature > temperature_limit:
    relay = "ON"
    print("Temperature is high.")
    print("Relay Status: ON")
    print("Fan/Load is turned ON automatically.")

else:
    relay = "OFF"
    print("Temperature is normal.")
    print("Relay Status: OFF")
    print("Fan/Load is turned OFF automatically.")

print("=== System Completed ===")
```
