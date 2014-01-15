def fahrenheit_to_celsius(tempf):
    # (note -- floating point division, not integer division!)
    return (tempf - 32) * 5.0 / 9.0     

temperatures = [9, 14, 18, 12, -4, 16]

index = 0
while index < len(temperatures):
    temperatures[index] = fahrenheit_to_celsius(temperatures[index])
    index = index + 1

print temperatures
