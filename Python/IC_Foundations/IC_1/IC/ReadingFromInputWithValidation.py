def convert_fahr(temperature):
    return (temperature * 9/5) + 32



while True:
    try:
        temperature_c = float(input("Enter the temperature to convert: "))
        break
    except ValueError:
        print("Error")
temperature_f = convert_fahr(temperature_c)

print(f"{temperature_f:.1f}")




