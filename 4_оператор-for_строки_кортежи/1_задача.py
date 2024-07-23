start = int(input("\nВведите начало счета: "))
finish = int(input("Введите конец счета: "))
print("\nРезкльтат интервала между счетами с циклом for: ")

for i in range(start, finish+1):
    print("\t - ", i)
    
print("\nРезкльтат интервала между счетами с циклом while: ")
while start != finish:
    print("\t-",start)
    if start < finish:
        start = start + 1
    if start > finish:
        start = start - 1