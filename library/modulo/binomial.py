from ...library.math.factorial import make_factorial_and_invFactorial_table

fact : list[int]
inv_fact : list[int]

def init(n:int,mod:int) -> None:
    global fact,inv_fact
    fact,inv_fact = make_factorial_and_invFactorial_table(n,mod)

def calc_comb(n:int, k:int, mod:int) -> int:
    """二項係数nCkを素数modでO(1)で求める関数"""
    if n < k:
        return 0
    return ((fact[n] * inv_fact[k]) % mod * inv_fact[n-k]) % mod

def calc_comb_998244353(n:int,k:int) -> int:
    """二項係数nCkを998244353で割ったあまりをO(1)で求める関数"""
    if n < k:
        return 0
    MOD : int = 998244353
    return ((fact[n] * inv_fact[k]) % MOD * inv_fact[n-k]) % MOD