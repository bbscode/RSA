from RSA import RSA
p = 11
q = 13
rsa = RSA(p, q)
print("Co-prime with N = " + str(rsa.n) + ": " +
      str(rsa.get_coprimes(rsa.get_totient(rsa.n)))+"\n")
rsa.set_e(7)
print("D = " + str(rsa.d) + "\n")
message = "MEET AT NINE"
string_array = [x for x in message]
number_array = rsa.convert_to_num(message)
print("Original message: " + str(message))
print("Message text array: " + str(string_array))
print("Message number array: " + str(number_array) + "\n")

string_array, number_array = rsa.encrypt(message)
print("Encrypted text array: " + str(string_array))
print("Encrypted number array: " + str(number_array) + "\n")

string_array, number_array = rsa.decrypt(number_array)
print("Decrypted text array: " + str(string_array))
print("Decrypted number array: " + str(number_array))
