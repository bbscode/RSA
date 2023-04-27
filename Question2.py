from RSA import RSA
p = 23
q = 41
rsa = RSA(p, q)

message = "PARTY TOMORROW AT ME"

print("Co-prime with N = " + str(rsa.n) + ": " +
      str(rsa.get_coprimes(rsa.get_totient(rsa.n)))+"\n")

e1 = 31
e2 = 53
print("Original message: " + str(message))
print("e1 = " + str(e1))

rsa.set_e(e1)
string_array, number_array1 = rsa.encrypt(message)
print("Encrypted text array: " + str(string_array))
print("Encrypted number array: " + str(number_array1) + "\n")


print("e2 = " + str(e2))
rsa.set_e(e2)
string_array, number_array2 = rsa.encrypt(message)
print("Encrypted text array: " + str(string_array))
print("Encrypted number array: " + str(number_array2) + "\n")

s1, s2 = rsa.extended_euclidean_algorithm(e1, e2)
s1 = s1 % rsa.n
s2 = s2 % rsa.n

print("Bezout co-efficients : " + str(s1) + ", " + str(s2) + "\n")

test = rsa.convert_to_num(message)

print(test)
cma_array = []
for i in range(len(test)):
    temp1 = pow(test[i], s1*e1)
    temp2 = pow(test[i], s2*e2)
    temp3 = (temp1*temp2) % rsa.n
    cma_array.append(temp3)

print(rsa.convert_to_text(cma_array))
