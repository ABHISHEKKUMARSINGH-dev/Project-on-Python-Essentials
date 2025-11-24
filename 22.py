def extended_gcd(a, b):
    """
    Helper for mod_inverse: Finds g, x, y such that a*x + b*y = gcd(a, b)
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    """
    Helper for CRT: Finds x such that (a * x) % m = 1
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        # Inverse doesn't exist
        return None
    else:
        return x % m

def crt(remainders, moduli):
    """
    Solves a system of congruences x ≡ remainders[i] mod moduli[i]
    using the Chinese Remainder Theorem.
    
    Args:
        remainders (list): A list of remainders [r1, r2, ...]
        moduli (list): A list of corresponding moduli [m1, m2, ...]
                       Assumed to be pairwise coprime.
    """
    if len(remainders) != len(moduli):
        raise ValueError("Input lists must have the same length")

    N = 1
    for m in moduli:
        N *= m

    total = 0
    for i in range(len(moduli)):
        r_i = remainders[i]
        m_i = moduli[i]
        
        # N_i = N / m_i
        N_i = N // m_i
        
        # Find the modular inverse of N_i modulo m_i
        y_i = mod_inverse(N_i, m_i)
        
        if y_i is None:
            # This would happen if moduli are not pairwise coprime
            raise ValueError("Moduli are not pairwise coprime, inverse not found.")

        total += r_i * N_i * y_i

    # The final solution is total % N
    return total % N