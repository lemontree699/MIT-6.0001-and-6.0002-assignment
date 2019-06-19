# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations = []
    # 如果只含有一个字符
    if len(sequence) == 1:
        permutations.append(sequence)
    # 如果含有多个字符
    else:
        # 首先获得去掉第一个字符的子串的全排列
        sub_permutations = get_permutations(sequence[1:])
        # 在每一个子串的全排列中，将第一个字符插入其中
        for item in sub_permutations:
            for pos in range(len(item) + 1):
                # 插入第一个字符的位置共有len(item)+1个
                new_str = item[pos:] + sequence[:1] + item[:pos]
                permutations.append(new_str)
    return permutations

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'xyz'
    print('Input:', example_input)
    print('Expected Output:', ['zyx', 'yxz', 'xzy', 'yzx', 'zxy', 'xyz'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'qwe'
    print('Input:', example_input)
    print('Expected Output:', ['ewq', 'wqe', 'qew', 'weq', 'eqw', 'qwe'])
    print('Actual Output:', get_permutations(example_input))

    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

