def make_factorial_table(max_n:int,mod:int) -> list[int]:
    """任意素数に対してmax_nまでの階乗のテーブルを作成する関数, O(max_n)"""
    fact : list[int] = [0]*(max_n+1)
    fact[0] = fact[1] = 1 #0! = 1
    for i in range(2,max_n+1):
        fact[i] = (fact[i-1] * i) % mod
    return fact

def make_invFactorial_table(max_n:int,mod:int) -> list[int]:
    """任意素数に対してmax_nまでの逆階乗のテーブルを作成する関数, O(max_n)"""
    inv : list[int] = [0]*(max_n+1)
    fact_inv : list[int] = [0]*(max_n+1)
    inv[1] = 1
    fact_inv[0] = fact_inv[1] = 1
    for i in range(2,max_n+1):
        inv[i] = mod - inv[mod % i] * (mod//i) % mod
        fact_inv[i] = (fact_inv[i-1] * inv[i]) % mod
    return fact_inv

def make_factorial_and_invFactorial_table(max_n:int,mod:int) -> tuple[list[int],list[int]]:
    """任意素数に対してmax_nまでの階乗・逆階乗のテーブルを作成する関数, 別々に作るより効率がいい。
    max_n < mod を仮定する。
    O(max_n + log mod)"""
    fact : list[int] = [0]*(max_n+1)
    fact_inv : list[int] = [0]*(max_n+1)
    fact[0] = fact[1] = 1
    fact_inv[0] = fact_inv[1] = 1
    for i in range(2,max_n+1):
        fact[i] = (fact[i-1]*i) % mod
    fact_inv[max_n] = pow(fact[max_n],mod-2,mod)

    for i in range(max_n,1,-1):
        fact_inv[i-1] = (fact_inv[i]*i) % mod

    return (fact,fact_inv)