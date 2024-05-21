# 算法考试例题复习

算法例题数量：15

## 分治

题型：填空，简答，算法填充题
考察内容

* 算法的伪代码描述
* 算法的时间复杂度

前情提要（如何求递推式的时间复杂度）:

如果一个分治递推式长这样：

$$ T(n)=\begin{cases}
c & n=1 \\
aT(\frac{n}{b}) + cn^{k} & n > 1 \\
\end{cases}$$

$\frac{n}{b}$ 是分治后的问题规模，$a$ 是子问题数量，$cn^k$ 是和并子问题需要的工作量


时间复杂度公式：
$$ T(n)=\begin{cases}
O(n^{\log_ba}) & a > b^{k} \\
O(n^k\log_bn) & a = b^{k} \\
O(n^k) & a < b^{k} 
\end{cases}$$

### 最大子段和



__算法的伪代码描述__:

算法：伪代码求最大字段和
输入：一个整数序列a
输出: 最大子段和

```c
int MaxSum(int a[],int left,int right){

    int left_sum, right_sum, mid_sum, sum = 0
    if left == right:
        sum = a[left]
    else:
        center = (left + right)/2
        left_sum = MaxSum(a, left, center)
        right_sum = MaxSum(a, center+1, right)

        left = 0, temp = 0
        for i in range(right, mid, -1):
            temp += a[i]
            if temp >= left:
                left = temp
        
        right = 0, temp = 0
        for i in range(mid+1, left):
            temp += a[i]
            if temp >= right:
                right = temp

        mid_sum = left + right
        
        return max([mid_sum,left_sum,right_sum]) 
}   
```
__算法的时间复杂度__:


本题分之后的问题规模是 $\frac{n}{2}$ 所以 $b = 2$, 子问题数量 $a = 2$, 合并解代价 为 $1 \times n$

所以 $O(n\log_2n)$


### 棋盘覆盖

__算法的伪代码描述__:

```c

tc -> top_column
tr -> top_row

size -> chess_board_size

dc -> dot_column
dr -> dot_row


void ChessBoard(int tr, int tc, int dr, int dc, int size){

int s,t1
if size == 1: // 只有一个特殊方格了
    return 

size /= 2
t1 ++

//在左上角
if (dr < tr + size && dc < tc + size):
    ChessBoard(tr, tc + size, dr ,dc ,size/2)
else:
    board[tr + size - 1 ][tc + size - 1] = t1
    ChessBoard(tr, tc + size, tr + size - 1 ,tc + size - 1 ,size/2)
 
//在右上角

pass

//在左下角

pass

//在右下角

pass

}
```

__算法的时间复杂度__:

设：解决一个 $ 2^k \times 2^k $ 的棋盘需要 $T(k)$


$$
T(n) = \begin{cases}
c & n = 1 \\
4T(k-1)  & n >1 \\
\end{cases}
$$

递推易得， $O(4^k)$


## 贪心

考察题型：填空题，简答题
考察内容：

* 贪心选择策略
* 算法的伪代码描述
* 时间复杂性分析



### TSP问题

__贪心选择策略__

最近邻点策略：从任意城市出发，每次在没有到过的城市中选择最近的一个，直至经过了所有的城市，最后回到出发城市。

__算法的伪代码描述__

算法：贪心求TSP
输入：无向图$G=(V,E)$，和起始位置$start$
输出：回路长度,TSPLength

```
1 初始化 P = {}， TSPLength = 0
2 初始化 V = V - {start} u = w
3 循环直到P包含 n-1 条边 ：
    3.1 查找和顶点 u 代价最小的一条边 (u,v)
    3.2 P += {(u,v)}, TSPLength += Cuv, V = V -{v}
    3.3 u = v 
4 输出 TSPLengh + Cuw
```

__时间复杂性分析__

需要进行n-1次贪心选择，每一次选择需要遍历查找最短边，所以时间复杂度是 $O(n^2)$


### 背包问题

__贪心选择策略__

每次都考虑单位价值最大的物品

__算法的伪代码描述__

算法：贪心算法求解knapsack问题
输入：背包容量C，n个物品的values和weights
输出：x，零一向量
```
1. 改变v和weights的排列顺序，使得单位价值按照降序排列
2. x向量全部置0，i设置为单位价值最大的
3. i = 1
4. 循环直到 w_i > C
    4.1 将 第 i 个东西放入背包, x_i = 1
    4.2 C -= 第i个东西的重量， 
    4.3 i++
5. 将第i 物品放入， x_i = (w/C)
```
__时间复杂性分析__

时间复杂度：排序 : $n\log_2n$
贪心： $n$
综上所述 $O(n\log_2n)$

### 活动安排

__贪心选择策略__

每次都安排最早结束的活动

__算法的伪代码描述__

算法：贪心求解活动安排
输入：活动开始时间s 活动结束时间f 
输出：选定的活动集合B

```
1. B = {}
2. 排序 s和f 按照时间最晚开始排序
3. i=1, B += {1},
4. 从j = 2开始考察到 j = n ：
    4.1 如果 s_i >= f_j: B += {i},j = i
    4.2 i ++
```

__时间复杂性分析__

## 动态规划

题型：填空、综合应用题
* 每个问题的动态规划函数的定义
* 例题的求解过程
* 算法的时间复杂性

### *0/1背包(动态规划版)


__题目数据:__

* 背包容量 = 6

* 两个数组 $vi = \{ 25,20,15,40,50 \}$，$wi = \{ 3,2,1,4,5 \}$ 分别记录每个商品的价格和重量

* 一个二维表格 dp 用于记录在每种价格和可选物品下的最优解情况


__动态规划函数的定义：__


```python
if weights[i] > i:
    dp[i][j] = dp[i-1][j]

if weights[i] <= i:
    dp[i][j] = max(dp[i-1][j-weights[i]] + value[i],dp[i-1][j])
```


__求解过程：__

首先，背包容量和可选物品都为0的情况下最优解都为0

```python
dp[0][j] = 0
dp[i][o] = 0
```


||0|1|2|3|4|5|6|
|-----|-----|-----|-----|-----|-----|-----|-----|
|0|0|0|0|0|0|0|0|
|1 (w=3,v=25)|0|0|0|25|25|25|25|
|2 (w=2,v=20)|0|0|20|25|25|45|45|
|3 (w=1,v=15)|0|15|20|35|40|45|60|
|4 (w=4,v=40)|0|15|20|35|40|55|60|
|5 (w=5,v=50)|0|15|20|35|40|55|65|

__时间复杂度分析__:

两层循环
内层循环为 O（C），C代表背包容量
外层循环为 O（N），N代表物品数量

所以时间复杂度为 O(NC)
### *TSP(动态规划版)

__题目数据:__

代价矩阵:

|inf|3|6|7|
|-----|-----|-----|-----|
|5|inf|2|3|
|6|4|inf|2|
|3|7|5|inf|

定义二维数组df

行是一个数字，表示节点号
列是一个节点的集合

$dp(i,V)$ 表示从$i$出发经过$V$中的所有点一次且仅一次最后回到初始点的最短路径长度，其中 

例子 $dp(1,\{\})$ 表示从1出发不用经过任何点返回点0的长度，很明显等于 $C_{10}$

__动态规划函数的定义：__


$dp(k,V'-\{k\}) = min(c_{kj} + dp(j,V'-{j}))$

解释：（最优解中，k到源点中途经过会经过某一点j）

其中:
 $k \in V'$
$<k,j> \in E$
$j \in V'-\{k\}$


__求解过程：__ （你错了一次）

||{}|{1}|{2}|{3}|{1,2}|{1,3}|{2,3}|{1,2,3}|
|-----|-----|----|-----|-----|-----|-----|------|------|
|0||||||||10|
|1|5||8|6|||7||
|2|6|9||5||10|||
|3|3|12|11||14||||

__时间复杂度分析__:

算法需要对集合 {1,2....n}的每一个子集都进行操作，所以时间复杂度是 $O(n^2)$

### 多段图最短路径问题(动态规划版)

__题目数据:__

![](data:image/webp;base64,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)

声明一个dp一维数组大小为v，因为总共有v个点

__动态规划函数的定义：__

dp[v] 表示从原点s到定点v的最短路径长度

dp[v] = min(dp[u]+ $C_{uv}$) , u为上一个阶段的各个点

__求解过程：__


|0|1|2|3|4|5|6|7|8|9|
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|0|4|2|3|8|7|10|12|13|16|


__时间复杂度分析__:

两层嵌套循环，外层循环填表n=顶点数量，内层循环查找所有入边，每次查找的范围是查找范围（0~当前的n）

所以查找的次数 = n（n-1）/2

所以时间复杂度 = $O(n^2)$


### 最长公共子序列问题

__题目数据:__

序列 $x = zxyyzxz$ 序列 $y = xzyzzyx$

定义一个二维数组dp[i][j]，表示当x0-xi和y0-yj的最长子序列长度

__动态规划函数的定义：__


那么，有两种情况：

当 $xi \not= yj$ 时：

```python
 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
```

当 $x_i = y_j$ 时：

```python
dp[i][j] = dp[i-1][j-1] + 1
```

__求解过程：__



|||z|x|y|y|z|x|z|
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
||0|0|0|0|0|0|0|0|
|x|0|0|1|1|1|1|1|1|
|z|0|1|1|1|1|2|2|2|
|y|0|1|1|2|2|2|2|2|
|z|0|1|1|2|2|3|3|3|
|z|0|1|1|2|2|3|3|4|
|y|0|1|1|2|3|3|3|4|
|x|0|1|2|2|3|3|4|4|


__时间复杂度分析__:

串A长为n
串B长为m

内层循环遍历串A时间复杂度为 O（n）
外层循环遍历串B时间复杂度为 O（m）
所以总的时间复杂度为 O（mn）

## DFS: 回溯



题型：算法填充题
每道题的考察内容：

* 解向量定义
* 解向量空间结构
* 剪枝（限界函数）的定义额
* 算法的伪代码描述

### 装载问题

__解向量定义:__

$X = (x_1,x_2,....x_n)$ 

$x_i \in \{ 0,1 \}$

$i = 1,2,...n$

__解向量空间结构:__

一个子集树

__可行性约束函数:__

$\sum\limits_{i=1}^{n} w_ix_i \leq c_1 $

$c_1$ 是第一艘船的最大载重，$w_i$ 是第i个货物的重量, $x_i$是标志位

__剪枝（限界函数）的定义额:__


需要满足$w_{current} + w_{remaininng} \leq w_{best}$，不满足就减去右子树(也就是)（因为子集树的右子树都是0，也就是不拿这件物品）

__算法的伪代码描述:__

算法：寻找最优载重量
输入：集装箱重量$W=\{w_1,w_2....w_n\}$, 第一艘船的重量 $c_1$
输出：一个载重方案 $(x_1,x_2....x_n)$，其中$x_i \in {0,1}$

```
1    对货物的重量进行排序，从大到小
2    i=1， current_weight = 0, best_weight = 0
3    while(i<=n): 
3.1     if 能装入第i个集装箱：
3.1.1       current_weight += x[i]
3.1.2       x[i]=1
3.1.3       i++
3.2     else: x[i]=0
4   if current_weight > best_weight: 记录解，更新best_weight
5   回溯,然后返回3  
6   if (i==1) return bestx else 返回3 #说明已经全部回溯了一遍
```

算法：回溯
输入：i
```
1   while i > 1 && x[i]==0:
1.1     i-- 
2       if x[i] == 1 && cw-x[i] + 剩余集装箱的重量 > bestw:
2.1         x[i] = 0, cw -= w_i
2.2         i++
```

__复杂度分析__:

最坏情况可能会遍历 $2^n$ 个结点（也就是二叉树的所有节点）

### 图着色问题

__解向量定义:__

$X = (x_1,x_2,....x_n)$ 

$x_i \in \{ 1,2..m \}$

$i = 1,2,...n$ 表示n个需要涂色的节点

__解向量空间结构:__

因为有m种颜色，所以是一个完全m叉树

__剪枝（限界函数）的定义:__

顶点i和其相邻点的颜色不再重复，也就是当 $a[i][j] = 1$ 时 $x[i] \not= x[j] $ ，其中$a$是邻接矩阵，$x$是解向量

__算法的伪代码描述:__

ps：约束就是

算法：回溯法求解图着色问题
输入：图G(E,V)，m种颜色
输出：n个顶点的涂色情况color[n]
```
1 将数组初始化为1
2 i=0
3 为所有 i>=0 的点着色：
    3.1 从颜色0开始尝试，如果不冲突就移动到3.2，否则就搜索下一个颜色，不管怎样，就是要给color[i]赋值一下
    3.2 如果全部冲突（color[i]大于m，也就是溢出了）那就i-- 然后回到3
    3.3 如果还有点未着色则i++，转到3
    3.4 输出color[n]，算法结束
```


考察题型:填空题，综合应用题
考察内容：

*   解向量定义
*   限界函数的定义
*   实例的求解过程

## BFS: A*

考察题型：填空题，综合应用题
考察内容：

*   解向量定义
*   限界函数定义
*   实例的求解过程

### 多段图最短路径问题

__解向量定义__:

$ X = \{s,x_2,...,t\} $

s是起点，t是终点

约束条件：

显式条件：$x_i = A, B, C ... (i = 2,..,n)$
隐式条件：$c_{ij} \not= \inf $

__限界函数定义__:

$f(i) = g(i) + h(i)$

$g(i) = \sum\limits_{j=1}^ic[r_{i-1}][r_j]$ 
 （表示已经走过的实际路程）

$h(i) = min\{c[r_j][r_p]\} + \sum\limits_{j=i+2}^k第j段的最短边 $ 
（表示当前节点和下一个分段的可行的最短的那条路径 + 每一段之间的最短的路径）


其中，
$k$ = 总的顶点数
$i$ = 当前到的节点编号
$p$ = 下一步的节点编号
$c$ = 储存距离的二维矩阵

__实例的求解过程__:

![](data:image/webp;base64,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)

## BFS: 限界剪枝法

考察题型：填空题，综合应用题
考察内容：

*   解向量定义
*   限界函数定义
*   实例的求解过程

### 0/1背包问题

__题目数据__:

![](knapsack_data.png)

__解向量定义__:

$X = \{x_1,x_2,...x_n\}$ 其中 $x_i \in \{ 0, 1\}$

约束条件 $\sum\limits_{i=0}^nx_iw_i \leq W$

__限界函数定义__:

下界：贪心思想，按照单位价值来放
上界：直接就是用我们的限界函数从 $i=0$来计算

限界函数：$ ub = v + (W-w)\times(v_{i+1}/C_{i+1})$
(剩下的空间全部用除了已经选过的东西以外的单位价值最高的那个东西来填充)

__实例的求解过程__:

![](data:image/webp;base64,UklGRlA4AABXRUJQVlA4IEQ4AABQUgGdASrzAlQCPm02mEikIyKhIpL5oIANiWlu/785CEZwmHnjbr/Mf81/kvBr/C/5L7d/U/8f+m/x/27/OD+l507Uv5l9zv4f929tv9Z/y/8z4+/Kz/c9QL8r/oXnxwHuiP3P/X/xfsC+yv3TzZvqv/D/dfVT7F/+L3Af6V/cv+t7Gd/b+a/5/sBf1D/N+rn/neXL699hX9iRUXlrh3H1+DEIyW5j/nwZLLy0zHJZeWuHcfX4MQi9HOemEXo5z0wi9HOfC5dj/vu8fhF5sT7HtBgCiPwi82J9j2gwBRKluw33DdH2NYUU9P/rUkLb7ffTb1jXsEOMYC1T7h1394AYnTo9P/rUkLGx7+6o/2DqHEqD+1f0W9hzvz6RAlqn3Drv7wAxOnR6f/WpIWNj391wWBc0auiAoZ/qmBw5SelhAoKecGZEJ5r5GBCys8LiljisMfXeU0MULDstjx8QbMydGJuGElEvsl22fNaHpz29N7/83cEsNoFejTMh3NzZ18Qct34ty/4XnMTbj6ZecuIcfrknMa6WJNhZRJiMmQCGO+10Q5/fjOxWr5Kw7LmAAxOrLwMcfpl5y4hxjAXnLLtZIJn0p+c5/w6HQU7wKN3rK9W4HyIdSDp581SrY37T6MC3L4b7huOx7+tSQr18oiXlfv4yPTbyvK87J/+Y9s6fsxjPpaD8fUxmR/3m8lleO/rN/kSdSAv2qmQH2BQW5RSQtvT/60WsEPUoo7MjBmUQIW87UUy6t/6VjWa2X5ikUXhutDI+Bs4biVdVtpnB6btFS4vTdq9YUnptA69zhxDMVKnBhuFuUeFiW2SI9zzs2V4rYvZyLnRrHQLh6676GoGfTXkYvWGDHMsSIlgC7BqdP8vAvgY4xgY3ZAGFE2cYNio7+CjHdVf1sS15hS9C4UnjX5Fei/+TMt34tyjwWqenPIY7b5+v63oGVW5ZJlWzj/xu9LnZVinI4xs8wgYTbj6ZWEdlqcgDR1w2fiN0gdPP4srCkP0e4dd/dhvT/60TvMTkdt3m+ki7rSO9H+w/6VE3UXPHFaZW6wA92wJxRqekhuRlq/8vAvgY4xgQX/nXyelfdFwqGQvR7tCHZg6iTdEvdPOIeVR5xmFSXwai+afsMT3s1Tb6pgAMTp0en/1omobr2xo1ScbZ/9c04VlCTADS4Zyeus7uXztEz6LtWAtU96uOaRa9AJzo6IEKuLyKfUUk9sxSSTypa1hqSuHmUD/SBtVzdzP1jgs7nX9QvryLJHnESbFjCxn/H0y8bL4ypEzPvriR+vYFOHI0KO9HIf0kYzaE8wjQWnut3kKpF2tDeWicK8/JT9Cm3H0y85YOcYwLco8K6YZfEB5LlDUJbANb5v94EOJwKujfgrc9i3Gfgbvn3F1oYQkFlB+i/rVsZY0nFyMRaJMv6GzEFuxezap6f/bxv5/FiVbcOu/tg0UcaN/at2gJ5d6Iji+p/pJFS3WV0I9/nI1smBiWclZs33K/UKCxWxCELbQb1BaPapJa20CKDvdmpDmIWk+6/zm5hNuPrvKaGKFiW8VEqFEWEhpQgLxct03hzesyI4063ElPXnTk7KT5091oR3GGuqFPqm/5nk5ItGRXJTFyd3Mjs3Aiinp/94A6NEzPvri/cCDPmU12F6FkQyRZF/epR48PmmLK/4Q0oIiWY9/m0CFQbcakKaTpt1lHXJ8pBYfDHIs4HYF7Jb5FMSavXkyA57VdcKgfy2GJ1ZnH67x+EgGn0MC/sPLkcifeIS3utDCFoz0i0quwL3cGuV7MdVT4++3WdAGckROF/LFCinp/94A6NEzPvrmJtqeFjXDeAwlbAULkAZdqBB8zx3yHBY/IJ85cQ+FyjwtyjwsS2yIIGDktEBwr4qE1hotWSeyuGm40ewi943jA0448fVlDxFDbO3TsCdQ9SZmhUz+g004ypbsN9w3R9jWFjuhiS+uGsOyQ2Fmyetf2x8vwzeBzzF15a1VFeYJL1lOViYVt0NL7ipXE2+FoiEBFeYr8QILs3NgSxslsht7suLwHISJjEdw8B+qHwtjymhgCiPhMestsVargV4kahAMT4WjcqOTUw8FZ2rpiy3RggF0QiMVYoBs9EXu8GBz7D7uOPPhFa0kHGmkBl9165O60yvFept7RtnHGwtTJ9gN03rSxuU7NVudzlS1vC3KPCxLbJEfCY9d9Lx4zW+v5TNlXXo6KLENe17HIyFbkIQx0UNMmNKS6/arDGlfw4QTrLScts12D7H3jEw7X3ZA/ACgKzLPhbHlS1uuJp6f/WoAFmX+G+ALkvfdbVLQ7aL7q21KEpGPI7M5g9uARrmtL6O5R9IEOnq/p6bcX+RdSZ15Sh2lLkCwgah6BqsUQOgbrBiUVLdQHow6eVmWwZo4Y62GTl7PNDASJmffXMTbj6ZYscVaW0QnzZshNOMe2nedkrC0+jfBhpSWBg819T2f/LkbyqG7ypO58LY8poX/4UFlzuiuxgS1/jELZLZu8VtlQ/q0BsZQdxxY2PdBS3fi3L/i3KPBYaTTsboRTggM+MRLVmPKCiS7kk4SNf9NyFTzhZTYKEMzbbpVVI/VV6eBWxgxP5goAxRnQ0R8Qct34ty/4tyjwrzQ71bK7R7CioWKPInctKqF4JXX8Wegi+dZpYsZrvNNIHNt0s4I6F+In/+S8W1U0gSMGxZNy1AM9uqen/3gDo0TM++uYnS75lhGvGZbPH054bLW/WHJLG7csV+U5LXXHEaxIUxDQeCrXYmtkTMg70+n5ZDgKMlJ1CCwgxlxomfjVY5RSikhY2RnwiXAfqh7fO5wZJehF2E3aU0BGaVBKftWjA7+1UDI8VWRu7W8UMZD0Pb8E6qMAFGQ8VyeRjO1+AayVN1SCQG1IW5IjPj5o6j6AtUm42RnwiXAfqfmWUk8+Oe+28tBStiZSo1N3Xd8Y3O3brcPls99PYDs9paM9V/Ie27O42xnAu6/ohXlcfERuwjbBlUjpSBtnmFwCqTVwyb6+1S5q69bltRRGkPjLzmJ1Znt87ymg/5Y+KDZfP5oH6I5n+gTIf67UQReEtODyD/1jvAYQLXotwRCp+eWNq19sD0OJKO27ng5bvxacFB0ZZiG4C5oa/Jt6GX6eNeYPYK5Kip//Jm7xQB6FsxzTiw6sla8K/K1s0TvBftzvRk3AGvNZCG0O2FFgC932x6ZM+7mc9CRTqhWIwA7+764tIb4uPmeTye50KaBgzkUUow0F16BJROP6KiV27FIlOQ1p2vIr/kgQk2IdmHXTrzVBX1gkDATItWEtFXwXL92cB4M9uP5YaiIO+wrWjSMeUjFv2bqQhuMcH9Y9QUwHP9jOlM3Z8Llcots2kLM01C+npBcCWvBncGS4X5oheqXASmeKoo3HpwXAsPlTan3lIPwUVE9OkRpzOVuFp7sRIXKwe22ttjLnuF+LNjumYEVu5SAG9dJkUKFRSvwCeLXWpsCacbAwWBOQ7FIX/GINNDFnZS3bhAk7l5n1QY3jprKFE2Zmw7NY6ptZ3X9EQAYDo4gmW2uNO/5kyWHelow89qBu2wI/0h+vU8K4oZg3Zx5KnJInDmGliNbxybVXDwEiVbwerIWqen/1vCw7IdmX2MMh6tLcvhvt7AAA/v9ggmGkAAAAAAAAYUbXVOIonTW8iBRw7SpxL59ZD/SHWiAvnXj1xAAAHdsXplR575PcLNbpVlxH1Fffj0o1/h1djWXxoKYKm2+zQXtpWmP179l5xJ5t+ye/fFWF7n/EhxSwI3BjJ1b/8nc0fpMq528kcey+PnTQzU5to6AwAAbxLz0s0eVZmOWtEAjrUq6U9v/wF9vBj+phkhDnym6m3GbZ6vLjQBvwkaVRcaz0RvLIFL54rAlQN7lQg8R2HyY5wAmEUnuzObViQVRs0koD7G0Ez1E2Nnh0sQeB7wc15+I1qyXLsM73pc+MOXYFrQUKfZ1GsFK0aUu/RvhSx08HpIGrJElzpYqoSDnAD2hOacnYJwBIE0G5dLnPWX2O6FOPoEF/QlMrKd5M/UxFdeCtleyDvoAdo5TjExddYG4xmwZHQcNghR3oOQSaRX4CpCOY5kEUwBURwEtgABS4o8SbCMoqD7OPAP1tkoyWygt5vbSvJ0QrH0TYrLtpQSKAg/I/LKtjfk9HD5knLElUTCP6/rDiL4BiGnXZi+kXzP5SgW9JHrn0UdBpS7UnGU368Fpj6dcz6+ZP7saX6M5qwiL+WTjzSLE3PRsr0HuIps7pAHFwazRQhTNH3oL+nT+AAACFCo46IoTC+HQvvvNluHRAdwDPNlKoxRohInU/6EHdDCpWWYWaA4kOi6VW/FuoIMxM2kijNA7+FR8kWFyVuxr0Xiyg+LedKA/61d5m9PT0PQMRYx8dQmgnGbTVypCU1HHYYm11R6T3pV9IHU2DdZFZ3UWgz1jC+QjwHyO/MRRyLC2rn5mgT0TczJdZ1cPbySc5oz+KxfKljWDR9+rW+M63qOw2hah4i+TCnhFVgihaBFIXj8a1nofws9J3X7M0VHc834EAAGQghzACx0NE5avi9BLM27bza+CaDbmkFfSA0ahy00/1jVMNaQXjkOpHXgPLdGHd0/bftNrBDJsGVFOSZBUBV1nZBGPEPKgGbC6fAw7eRpUGOlcL9iXEW/ei/HdFjGnSaSB91nPLF8esBcwtDvJ+Lfjz6TQihPku7geEiK3H6dOxAYXI2xll4looTbPfm1SpVZ/rLe9KZFhD5R0Xka5SbYiLlB5oYHcwkkWtwX8MRXkbGUEN77SjF9fJFbiLSDmcO4s8rBumhYGgmwAftfmINtyyP7NPWPZb4LQAe1mwy/aVRFojh6wE4T6y6V/9NUc5gySeeg9LPG9n/v/ju8x4a/PJAS+ElB5rKl3lFV7C1cskGQVdb0nZmVxwzdgg3sTZvAlZx0gEmjjMxFOri6RtYO06ILU6jO274yszcgIPmtS4ic/sRd3PJonMAuT9xCmPmSLUxEI9U+v1o2MhypJEfQGG0oM731NdXtsLQm+NRFS3yZCTvQGa5iN7U+BH4CWk41NVlWXo/rAVS5+7p/tBQ+7l31ZicSe4KtaI270LPqNH5WhsKTfG07EAf2A0qoUJt9SgbRudk1DW14+AwoV7rvu2+ukhToPMzPY8pgDZKjFmzKihEC2Vf2F5+rgciPqipfkJFww3r+iYbPqMLF6Vt7yUoo+7llmoVPIWMBgLSnNBv57pzqtsIef3Elcp1FAPO9YgVLvzf9qA0mV1hG1CKGuANhtyVOU1kqx8DJki1DCakwjTyQa8GxYDp3WLAF4vtm77f1blREO7omB82Dv47FkDqN7+Yy0dgIG5A6BFgmtDE3nTI7jhTe4EdAd6P3QUUdm9e6b5cdFsLUNxAGxfurI1jQNmPZp5EbTAZqEg82eEeaXO54TcnDVHPgbFwdNuIKJvw+g6mFGUHYpX9jIItmfOPlM9C10APRQLcPmn5PvR22tv5P3L+OT0PVnbxokQaBVXdvnzozvP5yt3xjwp+p7yrR4FxXk2RIhdy3f5nYe2wN3JppRRM1gfj6duPiXRjEBNynPXxZTV0hDddl+vxAN965j4SOhiyGiqLukeSXLs4VvUZ8tzNWyr3YpNYaVlNOL2QNwYtyi4MLB7bOLftiOBUKlMQE5KZfQW/gP4XDmGe93NThxzKpbruoguye+6MOU2NyZpO3z65EMtGcaSh7KUl1Ko5pN4DLOlIQNRsPRknhCGHBCod9fcfYFZx0fa5hjfENq2lXe0rw05MpIM8J4A86CWIP/BWB/gqq1r9ZSVaOoZqzknYGaPPj3C6xGzA7PHh+BpIsU3YKmClfbM6enL0RnxdlKHBnhoU4FsENCQARUmDqxgG8vj2Dbv/HdjfHjQPSEYpDlRlqwO6nYhzRI7Kiwqww2cC6mTQn0SKlwHhCOOyzVGGkJvj8YHAFKbcj+mFhoZ5YZFeIegFWv0F+o+10Ay6mcaCeSRVNJLIpc4Z8hkJDuDdUh8MfVLEjphdl+T1IYxZRHP1/6xaRVb0rmYN2BN1Sf6M+ApbJq7c4tJeRBmhPDf8SKdx/xqADiRz805j/Wd7hrtn6RqorOBqu9UcYLKMdW0aziRPVmkkekVt/cdgBzKnqkkz0AKwjOfj3o1o0RcNHGodewUfNW2ycvQPFEyj3cySd8hQeTklUGXDOPxb290N7Ex40Ox2GccYUJ0JLhbtwYjJXCC/4YMVZKq8Dl0x1vLRlvoV7ZBtuTsR6JnnOpMg+SvgOdYA0Vg2EvxSCItLunDYoD3XMgsoCisDNUB51jv4OGmExgoqeGBQKbVvbRp0CmaQtsyMg3dUdDO0yBEDyZ1OhmVSXpN5b+76QS06uOrcyvC+Cs0ImDrhutWCnOngILrt5kZtIPvIWJIv4d/q9QZ8R8ajO3RU4l91srsMq5ALsmhjDW0kSAC1JD3wZmDPL+S5Lx5ieDuBTDnFsRvbdlT3Ib+fl/VLkK6Bn0qRlTqvqZvM28aCJnQdSmfHpI8sioo1FZxWBmbcss+MqK+AiRf1dHFr47UN1fqGYyyQTmTSftvmT8/jsyyiC0gReSThzwJ77EgMOVTUGCQEOBzBBIvkdN5/XwDgN2aKKQZecN2XdsM2I+/cPQ7RNieeF+dl/98ih7Iyqzjze9uyvg2ofqw2mZ9n3d5Cle/31880wVsFgCUtTVz2Hvb3tJJxj6oOHKADCCfEEh6lNgeXDw3h8sjoZs64oKePYl5hvl0WkRTib87uILc6K7oBL5sCkunL/vKcOPYZGpZ3B2is5oVPqtKJbLpDDMshsGw5L2sIH4hEJ4HmLxwFVRS9sFCJjtWGVgm0W6u9y+g5Xhbm3fwtOQl51r81zYUSilSUn0ODkVI3eGcvTIUoTTPCbzzvXz+HJHYNgzueDqjanpfYojf9VJPMHWS05nyGe5ZaMsnJL7fnXhSt/F8jP9IsRYqSMmrZKbNGGMwhB/7aiGzTeGe38d5reUNYCFmP2oD0gpruOvJFPnbLSJU9Cztar6KxRT3PEV7lI+hnI5q5rXkn6THhIVHeOARhS9i0yrlhJPLTba6n+WkWcz+Pl1VMQVZG2uRvYts0+jmxmtvkbN36QPxkvpZOInUxQKS2zl+TYTWw9eK5PP0PTN96+HyL8q3w7CPiiQnPgSvx1aE3GkfX0SSefAuia+V9mclZ6i8xxy3C0BB97OabBzVLFymyzh+woYUpaJzO9qxHf7nbXJX9TkX9sJKnvMXdOK8QK8MaixnI8SdtQ/aQ5bD8NcvrrQzHnn/nLqngKK21on3AKOUumpggjl50mXLgq/yaAWA1GPY4dYKmXCesaYE/EQsA0vGOkZwNeou+K5rbpiDOO6J4GqFTjp5GnADyDQr2VnD+39CTgk01BAwB966I+aSsABuMFVdCQxcwkkkl7+IqEiC+MlK+WKZ95Kqw8Q5AZe4yKz5bPupjptFtWwG48QDJNtJrvmNT3vO+w9APkqO8zTxHry+RMJzfz89nRMn1NmxU1jKj9sybkysQcHSphRsTDhB/prdURaJpcqP+q6UH4xaPNa9k8+2tWt4RvubEFuFPZNPXLwL6RJceXYTbZmeonjOiTNV4pi0j7wgCK+AiGgcR8rh9Sj2i8Qy0rIqXJZMxDVAWh3fEXaBmR7zICRZQMAuintBoECe2pKmURgrjlNlcwLJv1bEomF5j4lcFPX1iu6Kx6OXHq8ZvjJpAw9nZWIiOD928RFelUO9SSe7BAwl+0ndxssaWZPA13VBBw+bAWgLbtcx7r4foIdADBy4v2423UiD8RNn1xYOvhrJzxfKM1XMIFbe9HWob9QcYJ35Gdp7/8dBDTja8uyTE79sHng0dQCCrsbme5W3Xme5pxDuvFN5F0ml5VmUtyzc1YP/HdTWXjPG1+OMJEa5myry+Rsxmkpl5+m5DXT4sSmAvzdzqSt3jhrc/vcAoQbFiJKU3HwO0rNADfVfwZCLbyfbMpwEGAIPNYXfRa479zjdOLM+5h1Z4KCEl4JSJr5C4ety23RchYzmf9ZaWgqDZ7nxPnjEZMlgOVkUQa5cGmdxoYp6CLT75U445weE8art/ZYPMNKkUF8YJdmxcE9Hh2gFyV9MZDQQfN2eWaugMKic6YTYjBgN+xdyXPEl0ujfQLOoFAEsCmVdUhAcFtHDoNjH6vP2gwE/Ye7f+ps/b2w8IFXUq18VKUhk/1foCzlB6N3sJlHazBwn4glMYU9PwiZwgEfr2LZBzOfXW9gAbQI7FI49basOKAfC1lDrnUJfTKajfh9BNQuvzPa1DxNuiuUB8P3/E+GjdbanSFfyIR4C+DF6JSDVHsAbevdBeT0bvV7vWjKMczlGbZ/TFRzo17SCLr6M/sj4XG5tSTF+PE8myYOkhfaQJPX1QhGMAekMFDUzjEP+r6PU9q+Zq0CEIw7MI6PjvKeiMme9D6b3tMN8OhLXPzrVRFeKSzBBwKORvLSRGnDGMUfMf6hED82is5kxqhdA6FLEOgqeKGpY3zMDcMJTtf1rfQgiqzRtZFehQbboJ6STImTgjjjXfK5LfsriKgjsi8NQd+fwRy5ZcFHH6D1bJRAijW//cxqvWkD7/colMk8VtSFj26Am5VhyxvadN3p9keddCeIOJT6G9XjjAO3J8qcumwxpRVgZu7MW4G75ExCvzx6VzVp7BXZzZNmMLS5EXzGnDXz3ZqLgV3zfhYs7ii7kD5A3Mq1LFNxZJ13EP+eezy1rHFsrfra+jnuG9aFMuAtKKUDuj/eMQ1SI44Qzl4g86tEo9XnSu452ZePWYtxtJkP0zoa/Zr32eCX/fZBzMGkIyV4g7BiYsE9nTsymuKPnoFAFddIYp6Xc4HsIrTpDmqXmRDso56Jz7GijDmJdaCOH9tWFFGDUWnPTkfvQYFF04CbOgITNm+/B/XhMiYzGXeSZpTm9zM7yN+gOU0Th4EGazRK7skQ0pVUA0VEiRQgtVKqJO7wotThTk7AU1XvKMBHQlumIJSN1o+c3sKwb2YhPyotk+UJs+zHY8XGcK1KyzoAVzF5sRPBXlQ/LniANLIGmGZ/PNBX8jARIgZ1oMllUY22xo3C32xb18bM7wt0RnlzvhpC7IpVMehCacS5Jvy7oxHu7Lg2eEXa02/aKCW94++NKK0oLCoRu7RAfvZBC5EZ7/BH0kf6z3B96HmlBy8tGCbBQns/z0YnrGZfscG2Wgt3f0kJFTB5HcHrzOVQ/YLpbm9EtliXv/Kd1C4pbYhWwE9GUftuBIZ+vCOossrv1YNHr3g0/lu3jQYTPCkDXLl0HQ26mrZ8rpxUrhOuPqOPIYuTqu/W0zdeNoCD0m/9Z6fVvyY+3OTNfByH7RQHU8E7TcyH7s4O8GOw+y0WzdTpFwMjjUoBIe+oAIW9nu0fsQuU5ehYvkrVXqWC4kkteHlnv0FMMN4fwXUHLTpOqdXmA69Ri6pwrsmNXCGmtXEaxo0Ey8oO0v97CHzR2dhH7JF6JfjR5VtB+OA27WrIaAHzZjz+mJ3YzO4iCa/UpUfVZAWJAuhE2UhR+g4NrVu6WK5zzd+RICdeVbhokNr8zgBI4e126PNHRzE9CJlHlNm+fG3R3iaxOdwqSxovN+sWY2Evh1DWBDOgCE6arIFgzAse9J3itSqQCueRtMdM3SZTpOtG4JskK+3gv1Xhq0iiGcsxpC6ZMej/bP2FmBegm63CH5pcEIHKrooIiOoRZzSQaRaREiARTlsqO1m37+24WKJNJMEvkpWOJV6hMJxAdZ4V9FZ1uk1cWUo/t1kK3waadEE/DZ3tnmDd8VXR1yFQ5/jMLpenIGHFZwCrRuLCwgx5w8rZFmp0DNAVZucGTIO7xPiukfnzdv2T2gy7SXr6OUC/3ybOyzOxTl9uT54NpVH+vWt4UiMwdL61xgq5nO5a1HfHOyGtyZV74TWMQGJMuoc8g4K0/tydFGAjtGjt6Q3LCBPHyb9fohSwRAjyjx69Tx4b0+OzIGq25gy68M/w9RW4XQoWywmpncI13E/QruopKFZupEvAVEN4DPLImsWPsyFPqjlAX8zyw9CY6orB/7Ly7dI7fb2wFi/o7VeFk3NV7y7egjdYNjLKmIcWPrYPbEbBI4lZVYKB9QRm/eY911ozNWOXrrN2OKK0KLvKP3ZHrq2maNsJUTQHKPwBi8kygbs7VYyMdx3IA4IKnBuuU3Wtom4fBBsOeLbb67QMSJQE3Js8PBoYVegPLPvVcj7v0F7bAmQ2wWOcA/dCC9aanj1kx0oOtaEhVbAmZ77sAYAEzy6AlrFJYEby9iReHsFH3sbs9qBNh0ZMUy1G7ebAovafekb6KCW26LwIdo19Eu/tPITmd/StavT5VyAk+PcNR63UW29m1rUHAsc7IMVTq9NEaplBweC77zSgvbb4fF7im7kwW1QaPSGJTEe+xLsr+JEy9CoT3bUKK9j4LxIYERiW/oYnZ91rQ7ZwJqvQyyFZQAAAQLzgu+EtDeXE4FiEpcmnpH8orVP5F6F2D3XHfBg7U58hvxkINtyk81etLMEWOzOcPFw9I5OD1RUj6g67a9nS+efBkL8Q/kzzBa0Rd28E5xYWOBMfp2vEMiT0vmxs9Stp6aFpmi47mM+BneRD5OivwAa8Ni+s2G9t5ZhZR4gev3DX7uxhd5NlrvT0OKcD86KqWS9HoeP15/CrGyteUkamNjgDwiaGneq3LRYHkdnTmMl6xQhJSByLS/kPV2xDfalCAwQkuiGWnSmB0MIqDTWIHbggEOn36mxZN++SdGCMveDYAqRZlD1QpybySi+e9E0DsZmGuHpseXvvNHPZTcVy5Zu9gvy9P7evIRB29rR7XVTRUVLSU1Rdh0FzKauHRBLVmEH7DPIQJQH1ej9SJG0rxT03JPezEOc1B65VRxh42HkIRwAUGA4nE/mdSb1jUgw0qswne+bYiuo8JdeBek949dRPmxvjHexJVEdPw756WcbFTRPrEA177OOIPdGcWv/hQw7D3JfYRQ2hpwwaNCBO1UxzBEcxzpZHQlfbZjZ8Pdf4dZE3ofeLAkNqsEpqaiW6w/b0iu9hdjgZe2bAZGRq5kKyGfThhtnzFeZuBcLxxFKT15epRBj3QklTGWIBCsQaCGnXLt0X3HXj7Xrm4POCde0bcBuPKfPmUMwb97fZ8VcSpNCwyWMOx1vptR+OHdPm/fKzPtqs1BRn6nxsUAFdnulfIRIqqeYFew3YzzzfZvilnQVXXvSlSTOMEgSyDlioxnBM3JRaDZesBn0DPsP2KEP9ZshdnTqIQiVZ8mrXn9Sjlfkk6gWYJuriTaDeR6yxHR8pQhu9HwjfJyGTRMtiRksGAUc6BC67FZp6Ts51wkJlmHwuyAAT4OocwK/elnOdRhSJgkkvqg32jDr1jNkJvq0kv5MipMaNCF2mfUecQIdS6iPhy02FMMJg/dUjUs2+FYQcTXrsM/2j4aUYwW7By3q3Q5wmymgJSJtjCICXaM2VuOTj31ZOqDnfEGHWWgATeHmlxGt7g3hpfaAvMAeInNXRxJHtPMgsrgfp5G3j8Zt5uyPxw5JMuhRSGtKOacI6fcdQh7H3UOmwZfSeDuADVyq20Bm1wKnFITG49SsM2bLVqwv5if13qBAMJnmSSCG0u42ocwGhcBwEiXQXnpkFhA6/fzNSDSn8EZTdKdLTFgxjFZM4GmOz+d6G44vZrZf/XTuTzzP2NGEUxARdbqk2MfCA/y+EdLiukSNjoO/istlYaIRrvKmYEnaH8tXuv7G2vqSjAdpor1C9H0Vg4P2Mym6sP4N7DSMCpEnNm9IrDMgHQHbx29YMU7zDYDTuPnTlBFse2BTi3QLHP53cYCm7K5Hq5FhzSx79SXfZ9MUZUlYKmzle6Kx0txpRjdO2lDOJiPtRgHVi2iFnmyYPgfiEP68D1NsW1oBVp/WAYAgDM+c+6JDhTdYpq2dVQPM5m0RZOyqOt4znfqWWJ+20RlSJGa/4LKCvH2egr8JxoE5kIOWcgGEtsVPRcECN8S+77X0GU4SZqkqmpm7MxeU90BG8OU6e+p7Ge4kJUyiZgpd2QLf8AU8dHo4J4oLGU15iiCpzDiqNp4BA3E8j3BewMvViqicfEhe87D3/JvxsFQyfHqZ8wwW4TYHJmHsZTb6hT6tlpJ1pyL2ZruSgCgddTem244c447xeFhhLE7qvnTGov2zJQ+Qv4xjGZuQ3u+WrE7VYHlHdPmiDMjuKm+FdFRwozwudLl3Jt92hCcZZn5K44ej2XxbV7WlNzLUh7IiGbBZvL1KWYfZ/sU4VK388rKqQ0S7UAAs9u9018xZpYs2nTY1u/TNFLJ0+ZFyRkfaCccjDjcXIEwOv5OILHVqBNwMLoxoueIqtdsYj3YpskhaoZ0FyPuoe3+7QUTnUEb55632E0K1wCvWH6QnZ3PEcdV0X1bGdqPtbDepjU9quk9WxABs0YjiZyJm+tk8F6qszdiL8jKyNQor9qg5n8Zcl7KroQ7Qlx8RFj3g1Ldm6vhsD6GGa5/7T8cS4DGYGO47ofoNEwd95bi/hqkv6Ll7OTltDPvDCdWxZYbzlg9ihLG7HkuzTmnUcTi7IyNLtv223BymjX+67DdqQRZfDvPJDt6xnKPF7Dk75qQvx2dreNet2EspukGI8XLAqj4Hxo8srjpEvMsQftVlU6+berQitKYl+vtfGeCBPzXUWrLPUsEoTrpJdfpMx9AzwxclnAFlBOqIfZzj8Bbxki+dv+ZVDcp6UlUQ6g3YabdH/rb6gYK0+qkx3o0QZFFFTL7l19HET4cf6lYTWa12VvROL+k3gmMw1nn6ftXgtUUi2dByWnZXH3/FtFG4uikP4rzcwQSg/lGCa4y6GN9ylPQRMjueyQ+1dg33Vf29s6gJe5piqzlP+/ROrrE7MBqQ3FL5q9yqRab/ze9Urw//nI1N3hsZp5/7Ue+V0fM5t+A+4SrV9dpG7SGqafrIUbuctCuRKk9ooF92smr9JPV6Nsy0AHsCNbKkOXiP526ohYPOweQNNnV1YPqPeFImfZ57gTkeXvBEr0mbuRVd1hZ8pDMj158LgUBn6EJb7Uv4Rg+bExe6ugu35TmpdAp4xdjq8WnA+hBq1/qjJ69JMpPhKzgmH5AijoPy1Jc49x7kQp6BrQI+jXryfNsAwQ0787qmtrhTQBxedIj1Qnt/JreoAA4HsX9fOKiBgFgAaCRXiwzHO+UyUn1UYnwGRGGg0EvQbXlkRmPRGwbijZQLsBxIvTbhX9PdysDhZrQNGJB3KfwdSSxIS7h0wUAwzrofaEyeFH7HluPcT+pqew5PdZq/N+AcotABGn6+w1ao8hQKuC3aGCQ+1/VFqJcsH26ws+0ysjDTGHwl3Twx+YQ3svnblcl9PyxlfeQDaKmqOy30dmCeD33eZW3QW3sNL+3AbBtaIFdShb8nx09CnxgBhfjhupuQ9JCvXmXyJgZdQnQRGIil2OK44EE/DS+hCKct8bHhqlE5Zax5Gks08B8UeG9SEuscFukj2c6Hb+7R7SJhjK5c68UwE0HwxzPjFPk2cqOKWQT/xYTekPk6T5wClufRZQGuU6DEeHXNCFnLGPAm5VHkMqzTnPu2esCgOry2eaCf17gshSnjJmXs4Hj2taUoZJeYqIpVR8lIaJfMBV6CgkWQE83G9OKxRXbSHLT6MVkqLK5TjnE6wqk01LN6rqRapNI70CPtpAIqSOE5iJGJ6OGvV0ZDD9cJap1n/ikLudtwdrCpwY3eulzpnJHFD1bzg86N2k3Pz8XqwA/WsqUbQMXcQzf29rTIJyqbtDyzAwmXLwIr2A0/0jGuLhSFwQW+qkDA0n+o5QxnDfcG9mANRqgTRIDbb0VdbEycoPMwGBqzci2P9sa6LgK3QKesj3+KiXVMOR7I7IZa0eTHzRWOUbktg0l9zauehjnltO7qF/igyB8AI3TnGUs1F/Jlrp46Kdr535/o9OmEJFzGNrnri+7hiO857oH52PS0bbtqsMHRQq5Dw4q5HmHkir7MamaNzJLrcNkBcmjjNOtLQUpyKx57ffkEu5HEt66bFGVthsSlRbR4xpop/0VYfGM12ecSN3C4+WVfq5LurzJ5dgOG7KGcFgJhnTvkzcx6B5rEVykW3DGAaNafo58lD1lgrqKmPmItkjqQphwfOUxU99uUlPc1xv15oU3zPoIAGm3vh+OZnXvh1MBF33g9HN4geIwAqvZngsK/d2t67kSziZKb/z/msprw7B1oZHXBSQLHJL87p5RMyEeimO/aTwX/LVayc+cvN+h2/gnfhq00n9Y9wmK3yYXWJ4KsjYykAtHePW5vydy/iAEIFqEVKI4I7w10TilCidRJDxKEMXLbcEJaEUJKUIZF02FnpOgcjd6sIN2G/XXoHdm+CWjzbqKkUOVEzGx3JeM3nRiPFuZgFsEVOkdqo6Wi/fj/zxk8uhaDJn+JdIWvKtSFolWzwLsdSdd5nGGyThhPWDa62GewpyisM8AiVIYRWli9qF1Kqw+2SzGMSVWJ5o4KTZdD9hwGRB9Q6Tb0k0Z9J6d+l9I8KI2lRdILcKjoXZ7z5rAfvs1ondtmw9m0y2BN6yYY6InCr5/PyfFUsKR44VeyOrr9asyAv09LQCBYpNadQUb1BVBwq5iLWg+ZoCM+gNFDvQBwstTIg1ulpaL6SnLazXoJg2Zb8wPha7mCVhpnwemAbx2u7AAGOctrvVG/C9yM10g8X9gELzLcvyQpDGRVpoOhK9Q+gNIXy6xavVu3pJ1YfVDg0vBusdwNZsTPthxuCy92MiOvcEswJ9QwkQ6oRvk4i1Io9Td4PqoLg+cBOhw6tyv27jNKv8RW3Uu9ycS5tj41PBys7LdWRJYPtlZOG72BnjV9Egv+zoW3a2ks1GeqZF8/z0ccSW1dNjen41ubuufsgqPfkGRdG/fSd5Z19Ou2XJ6656nh4qQAAK4j2tUvfldR6L/7IYQQP2KbqBuB3uVUiNfst3ft/2KEFDJbZEM6xc/gatC13vfR2MbKROubF9hMN4+nI5IIpi/BbTBdnwGZp9QI8+4TZkkOcblHB3kJ77QHHIDTjF8HQ0AYMIo+buZUnjStIFUDtpVE5fSnGw6aXywpRAo5h0LsxttNkPZebOmRehQLegtrztyexRL4hlRc7Se7FZW2Uq8dDHJDFKxojWMhOynLzNRov2rnhVSTe/FkJR2gkPgZDycfxmSrKwn2MJRWlPx4J7m16TaCnOCYmOZ+i6FH4U8eJjNdud6CPJBHQACwrvyPEFaNyQNGSVhj1VrRqw7LOXjXtybkcIRKozm34A7g3A7remcZ6+lo4mbL36N25IHsM9h3rGzQSdX14KOyhJuW1wEGEePsWi8R1Jx3sAbZxinfVdhiWkyuKw84b0TUQUd6AVMx6vwPiTrnnz5ExGmQrdNb/H5HtVAX+T1sj0SUmv9V6z7n4JnAZ6MYi9ks0abBjXW8DmCSHn/86JkC0l9hy6b/CXV5aBhQylcGUkgCELyF0TLZv4uXbAL5iz9+ouzvoorLiADSJBg19kzV+LPxUD/ziSt+ssCc3CiWMHf6MfdtD0lm36CkHnw2Yv+RD+vuSUboDOATSGu+tCpOrvAnM6Bb+ehbGcbtwz3/sahk43jxHM1Fca5bk3zmmVdx4A4tSfYd/zW19GBUFFD8ubptd0XyQwKsZNC4wb7+0ehcOmpF2MG5YApLEB6PxxJvvN6TrzoIFAt/pxQiCJ6uqEkTBmPrh+mCzLhrfc7xaBDavqFkP9rKppyHcXNK0zy5vhuXHAagGnofVIxXj04tvdUkxTRorH52hHAQQzpWVYSEhOubXjWjXYb/J/Z4ozoumLryrK6sPInD7L91SU+9iXtXpCtkUwuOkGRea1dXYBZhgvGGq+oc4jnznp3Ilh+h1Um5BDGmotsftyhodXAmDDlG1lAaU9j1XUBjkbHGQ2uj/3aXWxTFYC2tOit9dSiCyFLHEmQOg+HZQ9cX03I5S8zvaoacp/QWagS7mm+MeBCEj3pE3ivr6cjhkit9k58EvzExsPWSVyjmEAGEFuiPvmco0eAlPJNfTZYfWvZbozshl8co9NEQIhLXpG4OL1Zyf0LeWPXCG6INfxO3TNusEn6EEzGDV5nV1QE4xWaTcqy4U2NTDJC+naqhbk+jN/frNY6qpnve20fLmJ8I58zuUAWBaCQkVUhngv0guy7dHUVvTSDb+F8depSeqyhLSlxaF8zLuk9+TugRWgODHv7kX48qr6AriZ5fayI49VUUub7IsxHpiNHNgyOxPtsgdv7lAp+5GaSuKsQ0XLm54IEH9ASu7IYZP2GLswCBg92LUSAJG7eo19tHmQWLw977FyM5zJpHvMJPStUn2k9RmmVK8IVshVy/xuKp+e/AlljEc/lchi+uHLXfqCLqj7sqjaechPbJsdmfFCpS67yZZXCRJykj8XZCRTqL+WaeR23uw0Lx6FM2xuI6+xxpplwdn+ZKK5OTWzeVoE0asm0Evknk6To59HtP66Sdpaonfk/AvVgiRLWhuD8x9WkDVNcC1aqbMSxGzQCrsUm5NiiAI3nq9m4Jy0oDAa619TqrfmXFgur3FYM08dAL56joViwMYH50v7uG3OnTEmrM8+0SP7UeYfa4Nv4wpPckat0RpPUzaW4iQP9ea7htWVj2yesp0LPWy4HZIxgrewepTlqCYrm00/oPQz7AdVuBRstQcm2ZP4DREI200syUt77eMuT4WZMT5t7iW1uwCFKnXgXP141YrVJPHT1wDYsdGv/pyHqjMkniVx9OIQoaDWeLU3D59R8ffnVYHogRj2vX0OjF0GKsFOcoe0kaCQEduqOU8Ml6+hphF8VjvE4AvOKKcSXCu5HLlWp0Iy+LzRarPQvKk7gsCtN8sQMsCZfD4N5YnXWY8e+fdCVFPQuS5R2OjzwFjrK+jgNvookBpHJJZ6A2QlNLmKkxYBr0X9wxJrNHuHjNrZJf4g9NE5JrVRxUnXWqKP3+HyeG/YU0iCr5pzGS+y7YD41uFu2MSSqsyfLKR/4unFpM136R0p3vYTSOwsOq7OEnVoeaciZwqiEq9LjBb5wjNB6a5JG6IXJSo5D0vQGphanPII3GKaoWRLTQjMSxNZkwS7Y8g8g4bouZ36XlO2hcSnetLVPETaC2cHhXO54yj1/L92LjDZ83F8PBTaG73RxLigGdGPaYcYp2FQ5mk3+DnvO5at1kLEcq5xrieLtVgHrN+Hdi2s8iaZB7vJx5PcbbB1HgSlPJIbu8lj72hXzus6/HpizQW/dtWwPAXY46JxasG+Ku3E5LkKl96rCJl6Zu6OHGwIUHLYNfgLvKAHpAfTayl8CRBIo1HIWObcF7nUErtMTmjDRJxMb85+IHuxPZNpz5YhA7SbZmJQ9K/TIlezqS5TB3cKE/bXLArEQiQleGksq3BAXFbbJfZN7W1mdsrXyqNjoXEAErRsXd0AKUsVSlOYCE2WwFTfDzo/JTz7B+5Apk/NQvkQLxadgcamTyIjCrZWPxyQeA1QyZ0KChBrnm+5XHfettqtXB63uzrFIJyO6hLFkpIvmmqqQlIHLSLdYhvjGmnCHlP1b8kZw/U7Ho/3R8Ka9FovLS8xEdQzTa31d+3DR7dcqA5ullTdEttuZolkCIc5SHPvTGlXEzvN9wDe1juAwb2GRWHcASj07a/ENBOnzIBapQkV89xwrZvJeIkFXzo/bKK//c9Dqj7Nq9Oyvd8K0kpv8/8ahPwEWPwpKH3C1UuPzEfyL+sHW+viH4j+3erPyIydhPNeZoeDWx0MDHH5wwqeF1qg3ri022qPEHEo30XoORbkuo4A8c7PdARLTRKgHgwCIIdcYGgvPDByEN6+7xwksskrYe47fDP2m5uPTCO7Jmzhh7Y+MIAoCvOXDLuOuAMjCUwpotVWMRkVXkyHoeCec793qFP3nOx4M8+GJNUf+bahCT7jHhDORsIleFct/X802IkXFR/BJfjVTOVo8finfSTtg4Oy37mEHlO+E+p7qKJczwKdK6VfAV9KvPxUmrm5UeyRvBqNysa/c0LlnJMW2uXu7+70FjWBDOgfn/pZt0VYncMIRVJPfMecKd8pcWr33PKYPlKokU5+cpJs6zv7yLmYoL/X0jdiO5WWLd/GesNKHAlxLz8tGHtCvjvBY7gpxzDh/iywBOcnACftjf0Bh2hnjBQfyzRQF2JWk9jLLFYJbH5tX/9UHmdxOUJeuqxWfwC4yLVSKJoVKSTxDqCqfsgaJ6CU6jV02phQbYUgf2mP2hcg3FkgOBxHqUFej55/1dhNYR7Vd1IVBbbgPzLpCey1OYEaU0r+Djjs4bPrC/9cyLix5c7yj0JdvY2oCnEAA+ifDLqv6TI0jtvOQK687ikRAkvyGkCC4hQNlXuib2Y9PyILnQbtjBP2HRAYgrfMm3fD3tQ5uHfs2foQq1d9j0ckiDhgj2X2kLYznsSiAzkWBGFuhQA5wVqmy4HSZhnCXpFXODVFIpn2vr6tALnh7k8Zhe6BeQPBFdad+oJJ9C8PBOk/q7ZxlU7A6l1XudZ5oBUP6rLD/KjwqDIGoG8Ii6TWPcA0SPxsdxuRRc1bZ1V4fc9yRUhZ2rkqk+lgzvV1k1QwQm/ssbVIrlLbXQdojJtQKjKyX/dt+APPI41HUOYwNDjiq3fdqk7QzqUSi7TDfcqfF4qtuipENFxyEqggnKImhT5jmHNWGqaTj8tDqNrxW7FyrCjNROtYQ73mhjeXAPjBmjF9kgIw9RdTukCLiiYFE9guaMMnBTYS1O1wGmmKfF0kGMH3vAa1V3DvwM9LZiEQY6zvjiNLP2DX7PhZFLDSa9gn/jsX6MtiMzimKS6s9JpupFUD04Wfr8Nnel/5gnwVt9frvDQvJx4oUoo6swzb93l6+cx0nUhLCZYVzIztVcF/vdLTEKXUj2MINptxH5mxcXM4BAJwnlzGOUwvWTWwoO/IwIVPTR3E6Oc8Itngy145t372pG4ngUCyqmdD9UzuoMTGNwL5a7FtPnXJFfBnMTzABCPfiUdsTrCnVSowddy/EVfPVxVJ5TaVk+XaLD1PWXeKcH2noZzjpNwkh6g35cdmxiyGw6msbTLnBHerzkQ58qr7QZIY7qsgFudao/qL2K5BZZrSJr1/OrU+UjBgWdILesb9yAmZ7js2hh93DEZghbOZ2ZrXdO8UUigBLOkrxVFPDxLQDFulNKzexVhWuergr0Oic6UCAFgx0+9VKLF9q4kzNkDVhIRzis4gAlXclWgoAAAA)


### TSP问题

__题目数据__:

![](data:image/webp;base64,UklGRq4MAABXRUJQVlA4IKIMAACwTACdASoTAfMAPm00lkikIqKhIzEqqIANiWluumBpKl+vH+j7cv9d4l+Lj0LL9OH/lv3y/Vf3L0T75/i3qBe2t3v2n/Yf8j1Efbb7V35uqV3y9gDgfaA/6o9Wb/U8oX2F7CQ9pin/lvFSd+k4ixrRXnnfY35KNymeO44weHsOwT/2b+BGIZuGfCsjkEGmn8B/SHwI/eGf46a5o2M0qbGqBLTG4BVkOxy0KKxc5O0nzAR2udKDlrkPNWkPyEP+AuafBqNB+BW9t/15u8XwI38E1zBumkx+kQ37zbFHJdycre0uEH+aLpFGj1wVs3zn9r8DDNU4tpZP2cVlbLUu3iFxR0Ai+1nAJeWji/zvYwyHqCmO9LFAoIC95XncDzZtNiwi9ZwDObAn2KD3FEm1GlLTQYyO9gjVtpAt7YNAA8ky8/Mlw1rPEUDkjuy4pqjpJKE73rT1bAEKYwkj+UDLZ5Hyy47ugG2QOO/l5RWoKcThE072K9LB1J4NmPiLN96fB3ovkp94dZjjm7e7P3wBXtGAMmwglICvx4beqlYZCHaXX/JutQzSSKsld4MU9rji7StFaCQtDTig263vDRyUijcnmOJuaeBkjr5EF35CyR8exI1bCGRyrtJgQEGiyVyFtPIvq6bFEEjb5IPjFI0sq/c8Oqr4WSDVhYbpZnG0oa6LdDuC5CbSE4JRE9LQ+/gilI1yuZ0z7svpg+bEDgo7CybGK717nYUIt1ylecJjfwSvgaQVuOmkAK930RAMkC52xRhpQYMb9majxqndiqv0a/gaIfOb1xAm1l4sFMo6EHWOTp5F+WtO8Y4SwfiSZ3XIAP78MA8fZl+KrMirZFLPH/smBFSjn3Cv/xBDT0c5tYolBOTuOP6KebaIyIb+KX0R+bv4Utt/c3Ib7R5L46lgainu5hUJacAx9PvtoMzvqyw2o/9BnTYNa4BgFXF570A/Bvn2YnRBL6ThPtOSO0WRt8QB06J1WlV9TffT0xsg2Gn9CbU+5/7v/5MPlVVGsaJaabQs+gJ4hvOgRkad0xWXin47BZQclj7Qu5bMGOMuPo75k9GSvOPyUaD+cheBUlMkcHqUIMBbXwklBoV0ejlBi80d+BZPX1rM0lIvtJoErnpGBY4FpjDc5xaCWuN+rlAy4k/jcAVZ/bBd90P0znJcjQM6fR+GOk9x70rw7B6uM/6bkT2DrIt0q8BDes3tHy0WnTzc4bOi2AnV+QqV0+THhhws4m1iPU4yiJBY37IdTv+DNYqnp1LY/o5NnF19SJttYeI5ohQRf9zIMPATH5HJ3eEFoOC0MmVPJwYneN5AB7YVWI+dz/hQFuKcSL9vcHIdQezV5+jSE43xC5gmHlf+RI3CQB7YUKmMX9o+KvUV2KicyX2qtwJYRHfduMq85nin1f6WG2zk8KvqklaXeYBDQhRBGYRdlEBvJgFaQMWbjDxK5DuDStU5MNV2yXThZ3NrkXkoQmM5Dfa6/Mvz7ZmxlXQB1luUn9mIeEmR/ntEcmHtAszE3890FU4Fkv8grmf2cwk1q5+ZBsjBiMaIpq95p9g7k2J+LruYttjunxDVEGxdlw9fBITVxNGzK6iTKlvGlLBraZRtlpWSBlE1uzn1ROHok0ALtHhvlgdNeXU8YLj/2oWG3mC4dWdh8By7ITsXhlvGNlqzi27/bemi+N4cucL0JLRMhasecjRorX6PZhUxjipmmDrt6actkaTnftPx66Kow71WBGdmo445GM8xLt1mCfXkIGRjeRe+YJ/HL1nXNZmaV83aPKOI2nUe8oYoW2cLUGLChz63AbDa8oALqM6p2ASlj92mkafQx4NNOmA0/5e0DijQuGXL/dQAYCWSLmZYZCNH6WOI0G8xDVlHteVwpDGhw0tRYXvmrf4b/1ETMqFkJ7lKP4jeoOwn9guGd/wWH+avpjYRxhhp27zNmuilpb6PfZBJ+knm84bJcwieozXj3ypf7EZMXn8ve3jMAAvrT7G0GgyMyrntSXxzG/J8ikJrElfmYHFXrwLs9BO28uUMyNu8PbxNDt+IoTxxV07NNpFunuyh3cq2oX64SV8VuGd4oyfdF5XUisMfzouOhKAsKPVzVARzFSnKsvgd+yTPWwrC5WHqE1MHp7xRmvNt/meGjwaeuRTyPSxyArkVxpO3RLdrd+/ptwrIhOZn1fkDg409lxlolw68rb9bE9VI73MxrLPeWnI4qStads0KyUZ4IIdPvyywOO3anMxoHoAINirhuaBgrYzq0+qvDGoQBiOUUsJjauJ5Ck2SV60fZsKSOuHHoIrjsmVrjd8mD/LBlEdfvEd3g484j+C9BMRsXAHR77Yxy6EG5wQTIIewGCOrHeCZvynT/M1Q5jm2GClMF+AFnfQr/y1U43GZsl/4++uQ6PDGHD4f2YzoUjR8fgfB0/RzZUqW3+yV29K4A85pH+6eVtevCS3nZAFHqQEWbWr6gJVn4rI3XyLvL+K94ZV4ePJXLAfjkXt6SRSfJ2LABdCqhq8mTN9++rpqJCict4w+BbnZjqKKgV74ep1KyL4rebWON8wDN9R1M89wIqb8/psTECj/AsOwKjylTk/CcJtfKn//pQd0ssu7ZJINeJF2e18Roh/6tHTV7MvhMCss0idlDXOAbsyBqDQuO8uhZYD9QlTisSrtKvdgEQOFh/adrhCsxZI/t67/edaLOMiihPxAweh/UrsLR1hyoiROK99YcCucktTD4C16PqiMMGGgHX1OPFqaParoB3kEBbDhHirvaOQHcvlui8Z3PnWGzgSN0bx+xT+1C01euBNocVt2/LF/c3QsyutX/ref4fu0K3YyW0IsYoB50Vryr8fXT0v+MS7d1+4wV+Wi5lD3Imn2rmmrEXXHUBf1He/IGD5X+UzHmDNQ65/j2hgQYQmV8UM0/UzdyRb1CuNvCU53WvLz4rD4FkyKqD9pc/K2IdR7X6gkYg3Hj9i3B6Y9uCWdNXasFMkd/Urzz6vjdIGjZZfUex9D3VCAVvLFDUiviq87nFEW41ljstmL80LUsyWO3dG+SI7lxWrdbl66d/eArXk0JAIZjAuhSgiFG1Aq3bZY7RJM1/GMviqlvyT3h8GwI1Sgm2OivUygAABxSeJcj7P7cnBF1EXzz6ELD4Zrbf3ZQ9+mEZuB8Vx5Lypi6YoYqO40IgXwCdyo+ooqqbnZe6rwpBu6Upi4RGMQdGdZ/xMOwpQrlntdD7wOv1mJgfQwxAIjeIwCYwF/UJxUAixqM3o2FMmKp3i2XcQX9xZF2bvc4UjXCPxY5f9sx08zxw0mlMotwwiWSg1DTOm7UPdzim+eshuI32BVI7PvFeS4pyS92oehqoPt/zDu0mSGTKXy8N5nZln+x/Y471DDhU/dTZ28uZ8uUoG7VC6lvi7GfbFtoRjWU+3RIQZ3MFovBdnsujGYS+tiwEK6bZPO1vGhQPgvPyK5rHSNwB10Kx5VHxC62MQOV8JgVrxGhqpMalNnmToLgXhfz+dE0wY5O928TnN0FS6sEmoAjkqCHDmoX1/syD5WNVqbdxNdWGkyuYk9CYOPapaKNBydfE7EiTnAyl17HbXnUm7D13GXY+pbZ8iem2Et0T80Ab6aeRmTxh8jGN0vERLg6rV+31CtrlbYVOsGqbO8ndFcoLgJMmznZgbIl8UZBJg+uFkXQtqloPhqzMZsdSv1k8AqE8Nv46gpbKCkyM1sj62TdRLtR+R/6wxahHFrXH+4mkXZYtghbFJyd9sX3PJfUBAbYAp4qdqEPkX8PoP7iLw500WyUJFjgNPzKViZ2TacB+KMXF85YbeqtM3hsQxWfjYSQGQdh/sorBtYgHCE/vXFi0tt+whToddFb4HIGFO4wApXmK9wwz57SgGNkUxglnEiTswlc0uWtwuz1hjR7P2oqFfehYgsaUJ4gboAdoWaO7eTURrNHDRN6lJJ1ng3w1X3nejT4B0730w4Cp/hCmoOhuiPrwOiePdjQJS4dTEg2yIb7RyASHfingxdnP/BTTqGahmZSyeud8M+rfuZezNuKyw4RjkE6je62pKAj9UE2Vxf72rVrpn6mDCW9kP5slxIUA8anx0LGJkzqLKt9ec+bLKLLiqUjD6FCou89OVKaeFGAt3UmxfqrJ18JxFUDMQMB74WKtQmYmC+QIwjkKs10td0KXVtgzjH402Wt9WvGe1V5gaLQ82vU8l0z9BYYWYraXpWCroHsntjv5LqCb7cs4dacYdkPLYNxGIskRCo093Hs1xYhE8PgNhRyBrdrNyQe+3+eYjvIOnUi9vtUQS2Ef9vyYGAJGx5dHx4O22FPRuqAAFk0AAAAAA=)


__解向量定义__:

解向量不含起始点，因为没必要

$X = \{x_1,x_2,x_3,....x_n\}$

显式约束：$x_i = 1,2,3,4...n (i = 1,2,3..n)$
隐式约束: $(c_{ij} \neq \inf )\land( x_i \neq x_j)$ 

__限界函数定义__:

这个题目的最优解是越小越好，所以限界函数是限下界
上界：贪心法
下界：每一行的两个数加起来除二

假设已确定的路线为 $U = \{r_1,r_2,....r_k\}$


$f(i) = g(i) + h(i)$

$ g(i) = \sum\limits_{i=1}^{k-1}c[r_i][r_{i+1}] $
$ h(j) =  (\sum\limits_{i = 1,k} r_i 行不在路径上的最小的元素 + \sum\limits_{j \notin U}r_j 行最小的两个元素) \div 2 $

（$r_i$ 行不在路径上的最小的元素的意思是，从集合U中出来的边）


$r_i$的意义：$r$没有什么意义，它的下标$i$就是它的全部意义

__实例的求解过程__:

![](data:image/webp;base64,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)

### 批处理作业调度问题

_tips:_ 这个题目有一个前提，那就是，可以证明（虽然我不知道是怎么证明的）存在一个最优次序，这个最优次序满足三台机器都以相同的任务次序在三个机器上完成所有任务。

__题目数据__:

![](data:image/webp;base64,UklGRnoPAABXRUJQVlA4IG4PAAAwUgCdASr8AAEBPm00lUikIqIhIpGLGIANiWluumBpKj+yn9x7Uv8P4c+Nv0v+q+f1k37D9Sn5N9qv1v+B9De/f4z6gX5X/Pv93vmu0/tx6gvsf9g71L/O9D/rd/ufcA/nH9e9Lu9hoA/0T/Kf+b2Zv87yl/XXsIfsEQTVKL0LTrnAO7uDinCOAhz9kHnT6/ESuv+pdLu7+BQR8VEIPosZ6wq1NilxabbtR43eoHJ+iv0hVMCN0yhLG88vUQojTSjLS3Ewlnu6+xVVHWzjmhs2SALeaDHMwafYdd9B4lA02RuArV7y5GQsm4aYQI+/ZYRyon7F9rwbYUCmvwQ20KNxldoxKdjOUbxPuR9JsDWNtDceLrcBgyaKyXqU3mATLYAE8oywmjiqrvgoVj/ytPYGeEakcFybJYT8YuMC3SZQV+cynxu7fKEF0bHpS72t8IIT+qZifuo9VDcvrhlRr8K3mEAa32xH61HMtDcV0OloamkIpUu833/VZE+o0yNWeBr2KUVQr8X46u39831M8F+G/vt3aWkawR9rEYmQhsBqkXIAEqoGvN17rC+0CnIdLxXl92lgi7LLZGJTyWynxiantAm0PTHmV0jDFsOmaasXPpQnZmZW6qppcnf8YMnUehxo37HgzKUDzw72ovOFjjr5fRPr3fLL5We7PRgjiSJMdb8vAhC9ncRPng5IjuHEZap1n7bL0EVSPLqfYeq0wNa5ktONE3CDaYWKGBM+zwMK/uv+qheXDzAJXKCQ7htSWAFA3dvKroy0kvgoPPJFStikTvxPz7uGVZlPZgo/wSkvkv30SfrjK8EYJj668GjN2IfqyquBKb9oALvkhsu0fuP7a0nAJcPChQV+5rYPGS5wgmAjIxioNEYt3EAA/vyRyifIEjpmpwTDGDgo8l4AmD64zfsZ5QiIxLIdwRtpN5A8FRXtf0k9KefGabIeY63x1Yon8BwKvrzZ2zf59Dvb27P8B9N+JPD3ghvh3lJIb17rYwVsKdt/7ocvpdi02AYC2EPnvIHC16EHh+9teDn0F9xx6ObXLqurqdBYwNR2Jg3DxTGAaVZ2awYMPli/+GOgswBcmZiwUWh109uh/HEmmKageG+5F8+AzLXOaUBclHq9WRJtI4qS1E4No19vt9gZV+lGkk+8uXxS6epQbyq8zoh7mgvaN04CNAVpcWxlRgc6qLOmq8QRcTkji0XG7/SMzDk8D7+ivFBOf1eUR1Ds549AGvi7//RpGtpxZsm+5tVYhWxyT0eeQ/1KoonGscEvhJ8dlBUVKRu3CD0489cJJhwGspTQtS82q4ZITHKedUFoQ8ibeDePCTM1hRNtnWm4/57AEFWMK6cMDzqVdGS2G9Zx7Vybxu6wfYMXEHyAlKcPTAHF1T2aY3XcL+Lzi5mowrZEdiel59nAm+cNuYAVW6ipkNuh4fSCNuK2g+QCM/KpDF7WZ9lHOu02xto6xxZO78Y938KKpSC/RzweaLmJ7XKu89Uv1vS9i/BUqqoNgZjE7PpIGf+Gw81dPOv6SfjcHUvKcvWLBd/4JBCwR//YrMOHOHpZDj46D5W0+D3aWwIymFh8eRrmyLwy41ZnLBIRC4zF+/9t8vSoI4/LAA9dXDCH2p16QNC9CZyzGUIiXAkp4stxtTzmE48iGnv+gihlWJnHHR+jNjyY63Ck5lgmPTHB5ZlZJCexUpAEkJUHf5ZGz1JIuKcG2/JXhSylMk19CacHH2Snn4Fw0kvQQ6clzEFE6Gj1Q5RoUT8ilqMK5IQYP42UEoLfeM9yqupSdwn+ET+0ulMb0/XsOej+NA7fY92t0/fOiXF6RjMjIQ26C5p0m9J0kCzbbg0PA4Ua8j11boomQihC6BvHhabMQZn/v6WfYRmcszWtO1HEY4KEUU48jvXhz+Hx7BLtzoBShSca1ZvmCuZHcn76I5+Zusf+4bDdvbw919EuV5ccQD3ht+0FgP5bUk1/ZGyh4VBU/Anh/oIpkMzX1f/JG4a5C1Agn0xAcWcvCZJcr8SowBaLfK4Lacpd5qsp1Ada47mrVn6nAUM4Uvvr2tc3jZnaUoadCHqb1ACo3F+SlYQA6yEV6NSmB+Ru0rvwBIx5QMMLQoLoR5qRzgbd58z1rIUL7NaMUbumdacDEQrzw1crnNyLP24nmiRWX5m7EndYsU99QEdLe0L8UhDwstqq/fS81MXd7Fd92DAyBHydWcD50z6zV1EQoAEogtb9IYLvAzyClErNGZdMpyiT29mnkCIji8q8Qq2k20DvO5ARof5OW20NEceOWkXeGNh1rg9xbJg27shveSPvaQl3GezQKPlTd5HZwB2YXzV1uTLz5isH7rM3FzpwhzpAjNVHEFc+mLMxfp3qKaMF7DCV98JyxwV6D7k0sEIJThct4m2m7+nl/zCsZSAAT7bMQuRPDURFnsxWua0WkzJGdrHfIEnc5/8nbzHOBAgEodx8CBkacNRGrL5hsaMDT0/cM5FY4rFVgb9UWAzsckTBwLW90600ALqOcC+LTLUBgE9PSgxwtAQi8Bd3Mi4cUFiYme08F+kftfhhEQcoy4KKRQZ4VjFNec1t64rhSjkPA5ArB8NKwV4LydXA/Hpagvdien9p+PaFV20NpTx7RkjYRynOm5UUGZBwmQu2+XwFFielynDwPZWQmTcI9C8a2ndsH4+RNselmP3XHwrrmaeoR/+v67XLGI8kOGYzr5KXqJNuFI3hKaMI+TdfDVPv9KLlkD/q6HUgt4tPp8C6+ipChDr5IJBmuYx0zxxNA1SN8Bek9hW6fZPAjROAnhZehAJ6CnojFU7PI92spycH1dvZUT7BwGHa1M7j+MqmKwFQkKbJ+Yr+MkleKUjRvFTX3SLBluzX7o76+oL033MhWzkurxllpoXxm7KD05ahv24fjbbRpb0FGv44TkfRhAU57WOSKHPCXPuvux8VTksI0kHrOI2nV0abaw/jlO0yRv1VzwlfjmsPuTJA1s2QYLeWMf6jmnZabwUOFcLFrlLm8Wk4X9uiIkhodPkXeBLp+VevfFUIsPGxXEVNSniU4BzlexX0mSfj2OGhh5toq4nh3ZtFNgP2henT3FuyEu5ZK8dyvNvH0hbGYUp6OAza4k+HTVo3t3+DTw1ajYGlaDZD9vNEq22yQ7B/gTtbePHSmU+PqlTo6berQfah2NgJVVR7RH3vmDbO618vUxYRFfIMiasCBuPDAlYvt0aYMn6X/PMiFrwvMDZt3o3+dPF+kbL1pxjc+c/A1/RVwMZQgrdNJYMS6bSSVl9KHYVBbHZQGuz5mTLIkliPvKuM4YOmkL4k6AueFzLpa6d+Z4Ezu4fzYX5n7qxtDGwe7AKhTcx5clpLUSRQRGdT24Cqr3+Xnjy8bqSHeIRvskvgN19pWF/y2xDLNAs7XIVnz/rgHP2CNOjdNXKxrggepMxNQE+maoa1998/6PCks9qo80cRdkmGmbCJEjBbGDq3y656nGqicrkcv5mzRfGnYGML8R9TLwxvxz/fZx5yRuJC4lNwLSqHCUdAVfl34shDBsA6wXkGj9z+wQZc3RX+8PbySczTnk965jvF5B6eAp+8L4vVq0yAYPmqWEC59dgio2vmFISs0RTDcJBO2qX34Dp8FDmsvR5B10q5Tx/Psxi7QlPd1KbnyY5w348tskCstG2l9znw3mblT1+UKrSPrJLpdxX6GM5jvkJGGq6ybYl/oCH486KDJmZbowPoy2r5x83OJOEHfuYIDA+EhqtfinzSFOOFLU3pW0qgImDJHHUGZni11NekwHgGHt2yH/59sxNShEgO63VeovlWLnpIYYduNXyYd7jIc0AF15ZxEMUGoUppNOIj62g4F2dtSDZ2g5JHFAIkudHMRfuXKoy3MEmkbeSw0Xft2kQdvXxA3gJMJiD6T1lBZGKlJ25gDQI5IkmvxhoGivsOB0byu0Haxf+MkwA87OxLOY3d1iUmwD8Q3St2GZNvPiiBOE7mLOdrwNyZf974pZRoQ9+xNAOkxNEP7NbaHH8lQ38Q7Ir74EaJnm/h0B0V/Kex5gVuzQ5X9OIufoUL2u7P3D2TFt/FP2+wPWujM8rLbOu4X4+uqF7GQULCM44cOkWFWE5dqEGO/Z+/ZGcRQCg78W5KWi8LQozAo7Zh5wPtXk5JrWhM0tAkmufDWPtVKM4YzfWyqYY0YM9Hm28ALjfDiU6w668wu6VSobOQegn9IwUCzBh4sLPUOXxPCUDcq2CgIIp9YjeiCEo2r3ZbcZl80Z9y20BhUagW3xeBzORGFtTDz/+gbQr7MCPFnKIU5FXq4oqzgvdEYN5G/HSvDtzC3D+NZk/kaRKepUBQD6Vep81sbxOBPHTetIqzqV1umG7yBKe44PSw0Ju+YsatYPT6R0Xr2jKVQrrMQiVI/k281EOZ4KA6Rhp7zCRF5dj+PlN83MC6gZMzbpLsnLpThHz2vmFNsL7tslbw7IfBgn0jDMoaCypJbeRA9dMY6A23SlSTpLA7qFm66EhFTGCi0Gbt7gAyaQZp3H4vfSf7UStadn4EeBfVTtO36uxvj0SU9CWM/sfVR2DZTLecMRCBU5zdLmd1KlLBCP2Q/NWtjl9SFJDMIrKaiV4o0dbY/UHkcyCCMlbyE6fPUyPlI+9Ul6o2H/0emgGWgZuV+ixbs5ZuPQ0rnVH5HdjmhDxQiOw3zMptKzclv4Deid/B/lgawSYb+XBFD29pQOw4odHot9vllKV2O8HUL0+SUfn5WpDOxbDq/erFRqf4EdT0moQGIbWc2ioe2/VQORg2DNp1bzEnCjaZjYEbrl/lVIE16yPuSriw3nfGGXy6Dlg93sZFLbS0+kRiIUZm+8lvHPWSHiPZJL+SiMPUsP45nvTCd21pPxk1lg8z/kBHUSOEDSMSa59mFWhyjlq3Ve6230burpGfnKYZ0edQk/pddRbNc+1Jp0TZo0JrHpA8HDTQnB1zKEB0JjueQONRY2X1oIlt0RxheNlNs8vkoATjAjtZwH02AAF2ppj/v6t/9LL9YD0R8Bewc6zv1/D+bcPLxsE/pl3K+lYJMIZxEzAiwNB/Dq9maZ8VTJ0sz2ttisfMszI4mXnaGbJg1tIXnD8oXcZXdjPDhXZ7tvHsxaZmTAtYXxV8wmgcYM4UmasraPNzrR+C3g4IEFr2iiwZzI+4bXruDN9RWdzGPztuufg+fXYqkFGvCNQdEu9+tC8i7TNBcVKAZjMaM0IYOAKCS0I6fa8CL49kUEEmSD2iyjdogwyoXPhbD8B6AL0Dz+EgwwAAAAAAAA==)




__解向量定义__:

上界：随便弄一个，然后把它的值当做上界,比如这一题是 41

__限界函数定义__:

$t_{ij}$ 表示第$i$个任务在第$j$个机器上所需的时间
$J_i$ 表示第$i$个任务 

_SECTION 1_

那么下界函数（最少可能耗时）粗略估算为

$t_{i,1} + \sum\limits_{i=1}^nt_{i,2} + min\{t_{k,3}\},\ k \not=3 $

其中$t_{i,1}$ 表示作业 $J_i$在第一个机器所需的时间
$\sum\limits_{i=1}^nt_{i,2}$ 表示所有作业在作业2所花费的时间
$min\{t_{k,3}\},\ k \not=3 $ 表示在机器三花费最少的作业时间


_SECTION 2_

假设M是当前已经安排了k个作业的集合

假设 $sum_1$ 表示机器1完成k个作业的处理时间
假设 $sum_2$ 表示机器2完成k个作业的处理时间

$ sum_1  =  sum_1 + t_{k+1,1}$
$f_{lb} = max\{sum_1,sum_2\} + \sum\limits_{i \notin M }t_{i,2} + min\{\sum\limits_{j\not={k+1},j\notin M}t_{j,3}\}$
$sum_2 = max\{sum_1,sum_2\} + t_{k+1,2}$


__实例的求解过程__:


![](data:image/webp;base64,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)


The End, Good luck

