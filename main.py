import random
import sympy


def main():
    p = int(input('p :'))
    q = int(input('q :'))
    n, e = make_public_key(p, q)
    print('n :', n)
    print('e :', e)


def make_public_key(p, q):
    n = p * q
    max_pq = max(p, q)
    lcm = sympy.lcm(p-1, q-1)
    e = random.randint(max_pq, lcm)
    a = 0
    while a != 1:
        e = e + 1
        a = sympy.gcd(e, lcm)
    return n, e


if __name__ == '__main__':
    main()
