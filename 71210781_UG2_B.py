import time
def deret_ajaib(n):
    if n <= 5:
        return n
    else:
        return deret_ajaib(n-2) + deret_ajaib(n//2)

n = 7
start = time.time()
hasil = deret_ajaib(n)
end = time.time()

print("Hasil :",hasil)
print("Duration :",end-start)