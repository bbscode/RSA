import math


class RSA:
    # Initializes the variables
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.totient = self.get_totient(self.n)
        self.e = None
        self.d = None

    # Calculates d
    def calculate_d(self):
        return self.extended_euclidean_algorithm(self.totient, self.e)[1] % self.totient

    # Allows us to set e and calculate d
    def set_e(self, e):
        self.e = e
        self.d = self.calculate_d()

    # Computes x and y using the Extended Euclidean Algorithm

    def extended_euclidean_algorithm(self, a, b):
        x1, x2, y1, y2 = 1, 0, 0, 1
        while b != 0:
            q = a // b
            r = a % b
            x = x1 - q * x2
            y = y1 - q * y2
            a, b = b, r
            x1, x2 = x2, x
            y1, y2 = y2, y

        return x1, y1

    # Converts a Integer array into a String array

    def convert_to_text(self, message):
        string_array = [chr(x) for x in message]
        return string_array

    # Converts a String array into a Integer array
    def convert_to_num(self, message):
        ascii_array = [ord(x) for x in message]
        return ascii_array

    # Returns all Integers co-primes with n that are less than n
    def get_coprimes(self, n):
        return ([x for x in range(n) if math.gcd(x, n) == 1])

    # Returns the totient value
    def get_totient(self, n):
        return (self.p - 1) * (self.q - 1)

    # Returns both the numerical and text encrypted arrays
    def encrypt(self, message):
        encrypt_array = [(x**self.e) %
                         self.n for x in self.convert_to_num(message)]
        return (self.convert_to_text(encrypt_array), encrypt_array)

    # Returns both the numerical and text decrypted arrays
    def decrypt(self, encrypt_array):
        decrypt_array = [(x**self.d) % self.n for x in encrypt_array]
        return (self.convert_to_text(decrypt_array), decrypt_array)

    def common_modulus_attack(n, e1, e2, c1, c2):
        rsa = RSA(1, 1)  # create a dummy object to use its functions
        s1, s2 = rsa.extended_euclidean_algorithm(e1, e2)
        if s1 < 0:
            s1 = -s1
            c1 = rsa.extended_euclidean_algorithm(c1, n)[1]
        elif s2 < 0:
            s2 = -s2
            c2 = rsa.extended_euclidean_algorithm(c2, n)[1]
        p = pow(c1, s1, n)
        q = pow(c2, s2, n)
        m = pow((p*q) % n, 1, n)  # compute the message
        return rsa.convert_to_text(m)
