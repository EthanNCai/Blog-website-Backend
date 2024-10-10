# React 上下文

本文将会用最短的篇幅记录如何使用 React 上下文（TypeScript）

## Concept

前端是一颗组件树，我们想要把所有的数据的 source of truth 放在组件树的最顶端，这样方便管理，也方便在不同的组件分支传播。但是这样会带来一个问题：当组件树枝繁叶茂的时候，如果某个深层节点需要某个数据，就需要从组件树的树根一层一层的传下去，让代码变得十分的臃肿。useContext 这个功能就是来解决这个问题的。只需要在数据产生的地方写一些代码，数据需要被消费的地方写一些代码。就可以实现传送门一样的效果。

有个有趣的例子 from "Learning React -- Alex Banks":

- 组件树传递：从旧金山坐火车到华盛顿特区（需要考虑整条路线上的事情）
- 上下文：从旧金山坐飞机到华盛顿特区（只需考虑起飞和降落的事情）

## 准备工作 1 -> 你想要传递什么数据？

首先我们需要定义一个 interface， 这将会使 React 知道你需要上下文为你传递一些什么数据，也就是你需要声明一个“上下文蓝图”
例如下面的数据是一个典型的例子，其中还包含一个可能为未定义的值 **kChartInfo** 和一对 useState 变量：**duration** 和 **setDuration**

```ts
export interface StockContextInterface {
  kChartInfo: KChartInfo | undefined;
  duration: string;
  setDuration: React.Dispatch<React.SetStateAction<string>>;
}
```

## 准备工作 2 -> 建立 Provider

根据刚刚建立的上下文蓝图来使用 createContext 建立一个上下文，我们需要为这个上下文提供一个初值，这里可以先不提供，可以定义为 undefined

```ts
export const StockContext = createContext<StockContextInterface | undefined>(
  undefined
);
```

值得注意的是，这个 StockContext 仍然是一个类似于蓝图一样的东西，本身不保存上下文中数据的值，它类似于一个 Tag，数据的 Provider 那这个 Tag 去发布数据，数据的 Consumer 将来需要拿这个 Tag 去从上下文中获取数据，这个 Tag 包含了上下文的数据的类型变量名等信息，因此代码补全可以在 Consumer 端实现。

好了，有了 StockContext，现在我们可以在组件树的顶端建立数据消费的 Provider 了，语法就像下面这样，这个时候可以传入对应的值

```ts
const [kChartInfo, setKChartInfo] = useState<KChartInfo | undefined>(undefined);
const [duration, setDuration] = useState("1y");

<StockContext.Provider
  value={{
    kChartInfo: kChartInfo,
    duration: duration,
    setDuration: setDuration,
  }}
>
  <OtherComponents />
</StockContext.Provider>;
```

## 准备工作 3 -> 接收数据

在 `<OtherComponents/>` 的任何一个子组件里面我们都可以从上下文中获取数据，首先需要 import Provider 中的同款 `StockContext`。

注意这里有一个非空断言，因为我们在 Provider 的地方已经赋值了，所以这里不可能是空的，因此需要加一个感叹号

```ts
const { kChartInfo, duration, setDuration }= useContext(StockContext)!；
```

接下来就可以像正常变量和函数一样使用这三个值了
