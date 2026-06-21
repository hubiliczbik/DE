def is_ipv4(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        number = int(part)
        if number < 0 or number > 255:
            return False
        if part[0] == "0" and len(part) > 1:
            return False
    return True

print(is_ipv4("192.168.1.1"))
print(is_ipv4("0.0.0.0"))
print(is_ipv4("255.255.255.255"))
print(is_ipv4("256.0.0.0"))
print(is_ipv4("01.0.0.0.0"))
print(is_ipv4("1.2.3"))
