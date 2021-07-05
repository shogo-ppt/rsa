import sympy


def main():
    # n = int(input('long :'))
    n = 200  # 素数の桁数
    p1, p2 = make_prime(n)
    public_key, secret_key = generate_key(p1, p2)
    e, n = public_key
    d, n = secret_key
    public_key = e, n
    secret_key = d, n
    
    print(f'''
PUBLIC KEY:
e : {e}
n : {n}

SECRET KEY:
d : {d}
    ''')
    
    p_text = input('Input plain text :')
    p_int_list, enc_int, e_text = encrypt(p_text, public_key)
    
    print('\n---ENCRYPT---')
    print('\nEncrypted text:', e_text)

    enc_int_list, dec_int, dec_text = decrypt(e_text, secret_key)

    print('\n---DECRYPT---')
    print('\ndecrypted text:', dec_text)


def make_prime(n):
    p1 = sympy.randprime(pow(10, n-1), pow(10, n))
    p2 = sympy.randprime(pow(10, n-1), pow(10, n))
    
    while p1 == p2:
        p2 = sympy.randprime(pow(10, n-1), pow(10, n))

    return p1, p2


def generate_key(p, q):
    n = p * q
    lcm = sympy.lcm(p-1, q-1)
    e = sympy.randprime(max(p, q) + 1, lcm)
    d = sympy.gcdex(e, lcm)
    d = (d[0]) % lcm
    return (e, n), (int(d), n)


def encrypt(p_text, public_key):
    e, n = public_key
    p_int_list = [(ord(char) - 32) for char in p_text]
    p_int = n_to_dec(p_int_list)
    c = pow(p_int, e, n)

    enc_int = dec_to_n(c)

    enc_text = ''.join(chr(i + 32) for i in enc_int)
    return p_int, enc_int, enc_text


def decrypt(enc_text, secret_key):
    d, n = secret_key
    enc_int_list = [(ord(char) - 32) for char in enc_text]
    d_int = n_to_dec(enc_int_list)
    p = pow(d_int, d, n)

    dec_int = dec_to_n(p)

    dec_text = ''.join(chr(i + 32) for i in dec_int)
    return enc_int_list, dec_int, dec_text


def n_to_dec(data):  # N進数 -> 10進数
    dec = 0
    l_list = len(data)
    for i in range(1, l_list + 1):
        dec += data[-i] * pow(95, i - 1)
    return dec


def dec_to_n(pe):  # 10進数 -> N進数
    pe_int = []
    while pe > 0:
        pe_int.append(pe % 95)
        pe = pe // 95
    pe_int.reverse()
    return pe_int


if __name__ == '__main__':
    main()
