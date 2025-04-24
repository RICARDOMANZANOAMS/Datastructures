class fibo:
    def __init__(self):
        pass

    def fib(self,n):
        if n<=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
fibobj=fibo()
print(fibobj.fib(10))
