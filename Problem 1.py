class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        TLE

        flag = False
        if divisor < 0 and not dividend < 0: 
            divisor *= -1
            flag = True
        if dividend < 0 and not divisor < 0:
            dividend *= -1
            flag = True
        if dividend < 0 and divisor < 0:
            flag = False
            dividend *= -1
            divisor *= -1

        total = divisor
        count = 0
    
        while total <= dividend:
            count += 1
            total += divisor
        
        return count if not flag else count*-1"""
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Clamp to max 32-bit integer
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        result = 0
        ldividend = abs(dividend)
        ldivisor = abs(divisor)

        while ldividend >= ldivisor:
            count = 1
            while (ldivisor <<count) <= ldividend: 
                # ldivisor = ldivisor << 1
                count += 1
            
            count -= 1
            ldividend = ldividend - (ldivisor << count)
            result += 1 << count
            # print(ldividend, ldivisor, count)
        
        return sign*result


