# 在由0 ~ 9中取任意五個不重複數字所組成的五位數中，判斷其最大、最小值分別為何，且判斷這些五位數中是否有質數，質數為何?
# Ex: 用random方法從0~9中選出五個數，將其生成所有可以排成五位數數字的數列
# 隨機抓出1 2 3 6 8
# 21386, 21368, 21836, 21863, 21638, 21683, 23186, 23168, 23816, 23861, 23618, 
# 23681, 28136, 28163, 28316, 28361, 28613, 28631, 26138, 26183, 26318, 26381, 26813, 26831, 12386, 12368, 12836, 12863, 12638, 12683, 13286, 13268, 13826, 13862, 13628, 13682, 18236, 18263, 18326, 18362, 18623, 18632, 16238, 16283, 16328, 16382, 16823, 16832, 32186, 32168, 32816, 32861, 32618, 32681, 31286, 31268, 31826, 31862, 31628, 31682, 38216, 38261, 38126, 38162, 38621, 38612, 36218, 36281, 36128, 36182, 36821, 36812, 82136, 82163, 82316, 82361, 82613, 82631, 81236, 81263, 81326, 81362, 81623, 81632, 83216, 83261, 83126, 83162, 83621, 83612, 86213, 86231, 86123, 86132, 86321, 86312, 62138, 62183, 62318, 62381, 62813, 62831, 61238, 61283, 61328, 61382, 61823, 61832, 63218, 63281, 63128, 63182, 63821, 63812, 68213, 68231, 68123, 68132, 68321, 68312

# 輸出:
# 最大值: 86321, 最小值: 12368
# 質數是[21863, 21683, 28163, 28631, 26183, 26813, 16823, 38261, 36821, 82163, 82361, 82613, 83621, 61283, 63281, 68213]

import random

# 遞迴生成排列组合
def generate_five_digit_list(arr, n):
    if n == 0:
        return [''.join(arr)]
    five_digit_list = []
    for i in range(n):
        arr[i], arr[n - 1] = arr[n - 1], arr[i]
        five_digit_list.extend(generate_five_digit_list(arr, n - 1))
        arr[i], arr[n - 1] = arr[n - 1], arr[i]
    return five_digit_list

# 檢查一個數是否為質數
def is_prime(number):
    test = 0
    if number > 1:
        for i in range(1, number):
            if test > 2:
                return False
            if number % i == 0:
                test = test + 1
    return True

# 從0到9選五個不重複的數字
selected_numbers = random.sample(range(10), 5)

five_digit_list = generate_five_digit_list(list(map(str, selected_numbers)), 5)

five_digit_list = [int(p) for p in five_digit_list]

max = max(five_digit_list)
min = min(five_digit_list)

prime_list = []
for perm in five_digit_list:
    if (is_prime(perm)) == True:
        prime_list.append(perm)

print(f"最大值: {max}, 最小值: {min}")
print("質數:", prime_list)