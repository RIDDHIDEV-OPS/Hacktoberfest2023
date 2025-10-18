class Solution:
    def tribonacci(self, n: int) -> int:
        #Base case
        if n==0: 
            return 0
        if n==1 or n==2:
            return 1
        #Recursive Case
        return self.tribonacci(n-1)+ self.tribonacci(n-2)+self.tribonacci(n-3)
