def fahrenheit_to_celsius(tempf):
    # (note -- floating point division, not integer division!)
    return (tempf - 32) * 5.0 / 9.0     

temperatures = [9, 14, 18, 12, -4, 16]

temperatures[0] = fahrenheit_to_celsius(temperatures[0])
temperatures[1] = fahrenheit_to_celsius(temperatures[1])
temperatures[2] = fahrenheit_to_celsius(temperatures[2])
temperatures[3] = fahrenheit_to_celsius(temperatures[3])
temperatures[4] = fahrenheit_to_celsius(temperatures[4])
temperatures[5] = fahrenheit_to_celsius(temperatures[5])

print temperatures
