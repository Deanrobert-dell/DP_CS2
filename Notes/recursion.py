"""number = 5
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(factorial)

def factor(num):
    if num == 1: return 1
    return num * factor(num - 1)

print(factor(5))"""



number = 500
nums = [1,1]
for i in range(1, number):
    nums.append(nums[i] + nums[i-1])

print(nums)
