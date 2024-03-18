# Algorithm Day1 24.3.18 - Sortings 

## Problems today
### AC

*   simulation - P1042 [NOIP2003 普及组] 乒乓球 
*   simulation - P2670 [NOIP2015 普及组] 扫雷游戏
*   simulation - P1786 帮贡排序

### Non-AC

* nope

## Common sorting codes in Python 

### Single sort factors

```python
my_list = ['apple', 'banana', 'cherry', 'date']
sorted_list = sorted(my_list, key=x:x)
```

### Multi sort factors

```python
sort_by_level = lambda p: (p.pri, -int(p.exp), p.sn)

# p.pri, int(p.exp), p.sn are all numbers 
# default in ascending order, use a negative sign to descend
persons = sorted(persons, key=sort_by_level)
```


### sort in an interval

```python
persons[unmoved_index:] = sorted(persons[unmoved_index:], key=sort_by_banggong)
```



## Python Explore


```python
items = [1, 2, 3, 4]

for item in items:
    item = 0

print(items)
# out: [1, 2, 3, 4] 
# this proves the item here is read-only
```