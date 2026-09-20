from ...library.math.factorial import make_factorial_and_invFactorial_table

class CombinationClass:
    fact : list[int]; inv_fact : list[int]; max_n : int; mod : int
    def __init__(self,max_n:int,mod:int) -> None:
        self.max_n = max_n
        self.mod = mod
        self.fact = []
        self.inv_fact = []
        self.fact,self.inv_fact = make_factorial_and_invFactorial_table(max_n,mod)
        pass

    def calc_comb(self,n:int,k:int) -> int:
        """二項係数nCkを__init__で定義されたmodでO(1)で求める関数"""
        if n < k:
            return 0
        return ((self.fact[n] * self.inv_fact[k]) % self.mod * self.inv_fact[n-k]) % self.mod