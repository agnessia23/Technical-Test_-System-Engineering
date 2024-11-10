def generate_arithmetic_series(N):
    a = 2 
    d = 3  
    series = [a + d * i for i in range(N)]
    return series

N = 4
print(generate_arithmetic_series(N)) 