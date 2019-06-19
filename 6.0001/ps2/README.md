# hangman_game

Hangman game的介绍与规则：https://en.wikipedia.org/wiki/Hangman_(game)

我实现了这个游戏，words.txt是单词库，计算机会在其中随机选择一个单词。玩家可以与计算机交互，每次猜一个字母，当猜中整个单词时，玩家胜利；当错误次数超过6次时，玩家失败。

玩家如果输入的不是字母，或者输入了之前猜过的字母，会触发警告，玩家共有3次触发警告的机会。若超过了这个数目，直接扣除一次猜字母的机会。

游戏共有两种模式：有提示（hangman）与无提示（hangman_with_hints），可以在函数中进行切换：
```python
if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

```

若选择有提示的模式，在输入字母的时候，可以选择输入星号（\*）。便可以得到单词库中与你当前输入匹配的候选词。
