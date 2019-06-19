###########################
# 6.0002 Problem Set 1b: Space Change
# Name: myz
# Collaborators:
# Time: 2019.05.27
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    
    list(egg_weights).sort() # 按照重量给蛋排序
    dictionary = {0:0}  # 字典中的key表示需要的重量，value为对应的重量需要的蛋数目
    for weight in range(1, target_weight + 1):
        dictionary[weight] = float('inf')
        for egg in egg_weights:
            if egg <= weight:  # 如果蛋的重量小于当前需要的重量，则可以将其加入
                dictionary[weight] = min(dictionary[weight], dictionary[weight - egg] + 1)
    if dictionary[target_weight] == float('inf'):
        return -1
    else:
        return dictionary[target_weight]


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()