Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. 

Note that 1 does not map to any letters.

```python
phoneMap = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7' : 'pqrs', '8': 'tuv', '9':'wxyz'}
```


```python
class Solution:
    """
    pass
    
print(letter_combinations('2'))        
print(letter_combinations("28"))
```

```text
output:
['a', 'b', 'c']
['at', 'au', 'av', 'bt', 'bu', 'bv', 'ct', 'cu', 'cv']
```

