class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        k = []
        for i in range(1,n+1):
            if i % 5 == 0 and i % 3 == 0:
                k.append('FizzBuzz')
            elif i % 5 == 0:
                k.append('Buzz')
            elif i % 3 == 0:
                k.append('Fizz')
            else:
                k.append(str(i))
        return k
        