class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        elif n == 0:
            return 1

        power_sign = n/abs(n)

        simple_res = 1

        i = abs(n)

        while i > 0:
            if i%2 == 1:
                simple_res *= x
                i-=1
            x = x * x
            i//=2

        if power_sign > 0:
            return simple_res
        else: 
            return  (1 / simple_res)