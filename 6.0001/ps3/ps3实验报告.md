# <center>problem set 3 实验报告</center>

<center>16337183 孟衍璋</center>



&emsp;&emsp;这次实验实现的游戏规则大致为：玩家会拿到一些字母，他们根据这些字母构造一个或多个单词，每个有效单词根据其长度与字母计算得分。

&emsp;&emsp;要完成这个游戏，需要实现几个函数接口，分别如下：

`load_words()`:从txt文件中读取单词存入列表。

`get_frequency_dict(sequence)`：返回一个字典，对应每个字母出现的次数。

`get_word_score(word, n)`：获取单词的分数。

`display_hand(hand)`：显示当前手牌。

`deal_hand(n)`：随机生成手牌。

`update_hand(hand, word)`：根据输入的单词更新手牌。

`is_valid_word(word, hand, word_list)`：判断输入的单词是否合法。

`calculate_handlen(hand)`：计算手牌中还有几个字母。

`play_hand(hand, word_list)`：进行一轮游戏。

`substitute_hand(hand, letter)`：将手牌中的一个字母替换为未出现过的字母。

`play_game(word_list)`：用户界面，将步骤联系起来。



&emsp;&emsp;有些函数之前已经实现，所以只需实现以下函数：

#### get_word_score(word, n)

```python
word = word.lower()
pos = word.find('*')

temp1 = 0
for i in range(len(word)):
    if i == pos:
        pass
    else:
        temp1 += SCRABBLE_LETTER_VALUES[word[i]]
temp2 = 7 * len(word) - 3 * (n - len(word))
if temp2 < 0:
    temp2 = 1
score = temp1 * temp2
return score
```
&emsp;&emsp;因为之后的需求中要加入通配符，所以里面有考虑通配符的情况。



#### update_hand(hand, word)

```python
word = word.lower()
    new_hand = hand.copy()
    for letter in word:
        # 如果字母不在hand中或者个数不足，就忽略这种情况，其余情况还是会扣除hand
        if (letter in new_hand == 0) or (new_hand[letter] == 0):
            pass
        else:
            new_hand[letter] -= 1
    return new_hand
```



#### is_valid_word(word, hand, word_list)

```python
word = word.lower()
    new_hand = hand.copy()

    # 如果单词中含有通配符
    pos = word.find('*')
    if pos != -1:
        for wildcards in VOWELS:
            flag = 1
            new_word = word.replace('*', wildcards)
            # 如果单词不在单词库中，返回False
            if (new_word in word_list) == 0:
                flag = 0
            # 如果字母不在hand中，返回False
            for i in range(len(new_word)):
                if i == pos:
                    pass
                elif (new_word[i] in hand) == 0:
                    flag = 0
            # 如果字母的使用次数超过hand中有的个数，返回False
            for i in range(len(new_word)):
                if i == pos:
                    new_hand['*'] -= 1
                else:
                    new_hand[new_word[i]] -= 1
            for i in new_hand:
                if new_hand[i] < 0:
                    flag = 0
            if flag:
                return True
            # 每次循环new_hand需要更新，不然会持续减，导致结果错误
            new_hand = hand.copy()  

    # 如果单词不在单词库中，返回False
    if (word in word_list) == 0:
        return False
    # 如果字母不在hand中，返回False
    for letter in word:
        if (letter in hand) == 0:
            return False
    # 如果字母的使用次数超过hand中有的个数，返回False
    for letter in word:
        new_hand[letter] -= 1
    for i in new_hand:
        if new_hand[i] < 0:
            return False
    return True
```

&emsp;&emsp;这个函数的实现中，需要考虑两种情况：有通配符和无通配符。在实现过程中最开始我忽略掉了一个地方，在通配符遍历元音的时候，忘记重置`hand`的数量，导致结果一直不正确，后来输出`hand`查看之后才知道问题出在了什么地方。

&emsp;&emsp;这个时候运行给出的`test_ps3.py`程序就可以得到以下结果：

![1556281747346](C:\Users\myz\AppData\Roaming\Typora\typora-user-images\1556281747346.png)

&emsp;&emsp;说明以上实现是正确的。



&emsp;&emsp;接下来就要开始实现玩游戏的功能。

#### calculate_handlen(hand)

```python
n = 0
    for letter in hand:
        n += hand[letter]
    return n
```



#### play_hand(hand, word_list)

```python
total_score = 0
    while(1):
        print('Current Hand:', end = ' ')
        display_hand(hand)
        word = input('Enter word, or "!!" to indicate that you are finished: ')
        if word == '!!':
            print('Total score:', total_score, 'points')
            break
        else:
            if is_valid_word(word, hand, word_list):
                score = get_word_score(word, calculate_handlen(hand))
                total_score += score
                print('\"{}\" earned {} points. Total: {} points\n'.format(word, score, total_score))
            else:
                print('That is not a valid word. Please choose another word.\n')
            hand = update_hand(hand, word)
        if calculate_handlen(hand) == 0:
            print('Ran out of letters. Total score:', total_score, 'points\n')
            break
        
    return total_score
```



#### substitute_hand(hand, letter)

```python
new_hand = hand.copy()
    num = new_hand.pop(letter)
    letters = string.ascii_lowercase
    for i in hand:
        letters = letters.replace(i, '')
    new_letter = random.choice(letters)
    new_hand[new_letter] = num
    return new_hand
```



#### play_game(word_list)

```python
num_of_hands = int(input('Enter total number of hands: '))
    total_score = 0
    flag_sub = 1
    flag_re = 1
    for _ in range(num_of_hands):
        hand = deal_hand(HAND_SIZE)
        new_hand = hand.copy()
        if flag_sub:
            print('Current hand:', end = ' ')
            display_hand(hand)

        # 询问是否替换字符，且只能替换一次
        if flag_sub:
            sub = input('Would you like to substitute a letter?(Please enter \'yes\' or \'no\'): ')
            if sub == 'yes':
                letter = input('Which letter would you like to replace: ')
                hand = substitute_hand(hand, letter)
                flag_sub = 0

        new_score = play_hand(hand, word_list)
        total_score += new_score
        print('----------')

        # 询问是否replay
        if flag_re:
            re = input('Would you like to replay the hand?(Please enter \'yes\' or \'no\'): ')
            if re == 'yes':
                total_score -= new_score
                total_score += play_hand(new_hand, word_list)
                print('----------')
                flag_re = 0
    print('Total score over all hands: ', total_score)
```



&emsp;&emsp;至此，整个游戏就已经实现了。试玩结果如下：

![1556282161350](C:\Users\myz\AppData\Roaming\Typora\typora-user-images\1556282161350.png)

![1556282492038](C:\Users\myz\AppData\Roaming\Typora\typora-user-images\1556282492038.png)

