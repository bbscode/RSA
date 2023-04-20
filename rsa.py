import math
q = 11
p = 13
n = q*p
print("q = " + str(q))
print("p = " + str(p))
print("n = " + str(n))
print()
message = "MEET AT NINE"
print("Message to encrypt: " + message)
print()
string_array = [x for x in message]
ascii_array = [ord(x) for x in message]
print("Message arrays:")
print(string_array)
print(ascii_array)
print()
phi = 10*12
print("Totient function for n: " + str(phi))
coprimes = [x for x in range(120)if math.gcd(x, 120) == 1]
print(coprimes)
