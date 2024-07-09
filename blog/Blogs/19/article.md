# 递推和递归

## 前言

观点来自如下题目（洛谷），均为本人主观臆断，仅供参考。

* P1255
* P1044
* P1028
* P1464
* P2437

## 一个平凡的递归

最简单的递归最起码要确定这些事情：

* 如何把答案传递出来
* 递归终止的条件是什么
* 递归的子问题分割方式

比如这题数楼梯的题目：

> 楼梯有 $N$ 阶，上楼可以一步上一阶，也可以一步上二阶。
> 编一个程序，计算共有多少种不同的走法。

对于第 $i$ 步楼梯而言，它们可以来由第$i-1$级（跨一步）和$i-2$级（跨两步）楼梯直接到达。 因此，第$i$步楼梯的到达方法实际上是第$i-1$级和$i-2$级楼梯格子的到达方法的和。

目标 $N$ 的到达方法等于$N-1$级和$N-2$级的到达方法之和，其中$N-1$的到达方法等于$N-2$级和$N-3$级的到达方法之和.....

如此演算下去，最终会推到第1级和第2级楼梯的到达方法，这个时候问题规模已经足够小，我们可以人工算出到达第一级只有一种方法，到达第二级有两种方法。

把这个过程用递归描述出来，就是这样：

```python
n = int(input())


def recursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    #终止条件

    return recursive(n - 1) + recursive(n - 2) 
    #问题的分割方式，传递答案的方式


print(recursive(n))
```

## 记忆强化版递归

介绍完了一个平凡的递归，我们来思考一些一个问题，它够好吗，这里我还是拿那个数楼梯的例子，我们可以看看计算第10级楼梯方法的时候程序会经历什么：

![](data:image/webp;base64,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)

你可以看到，例如$f(8)$、$f(7)$等等被计算了很多次，这将会给我们的程序带来很大的时间复杂度的负面效应。

这里，我们可以这样改进一下这个递归代码结构，那就是，我们首次计算完$f(k)$之后就把$f(k)$的值直接存起来，下次需要$f(k)$的时候就不用反复计算它的值了。在Python里面用字典实现这样一个逻辑再合适不过了。请看代码：

```python
n = int(input())
memory = {}

def recursive(n):
    if n in memory:
        return memory[n]
    if n == 1:
        return 1
    if n == 2:
        return 2

    memory[n] = recursive(n - 1) + recursive(n - 2)
    return memory[n]

print(recursive(n))
```
原来代码计算 $N=36$ 的楼梯问题用时2.036秒，改进后用时仅1.1e-04秒。

## 递推

还是那个数楼梯的例子，让我们把上一章节的memory字典打印出来看看

{1: 1, 2: 2, 3: 3, 4: 5, 5: 8, 6: 13, 7: 21, 8: 34, 9: 55, 10: 89}

你应该会发现规律：第三项是前两项的和，第四项是第二项和第三项的和。我们其实可以用这个规律来不断从前向后（递归是从后向前）的递推后面的式子，这样速度会更快，代码如下：


```python
n = int(input())

method = [1,2]

for _ in range(max(0,n-2)):
    method.append(method[-1] + method [-2])


print(method[-1])
```

这次$N=36$ 的楼梯问题用时5.41e-05秒，更快了。


## 一些总结

一般使用递推式解决问题的过程是：首先写出递归代码，然后打印出来前几项找找规律，如果能发现递推规律，那么运用这个递推规律将会使我们的程序非常高效。一般发现递推的规律需要基于细致的观察，比如洛谷的P1028。

## 时间复杂度计算

### 拓展递归法
  
我们首先可以写一下这个

$$ T(n) = n \quad (n = 1,2)$$
$$ T(n) = T(n-1) + T(n-2) \quad (n >2)$$

由第一个式子可以得到$T(1) = 1$, $T(2) = 2$ 先保留备用

把第二个式子不断带入自己，就像下面这样

$$T(n) = T(n-1) + T(n-2)$$

$$T(n) = T(n-2) + T(n-3) + T(n-3) + T(n-4)$$

$$T(n) = ...+T(n-(n-1))$$

可以看到每一次代入后，项的个数都会变为原来的两倍

$T(n-1)$展开为$T(n-(n-1)) = T(1)$需要 $n-1-1 = n-2$ 次

$T(n-1)$展开为$T(n-(n-2)) = T(2)$需要 $n-2-1 = n-3$ 次

总共的项数大约为$2^{(n-3)} + 2^{(n-2)}$ 

所以时间复杂度为 $O(2^n)$

或者，可以把整个过程想象成大致形成一个这样的二叉树（以展开$T(n-1)$为例）


```shell
              T(n-1)
           /        \
      T(n-1)      T(n-2)
       /   \        /   \
  T(n-2) T(n-3) T(n-3) T(n-4)
   /  \     /  \    /  \    /  \
T(n-3) ...   ...   ...   ... T(1)
```

这棵树的高度为$n-2$，每一层的节点个数都是上一层的两倍。


# refs

[算法设计与分析 - 绪论](https://blog.csdn.net/qq_44958172/article/details/104488989)

[W211qwqq2  【数据结构】递归算法的时间复杂度分析](https://blog.csdn.net/qq_45888298/article/details/108563959#:~:text=对递归算法时间复杂度的分析，关键是根据递归过程建立递推关系式，然后求解这个递推关系式%E3%80%82%20通常用扩展递归技术,将递推关系式中等式右边的项根据递推式替换%20，这称为扩展，扩展后的项被再此扩展，依次下去，就会得到一个求和表达式%E3%80%82)



_The end 如有错误欢迎指出_


