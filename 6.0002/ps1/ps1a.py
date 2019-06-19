###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: myz
# Collaborators:
# Time: 2019.05.27

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    with open(filename) as f:
    	lines = f.readlines()  # 逐行读取txt文件，返回的lines为一个list
    	dictionary = {}
    	# lines的每一项都是一个包含奶牛名称和重量的字符串，通过split函数将他们分开后传入dictionary中
    	for i in range(len(lines)):
    		lines[i] = lines[i].replace('\n', '')
    		temp = lines[i].split(',')
    		dictionary[temp[0]] = int(temp[1])
    	# print(dictionary)
    return dictionary

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    # 将字典按照value值的大小排序
    sorted_by_weight = sorted(cows.items(), key = lambda item:item[1], reverse = True)
    # print(sorted_by_weight)
    transport = []  # 用来存储最终的运输方案

    transported = []   # 用于判断奶牛是否已经被运输
    for _ in range(len(sorted_by_weight)):
    	transported.append(0)

    while all(transported) == 0:  # 如果所有的奶牛都已经被运输，则退出循环
        transport_once = []  # 存储每一次运输的奶牛的名字
        already_token = 0  # 目前已经运输的奶牛的重量
        for i in range(len(sorted_by_weight)):
            if already_token + sorted_by_weight[i][1] <= limit and transported[i] == 0:
                already_token += sorted_by_weight[i][1]
                transported[i] = 1  # 代表这只牛已经被运输
                # print(sorted_by_weight[i][0])
                transport_once.append(sorted_by_weight[i][0])
        transport.append(transport_once)
    # print(transport)
    return transport


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    valid_transport = []
    partitions = get_partitions(cows)
    for partition in partitions:  # partition是某种分配的方式
    	flag = 1  # 判断该种分配方式是否符合重量规范
    	for transport_once in partition:  # transport_once是每种分配方式中运输一趟搭载的奶牛
    		total_weight = 0  # 计算每趟运输总重量
    		for cow in transport_once:
    			total_weight += cows[cow]
    			# total_weight += cow
    		if total_weight > limit:  # 如果重量大于限制，则不行
    			flag = 0
    	if flag:  # 如果符合条件，则存储这种分配方案
    	    valid_transport.append(partition)
    # valid_transport里的元素仍是列表，要选出其中长度最短的列表，其长度就是最少的旅途数
    return min(valid_transport, key = len)
        

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    
    cows = load_cows(r"./ps1_cow_data.txt")

    # 贪心算法花费的时间
    start = time.time()
    greedy = greedy_cow_transport(cows)
    end = time.time()
    print("greedy =", end - start)
    print("number of trips:", len(greedy))
    # print(greedy)
 
    # 暴力搜索所花费的时间
    start = time.time()
    brute = brute_force_cow_transport(cows)
    end = time.time()
    print("brute =", end - start)
    print("number of trips:", len(brute))
    # print(brute)


compare_cow_transport_algorithms()