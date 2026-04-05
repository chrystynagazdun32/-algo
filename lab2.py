print("введіть кількість прикладів:")
t = int(input())

print("введіть дані для кожного прикладу (N W H):")

for example_num in range(t):
    N, W, H = map(int, input().split())
    
    left = 1
    right = 1

    step = 1
    while True:
        cols = right // W
        rows = right // H
        if cols > 0 and rows > 0 and rows * cols >= N:
            break
        right = right + step
        step = step + step
    
    answer = right
    iterations = 0
    
    right = 1073741823
    
    while left <= right:
        mid = (left + right) // 2
        iterations += 1
        
        cols = mid // W
        rows = mid // H
        
        if cols > 0 and rows > 0 and rows * cols >= N:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(f"результат: {answer}")
    print(f"кількість ітерацій: {iterations}")
    print()

print("всі результати виведені.")