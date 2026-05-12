# Search Algorithm

# 1 基础概念

## 1.1 搜索的类型 (Types of Search)
* **无信息搜索 (Uninformed search)**: 除了问题的基本定义之外，不提供关于该问题的任何额外信息（也常被称为盲目搜索）。
* **有信息搜索 (Informed search)**: 使用启发式方法 (Heuristic)，从而在达到目标状态的过程中获得更好的整体性能。
* **局部搜索 (Local Search)**: 评估并修改当前状态，使其不断向目标状态靠近。
* **约束满足问题 (Constraint Satisfaction Problems)**: 对于特定类型的问题，通过更深入地理解状态，可以更快地搜索到解决方案。
* **对抗搜索 (Adversarial Search)**: 在存在对手（博弈方）的情况下进行搜索。

## 1.2 搜索问题的定义 (Search Problem Definition)
一个搜索问题通常由以下几个部分组成：
* **状态 (States)**: 构成一个状态的具体细节。
* **初始状态 (Initial state)**: 智能体 (Agent) 开始时所处的状态。
* **动作与转移模型 (Actions and transition model)**:
  * 描述当前可用的所有可能动作。
  * 描述每个动作执行后的具体结果/影响。
* **目标测试 (Goal test)**: 用于判断给定状态是否为目标状态。
* **路径成本 (Path cost)**: 为每条路径分配零或正数值成本的函数。

> **结论**: **解决方案 (Solution)** 是一系列动作的序列（即一个计划），该序列能够将初始状态转换为目标状态。

## 1.3 状态空间 (State Space)
* **定义**: 从初始状态开始，通过任何动作序列所能到达的所有状态的集合。
  * 状态空间通常表现为一个**图 (Graph)**。
  * 所有可能的动作序列构成了一棵**搜索树 (Search tree)**。
* **构成**: 节点 (Nodes) 代表状态，节点之间的连接线/边 (Links) 代表动作。
* **解决方案**: 是一条从初始状态引向目标状态的动作序列（即一条路径）。

## 1.4 状态空间图 vs. 搜索树 (State Space Graph vs. Search Tree)
### 状态空间图 (State space graph)
* 是搜索问题的一种数学表示。
* 节点表示（抽象的）世界配置状态。
* 弧线 (Arcs) 代表后继状态（即动作执行的结果）。
* 目标测试对应于一组目标节点的集合。
* **关键特征**: 每个状态在图中**只出现一次**。

### 搜索树 (Search tree)
* 树的根节点 (Root) 是初始状态。
* 节点代表各种可能的动作序列。
* **关键特征**: 同一个状态在搜索树中**可能会出现多次**。

## 1.5 搜索策略 (Search Strategy)
* **定义**: 搜索策略定义了**节点扩展的顺序**（即在搜索树中发现节点的先后顺序）。
* **评估搜索策略的四大维度**:
  1. **完备性 (Completeness)**: 如果存在解决方案，该策略是否总能找到它？
  2. **最优性 (Optimality)**: 该策略是否总能找到成本最低的（最优的）解决方案？
  3. **时间复杂度 (Time complexity)**: 搜索过程中生成的节点总数量。
  4. **空间复杂度 (Space complexity)**: 内存中同时存在的最大节点数量。
* **时间/空间复杂度的衡量参数**:
  * **b**: 搜索树的最大分支因子 (maximum branching factor)。
  * **d**: 距离根节点最浅（最近）的解决方案所在的深度 (distance to root of the shallowest solution)。
  * **m**: 状态空间中任何路径的最大长度 (maximum length of any path in the state space)。

## 1.6 图搜索与树搜索 (GSA vs. TSA)

**➢ 图搜索算法 (GSA - Graph Search Algorithm)** *核心机制：维护一个已探索集合 (Explored set)，记录访问过的状态。*
* **避免无限循环 (Avoids infinite loops)**：因为记住了访问过的节点，不会在环路中绕圈子。
* **消除指数级数量的冗余路径 (Eliminates exponentially many redundant paths)**：相同的状态不论通过哪条路径到达，都不会被重复展开。
* **需要与运行时间成比例的内存 (Requires memory proportional to its runtime)**：为了记住历史轨迹，其空间开销往往非常大。

**➢ 树搜索算法 (TSA - Tree Search Algorithm)** *核心机制：不记录历史状态，只根据搜索树的结构进行展开。*
* **可能陷入无限循环 (Could be stuck in infinite loops)**：如果在状态图中存在双向可达的操作或环路，TSA 很容易死循环。
* **探索冗余路径 (Explores redundant paths)**：到达同一状态的多种不同路径会被重复计算，造成时间浪费。
* **需要较少的内存 (Requires less memory)**：不需要维护庞大的已探索集合。
* **更易于实现 (Easier to implement)**：代码结构简单，仅需维护当前的搜索边界 (Frontier)。

---

# 2 Uninformed Search

## 2.1 搜索算法：广度优先搜索 (BFS)

以下为课件中的广度优先搜索算法（包括树搜索和图搜索版本）及其罗马尼亚地图应用示例，已添加详细中文注释。所有代码均维持原课件图片中的代码风格。

### 2.1.1 树搜索版本 (Tree Search)

```python
import collections

# bfsTsa: 广度优先树搜索算法 (BFS Tree Search Algorithm)
# 参数:
#   stateSpaceGraph: 状态空间图（以邻接表形式表示的字典）
#   startState: 起始状态
#   goalState: 目标状态
def bfsTsa(stateSpaceGraph, startState, goalState):
    # 使用双端队列 (deque) 初始化边缘集合 (frontier)。队列用于实现先进先出 (FIFO)，存放的是从起点开始的路径（字符串）
    frontier = collections.deque([startState])
    
    # 只要边缘集合不为空，就继续搜索
    while frontier:
        # 从队列左侧弹出最早加入的路径，即当前最浅层的节点路径
        node = frontier.popleft()
        
        # 目标测试：如果当前路径的最后一个节点（字符串的最后一个字符）等于目标状态，则返回该路径
        if (node.endswith(goalState)): return node
        
        # 获取当前所在节点 (node[-1]) 的所有邻接子节点
        # 将当前路径与子节点拼接形成新路径，并加入队列的右侧末尾
        for child in stateSpaceGraph[node[-1]]: frontier.append(node+child)
```

### 2.1.2 图搜索版本 (Graph Search)

```python
import collections

# bfsGsa: 广度优先图搜索算法 (BFS Graph Search Algorithm)
# 相比于树搜索，图搜索增加了一个探索集 (exploredSet)，用于记录已经访问扩展过的节点，避免重复访问和死循环
def bfsGsa(stateSpaceGraph, startState, goalState):
    # 使用双端队列初始化边缘集合，存放初始路径
    frontier = collections.deque([startState])
    
    # 初始化探索集为空集合 (set)
    exploredSet = set()
    
    # 只要边缘集合不为空，就继续搜索
    while frontier:
        # 从队列左侧弹出最早加入的路径
        node = frontier.popleft()
        
        # 目标测试：如果当前路径的最后一个节点等于目标状态，则返回该路径
        if (node.endswith(goalState)): return node
        
        # 检查当前节点 (node[-1]) 是否已经被探索过
        if node[-1] not in exploredSet:
            # 如果未被探索过，则将其加入探索集
            exploredSet.add(node[-1])
            
            # 遍历该节点的所有邻接子节点
            # 将当前路径与子节点拼接形成新路径，并加入队列的右侧末尾
            for child in stateSpaceGraph[node[-1]]: frontier.append(node+child)
```

### 2.1.3 罗马尼亚地图示例

```python
# 罗马尼亚地图的状态空间图，使用字典邻接表表示
# 键为节点（城市首字母），值为该节点可达的相邻子节点列表
romania = {
    'A':['S','T','Z'],'Z':['A','O'],'O':['S','Z'],'T':['A','L'],'L':['M','T'],'M':['D','L'],
    'D':['C','M'],'S':['A','F','O','R'],'R':['C','P','S'],'C':['D','P','R'],
    'F':['B','S'],'P':['B','C','R'],'B':[]
    }
    
# 调用树搜索算法，寻找并打印从起始点 'A' (Arad) 到目标点 'B' (Bucharest) 的解路径
print('Solution path:',bfsTsa(romania, 'A', 'B'))
```

### 2.1.4 Will bfsTsa(romania, 'A', 'B') terminate ? 

程序能够终止的核心原因有两个：

目标是可达的：在图中，从起点 'A' 到终点 'B' 是存在路径的（例如最短路径之一是 A -> S -> F -> B）。

BFS 的层级遍历特性：广度优先搜索是一层一层向外扩展的。

第一层：AS, AT, AZ

第二层：ASA, ASF, ASO, ASR... (这里出现了环产生的重复状态)

第三层：... ASFB ...

虽然树搜索会因为环产生无限多的重复路径（比如无限循环 ASASAS...），但BFS 保证了它一定会先搜完所有较短的路径，再去搜较长的路径。

当算法搜到第 3 层时，会将生成的目标路径 'ASFB' 加入队列。当从队列左侧弹出 'ASFB' 时，node.endswith('B') 条件满足，程序就会直接 return node 并终止运行。

### 2.1.5 什么情况下 bfs-tsa 陷入循环

这种算法会在**同时满足以下两个条件时**，陷入无限循环（死循环），最终导致内存耗尽或永远挂起：

1  图中存在“环”（Cycles）或双向边
原因：因为算法没有记忆功能，它不知道自己“来过这里”。如果图中存在 A -> S 且 S -> A 的路线，算法就会在搜索树中生成诸如 A、AS、ASA、ASAS、ASASA…… 这样长度可以无限延伸的路径。

(反之，如果图是一个完全没有环的有向无环图或严格的树状结构，即使找不到目标，算法也会在遍历完所有路线后乖乖停止。)

2 目标状态（Goal State）是“不可达的”（Unreachable）
原因：正如我们之前讨论的，如果目标是可达的，BFS 的特性（按路径长度逐层搜索）保证了它一定会在陷入无限深的死循环之前，在较浅的层级提前找到目标并结束程序。

但是，如果目标不可达（例如目标节点在图中不存在，或者起点和终点根本没有道路相连），BFS 就会为了寻找这个不可能存在的目标，不断地在环里绕圈子。它会把越来越长的重复路径加入 frontier 队列，永无止境。

---

## 2.2 深度优先搜索 (DFS)

### 2.2.1 图搜索版本 (Graph Search)


```python
import collections

# dfsGsa: 深度优先图搜索算法 (DFS Graph Search Algorithm)
# 利用 LIFO (后进先出) 机制扩展最深层的节点
def dfsGsa(stateSpaceGraph, startState, goalState):
    # 使用双端队列初始化边缘集合，存放初始路径
    frontier = collections.deque([startState])
    
    # 初始化探索集为空集合 (set)，用于避免重复访问
    exploredSet = set()
    
    # 只要边缘集合不为空，就继续搜索
    while frontier:
        # ⚠️ 关键区别：使用 pop() 从队列右侧（队尾）弹出最新加入的路径，实现 LIFO (栈结构)
        node = frontier.pop()
        
        # 目标测试：如果当前路径的最后一个节点等于目标状态，则返回该路径
        if (node.endswith(goalState)): return node
        
        # 检查当前节点是否已经被探索过
        if node[-1] not in exploredSet:
            
            # 标记为已探索
            exploredSet.add(node[-1])
            
            # 扩展节点，将新路径加入边缘集合的右侧末尾
            for child in stateSpaceGraph[node[-1]]: frontier.append(node+child)
```

### 2.2.2 树搜索版本 (Tree Search)

仿照 `dfsGsa` 和之前 `bfsTsa` 的代码风格，我们可以推导出 `dfsTsa`（深度优先树搜索）的代码。核心在于去除 `exploredSet` 相关逻辑，并保持使用 `pop()` 的 LIFO 特性。去除了教学演示代码使其更简洁：

```python
import collections

# dfsTsa: 深度优先树搜索算法 (DFS Tree Search Algorithm)
# 仿照课件风格去除了图搜索中的 exploredSet 以及演示用的 print/input 逻辑
def dfsTsa(stateSpaceGraph, startState, goalState):
    # 初始化边缘集合
    frontier = collections.deque([startState])
    
    # 只要边缘集合不为空，就继续搜索
    while frontier:
        # 使用 pop() 弹出最深层（最近加入）的节点路径，实现深度优先 (LIFO)
        node = frontier.pop()
        
        # 目标测试
        if (node.endswith(goalState)): return node
        
        # 遍历子节点，将新路径压入队尾 (栈顶)
        for child in stateSpaceGraph[node[-1]]: frontier.append(node+child)
```

---

## 2.3 BFS & DFS 性质总结

**基础参数定义：**
* **b**: 搜索树的最大分支因子 (maximum branching factor of the search tree)
* **d**: 距离根节点最浅（最近）的解所在的深度 (depth of the shallowest solution)
* **m**: 状态空间中任何路径的最大长度/深度 (maximum depth of the state space)

### 2.3.1 DFS 与 BFS 属性对比 (Properties)

| 评估维度 | 深度优先搜索 (DFS - 树搜索) | 广度优先搜索 (BFS) |
| :--- | :--- | :--- |
| **完备性 (Complete)** | **否 (No)** - 如果树的深度无限或存在环，可能会陷入无限向下探索的死循环。 | **是 (Yes)** - 只要最大分支因子 $b$ 是有限的，总能找到解。 |
| **最优性 (Optimal)** | **否 (No)** - 它会返回找到的第一个解，该解未必是成本最低或距离最短的。 | **是 (Yes)** - 前提是每一步的动作成本 (step cost) 都相同。 |
| **时间复杂度 (Time)** | $O(b^m)$ - 最坏情况下会探索整个极其庞大的状态空间。 | $O(b^d)$ - 需要探索所有深度至 $d$ 的节点（有时记为 $O(b^{d+1})$）。 |
| **空间复杂度 (Space)**| **$O(b \times m)$ (极大优势)** - **线性内存**，只需存储当前路径上的节点及其未展开的兄弟节点。 | **$O(b^d)$ (极大劣势)** - **指数级内存**，必须在内存中保留搜索边界上的所有节点。 |

### 2.3.2 性能对比：何时表现更好？ (BFS vs. DFS)

#### ➢ 什么时候 BFS 会优于 DFS？ (When will BFS outperform DFS?)
* **解比较浅时 (Shallow solution)**：当目标状态距离初始状态很近时，BFS 能逐层迅速找到，而 DFS 可能会在一条错误的深分支上浪费大量时间。
* **需要保证找到最短路径时**：BFS 基于层级推进，保证能找到步骤最少的解（最优性）。
* **面临无限深度的状态空间时**：DFS 很容易在无限深的分支中迷失，而 BFS 的逐层排查保证了只要解存在就一定能找到（完备性）。

#### ➢ 什么时候 DFS 会优于 BFS？ (When will DFS outperform BFS?)
* **内存空间极其有限时**：这是 DFS 最大的优势。它的空间开销是线性的，而 BFS 的指数级内存开销极易导致内存耗尽 (Out of Memory)。
* **解非常密集且处于树的深层时**：如果很多分支的深处都存在解，DFS 可以顺着一条路快速“下潜”直达目标。
* **搜索树的深度 $m$ 是有限的**：并且我们的核心诉求是“找到任意一个解”而不是“寻找最优解”。

### 2.2.3 性质补充

在《人工智能：一种现代方法》(AIMA) 等经典理论中，BFS（广度优先搜索）和 DFS（深度优先搜索）的**完备性（Completeness）**以及**何时陷入无限循环**，完全取决于它们是置于 TSA 还是 GSA 的框架下运行。

以下是完整的对比与总结：

#### 1. 核心底层逻辑：TSA 与 GSA 的区别
* **TSA (树搜索算法)**：**不维护**“已访问节点集”（Explored Set / Closed List）。即使遇到图结构中的环（Cycle）或双向边，它也会将其盲目展开为一棵深度无限的分支。
* **GSA (图搜索算法)**：**维护**“已访问节点集”。在扩展新节点前，会先检查该状态是否已被访问，从而实现剪枝，有效避免在环路中重复绕圈。

#### 2. 完备性与循环机制对比

##### **BFS（广度优先搜索）**
* **完备性**：**完备**。只要分支因子 $b$ 是有限的，BFS 总能找到解。
* **陷入循环的情况**：**极难陷入路径层面的死循环**。因为 BFS 是逐层（Level-by-level）推进的。无论是使用 TSA 还是 GSA，它都不会在一条具有环路的路径上无限深挖。它最终一定能在有限的层数内扫到最浅的目标。BFS 的瓶颈通常是空间复杂度（内存爆满），而不是陷入无限循环。

**什么情况下 bfs-tsa 陷入循环**

这种算法会在**同时满足以下两个条件时**，陷入无限循环（死循环），最终导致内存耗尽或永远挂起：

1  图中存在“环”（Cycles）或双向边
原因：因为算法没有记忆功能，它不知道自己“来过这里”。如果图中存在 A -> S 且 S -> A 的路线，算法就会在搜索树中生成诸如 A、AS、ASA、ASAS、ASASA…… 这样长度可以无限延伸的路径。

(反之，如果图是一个完全没有环的有向无环图或严格的树状结构，即使找不到目标，算法也会在遍历完所有路线后乖乖停止。)

2 目标状态（Goal State）是“不可达的”（Unreachable）
原因：正如我们之前讨论的，如果目标是可达的，BFS 的特性（按路径长度逐层搜索）保证了它一定会在陷入无限深的死循环之前，在较浅的层级提前找到目标并结束程序。

但是，如果目标不可达（例如目标节点在图中不存在，或者起点和终点根本没有道路相连），BFS 就会为了寻找这个不可能存在的目标，不断地在环里绕圈子。它会把越来越长的重复路径加入 frontier 队列，永无止境。


##### **DFS（深度优先搜索）**
DFS 的命运与 TSA/GSA 紧密绑定，因为它是“不撞南墙不回头”的策略：

* **在 TSA（树搜索）下**：
    * **完备性**：**不完备**。
    * **何时陷入循环**：只要状态空间图中存在**任何环路**（例如 $A \to B \to A$）或无向边，DFS 就会将其视为不断延伸的新路径。此时 DFS 瞬间陷入局部无限循环，沿着这个环无休止地走下去，永远无法回溯，也就永远找不到其实近在咫尺的目标。
* **在 GSA（图搜索）下**：
    * **完备性**：在**有限状态空间**中完备；在**无限状态空间**中依然**不完备**。
    * **何时陷入循环**：由于 GSA 引入了已访问节点集，$A \to B \to A$ 的绕圈问题被彻底解决，DFS 不会再因为“环路”而死循环。**但是**，如果面临的是一个**深度无限且没有环路**的图（例如不断向右生成新状态 $1 \to 2 \to 3 \dots \to \infty$），DFS 依然会一条路走到黑，陷入广义上的“无限深渊”，从而错过其他较浅分支上的正确解。

#### 3. 完整总结表格

| 算法特性 | BFS (广度优先) | DFS (深度优先) |
| :--- | :--- | :--- |
| **搜索策略** | 逐层铺开（使用 FIFO 队列） | 沿着单条路径探到底（使用 LIFO 栈） |
| **完备性 (TSA)**| 完备 (假设分支数 $b$ 有限) | **不完备** (极其脆弱，遇环即死循环) |
| **完备性 (GSA)**| 完备 (假设分支数 $b$ 有限) | 有限空间完备，无限空间不完备 |
| **陷入循环的触发点**| 几乎不会，通常先死于内存溢出 | 遇到环或无向边 (TSA)；或遇到无限深的分支 (TSA & GSA) |
| **与 TS/GSA 的关联**| 影响不大，逐层遍历天然免疫环路死循环 | **极其关键**，引入 GSA 是挽救 DFS 免于环路死循环的唯一方式 |

---

## 2.4 一致代价搜索 (UCS)

### 2.4.1 树搜索版本 (Tree Search)

```python
from heapq import heappush, heappop

# ucsTsa: 一致代价树搜索算法 (Uniform Cost Tree Search Algorithm)
# stateSpaceGraph: 带权状态空间图
# startState: 起始状态
# goalState: 目标状态
def ucsTsa(stateSpaceGraph, startState, goalState): 
    # 初始化优先队列 (优先队列使用堆结构实现)
    frontier = []
    # 压入初始状态，元组的第一个元素为路径总代价(0)，第二个元素为路径(startState)
    # heappush 会根据元组的第一个元素（代价）自动进行升序排序
    heappush(frontier, (0, startState))
    
    # 只要优先队列不为空，就继续搜索
    while frontier:
        # 弹出代价最小的路径节点
        node = heappop(frontier)
        
        # 目标测试：如果路径的最后一个节点等于目标状态，则返回该路径及代价值
        # node[0] 为路径总代价，node[1] 为路径字符串
        if (node[1].endswith(goalState)): return node
        
        # 遍历当前节点的所有邻接子节点
        # stateSpaceGraph 中的子节点格式应为 (路径成本, 目标节点)
        for child in stateSpaceGraph[node[1][-1]]:
            # 将新路径及其累加的总代价压入优先队列
            # 新的总代价 = 当前路径总代价 (node[0]) + 边代价 (child[0])
            # 新路径 = 当前路径 (node[1]) + 子节点名称 (child[1])
            heappush(frontier, (node[0]+child[0], node[1]+child[1]))
```

### 2.4.2 图搜索版本 (Graph Search)

```python
from heapq import heappush, heappop

# ucsGsa: 一致代价图搜索算法 (Uniform Cost Graph Search Algorithm)
def ucsGsa(stateSpaceGraph, startState, goalState): 
    # 初始化优先队列
    frontier = []
    # 压入初始状态及代价
    heappush(frontier, (0, startState))
    
    # 初始化探索集为空集合，避免重复访问已扩展的节点
    exploredSet = set()
    
    while frontier:
        # 弹出当前代价最小的路径节点
        node = heappop(frontier)
        
        # 目标测试
        if (node[1].endswith(goalState)): return node
        
        # 图搜索特有逻辑：检查当前节点是否已经被探索过
        # node[1][-1] 为当前路径的最后一个节点（当前所在节点）
        if node[1][-1] not in exploredSet:
            # 如果未被探索过，则将其标记为已探索
            exploredSet.add(node[1][-1])
            
            # 遍历该节点的所有邻接子节点
            for child in stateSpaceGraph[node[1][-1]]:
                # 累加路径代价，并压入新的完整路径到优先队列中
                heappush(frontier, (node[0]+child[0], node[1]+child[1]))
```

### 2.4.3 罗马尼亚带权地图示例

```python
# 罗马尼亚地图的带权状态空间图，使用字典邻接表表示
# 键为节点，值为 (边代价, 目标节点) 的元组列表
romania = {
    'A':[(140,'S'),(118,'T'),(75,'Z')], 'Z':[(75,'A'),(71,'O')], 'O':[(151,'S'),(71,'Z')],
    'T':[(118,'A'),(111,'L')], 'L':[(70,'M'),(111,'T')], 'M':[(75,'D'),(70,'L')], 
    'D':[(120,'C'),(75,'M')], 'S':[(140,'A'),(99,'F'),(151,'O'),(80,'R')], 
    'R':[(146,'C'),(97,'P'),(80,'S')], 'C':[(120,'D'),(138,'P'),(146,'R')], 
    'F':[(211,'B'),(99,'S')], 'P':[(101,'B'),(138,'C'),(97,'R')], 'B':[]
}

# 调用一致代价图搜索算法，寻找并打印从起始点 'A' 到目标点 'B' 的最低代价解路径
print('Solution path:', ucsGsa(romania, 'A', 'B'))
```

### 2.4.4 Uniform Cost Search 特性总结

**基础参数定义：**
* **C***: 最优解的成本 (Cost of the optimal solution)
* **ε** (epsilon): 任何动作的最小正向成本 (Minimum positive step cost)。假设 ε > 0。
* **b**: 搜索树的最大分支因子 (maximum branching factor)

#### UCS 属性 (Properties)

| 评估维度 | 统一代价搜索 (UCS) |
| :--- | :--- |
| **完备性 (Complete)** | **是 (Yes)** - 前提是每一步的动作成本都严格大于一个正常数 ε（即没有零成本或负成本的死循环），且分支因子 b 是有限的。 |
| **最优性 (Optimal)** | **是 (Yes)** - UCS 总是严格按照路径成本递增的顺序（利用优先队列）扩展节点。因此，它找到的第一个目标节点一定具有最小的路径成本。 |
| **时间复杂度 (Time)** | **O(b^(1 + floor(C*/ε)))** - 在最坏情况下，算法需要探索所有成本小于最优解成本 C* 的路径。可以把 `C*/ε` 理解为搜索的“有效深度”。 |
| **空间复杂度 (Space)**| **O(b^(1 + floor(C*/ε)))** - 极大的劣势。算法必须在优先队列 (Frontier) 和已探索集合 (Explored set) 中将所有生成的节点保存在内存中。 |

#### 补充说明 (Notes)
* **与 BFS 的关系**: 如果所有动作的成本 (step costs) 都相等，那么 UCS 的行为就和广度优先搜索 (BFS) 完全一样。此时有效深度就等于解的实际深度 d，时间/空间复杂度也就退化为了 O(b^d)。
* **本质**: UCS 实质上就是应用于图搜索的 Dijkstra 算法（通常 Dijkstra 用于寻找从单源到所有节点的最短路径，而 UCS 在找到目标节点后就会提前终止）。

---

# 3 Informed Search

## 3.1 基本概念
### 3.1.1 有信息搜索 (Informed Search)
* **核心优势**: 有信息搜索策略通常比无信息搜索（盲目搜索）能更高效地找到解决方案。
* **特征**: 它们不仅使用问题的基本定义，还引入了**特定问题的额外知识 (problem specific knowledge)**。
  * 引入知识的核心方式是使用**启发式函数 (Heuristic function)**。
* **常见算法示例**:
  * 贪婪最佳优先搜索 (Greedy best-first search)
  * A* 搜索 (A* search)

### 3.1.2 启发式函数 (Heuristic Function)
* **基本定义**: 一个用于估计当前状态距离目标状态还有多远的函数。
* **特点**: 它是为某个特定的搜索问题量身定制的。
* **数学表示 h(n)**:
  * h(n) 表示从节点 n 当前的状态到达目标状态的最优路径的**成本估计值 (Cost estimate)**。
  * **边界条件**: 如果节点 n 本身就是一个目标节点，那么它的启发式估计值为零，即 h(n) = 0。

---

## 3.2 贪婪搜索 (Greedy Search)

### 3.2.1 基本概念

* **别名**: 也常被称为最佳优先搜索 (Best-first Search)。
* **搜索策略**: 总是优先扩展具有**最低 h(n) 值**的节点（即每次都选看起来离目标最近的那条路）。
* **潜在风险 (What can possibly go wrong?)**: 
  * 这种策略过于“短视”，因为它只关注未来估计的成本，而忽略了过去已经花费的成本。这可能导致它陷入死胡同、在障碍物前绕弯路，或者最终找到的解并非最优解。

### 3.2.2 树搜索版本 (Tree Search)

```python
from heapq import heappush, heappop

# greedyTsa: 贪婪树搜索算法 (Greedy Tree Search Algorithm)
# stateSpaceGraph: 状态空间图 (邻接表)
# h: 启发式函数字典 (存储每个节点到目标节点的预估代价)
# startState: 起始状态
# goalState: 目标状态
def greedyTsa(stateSpaceGraph, h, startState, goalState):
    # 初始化优先队列
    frontier = []
    # 压入初始状态。在贪婪搜索中，排序的唯一依据是启发式函数的值 h(n)
    # 元组的第一个元素是 h[startState]（即离目标的预估距离），第二个元素是路径
    heappush(frontier, (h[startState], startState))
    
    # 当优先队列不为空时循环
    while frontier:
        # 弹出启发式预估代价最小的节点（即看起来离目标最近的节点）
        node = heappop(frontier)
        
        # 目标测试
        if (node[1].endswith(goalState)): return node
        
        # 遍历当前节点 (node[1][-1]) 的所有邻接子节点
        # 注意此处的 stateSpaceGraph 格式无需包含边代价，或即使有也不参与计算
        for child in stateSpaceGraph[node[1][-1]]:
            # 根据子节点的启发式值 h[child[1]] 决定其在优先队列中的优先级
            # child[1] 为子节点名称
            heappush(frontier, (h[child[1]], node[1]+child[1]))
```

### 3.2.3 罗马尼亚带启发式地图示例

```python
# 罗马尼亚地图的状态空间图（包含边代价，但贪婪搜索不使用边代价）
romania = {
    'A':[(140,'S'),(118,'T'),(75,'Z')],'Z':[(75,'A'),(71,'O')],'O':[(151,'S'),(71,'Z')],
    'T':[(118,'A'),(111,'L')],'L':[(70,'M'),(111,'T')],'M':[(75,'D'),(70,'L')],
    'D':[(120,'C'),(75,'M')],'S':[(140,'A'),(99,'F'),(151,'O'),(80,'R')],
    'R':[(146,'C'),(97,'P'),(80,'S')],'C':[(120,'D'),(138,'P'),(146,'R')],
    'F':[(211,'B'),(99,'S')],'P':[(101,'B'),(138,'C'),(97,'R')],'B':[]
}

# 罗马尼亚地图的启发式函数表：各个城市到布加勒斯特 (Bucharest) 的直线距离预估
romaniaH = {
    'A':366,'B':0,'C':160,'D':242,'E':161,'F':176,'G':77,'H':151,'I':226,
    'L':244,'M':241,'N':234,'O':380,'P':100,'R':193,'S':253,'T':329,'U':80,
    'V':199,'Z':374
}

# 调用贪婪搜索算法
print('Solution path:', greedyTsa(romania, romaniaH, 'A', 'B'))
```

---

## 3.3 A* 搜索 (A* Search)

### 3.3.1 基本概念

* **核心排序逻辑**: 为了解决贪婪搜索的短视问题，A* 算法结合了**向后成本 (backward cost)** 和 **向前成本估计 (forward cost)** 来对节点进行排序和选择。
* **评估函数 f(n)**:
  * **f(n) = g(n) + h(n)**
  * **g(n)**: 向后成本，即从初始状态走到当前节点 n **已经实际花费的成本**。
  * **h(n)**: 向前成本，即从节点 n 走到目标状态的**启发式估计成本**。
  * A* 每次都会选择总体预估成本 f(n) 最小的节点进行扩展。


### 3.3.2 树搜索版本 (Tree Search)

```python
from heapq import heappush, heappop

# aStarTsa: A* 树搜索算法 (A* Tree Search Algorithm)
# stateSpaceGraph: 带权状态空间图 (子节点格式为: (边代价, 节点名))
# h: 启发式函数字典
# startState: 起始状态
# goalState: 目标状态
def aStarTsa(stateSpaceGraph, h, startState, goalState):
    # 初始化优先队列
    frontier = []
    # 压入初始状态。优先队列排序依据是 f(n) = g(n) + h(n)
    # 起点时 g(startState) = 0，因此初始优先级直接为 h[startState]
    heappush(frontier, (h[startState], startState))
    
    while frontier:
        # 弹出 f(n) 最小的节点
        # 此时 node[0] 就是当前节点的 f(n) 值，node[1] 是路径字符串
        node = heappop(frontier)
        
        # 目标测试
        if (node[1].endswith(goalState)): return node
        
        # 遍历当前所在节点 (node[1][-1]) 的所有邻接子节点
        for child in stateSpaceGraph[node[1][-1]]:
            # 【核心代价计算逻辑解析】：
            # 新节点的评估函数 f(n') = g(n') + h(n')
            # 1. 已知当前节点的优先级 node[0] = f(n) = g(n) + h(n)
            # 2. 我们可以反推出当前的实际代价 g(n) = node[0] - h[node[1][-1]]
            # 3. 子节点的实际代价 g(n') = g(n) + 边代价 (child[0])
            # 4. 所以 f(n') = (node[0] - h[node[1][-1]]) + child[0] + h[child[1]]
            # 这种巧妙的写法避免了在队列中额外单独保存 g(n)
            new_f_cost = node[0] + child[0] - h[node[1][-1]] + h[child[1]]
            
            # 将子节点压入优先队列
            heappush(frontier, (new_f_cost, node[1]+child[1]))
```

### 3.3.3 A* 算法的最优性

#### 启发式的可采纳性 (Admissibility of Heuristic)
* **定义**: 一个可采纳的启发式函数 $h(n)$ 是**乐观的 (optimistic)**，它永远不会高估到达目标的实际成本。
* **数学表达**: 对于所有的节点 $n$，必须满足：
  $$0 \le h(n) \le h^*(n)$$
  其中，$h^*(n)$ 是从节点 $n$ 到达最近目标节点的**真实最小成本**。
* **通俗理解**: 启发式函数给出的估计距离，一定要比实际走过去的距离短（或刚好相等），也就是“认为情况总是比实际更好”。

#### 启发式的一致性/单调性 (Consistency of Heuristic)
* **定义**: 一致性是比可采纳性更严格的条件。它要求沿着任何路径的启发式成本的下降幅度，不能超过这两点之间的实际移动成本（类似三角形不等式）。
* **数学表达**: 对于任意节点 $a$ 及其通过动作到达的后继节点 $c$：
  $$h(a) - h(c) \le \text{cost}(a \to c)$$
  或者写作：
  $$h(a) \le \text{cost}(a \to c) + h(c)$$
* **一致性的推论 (Consequence)**: 
  * 沿着任何一条路径，总成本估计值 $f(n) = g(n) + h(n)$ **永远不会递减 (never decreases)**。
  * **关系**: 如果一个启发式函数是一致的，那么它必定也是可采纳的。但可采纳的启发式函数不一定是一致的。

#### A* 在树搜索 (A*-TSA) 中的最优性
* **条件**: 只要启发式函数是 **可采纳的 (Admissible)**，A*-TSA 就是最优的。
* **原因**: 树搜索不记录已访问的节点。因为 $h(n)$ 是乐观的，最优目标节点在被扩展之前，其祖先节点的 $f$ 值一定小于任何次优目标节点的 $f$ 值。因此，A* 总是会先扩展并找到最优解。

#### A* 在图搜索 (A*-GSA) 中的最优性
* **条件**: 启发式函数必须是 **一致的 (Consistent)**，A*-GSA 才是最优的。
* **原因**: 图搜索 (GSA) 会维护一个已探索集合 (Explored set) 以避免重复扩展。
  * 如果 $h(n)$ 仅仅是可采纳的而不一致，A* 可能会通过一条次优路径先到达并扩展某个节点 $n$，将其加入 Explored set。当稍后发现到达 $n$ 的更优路径时，由于 $n$ 已经被探索过，GSA 会忽略这条更优的路径，从而可能导致最终解并非最优。
  * 如果 $h(n)$ 是**一致的**，$f$ 值单调递增，这保证了**当 A* 第一次扩展某个节点 $n$ 时，它找到的就是到达该节点 $n$ 的最优（成本最低）路径**。因此，A*-GSA 不会遗漏最优路径。

### 3.3.4 重复访问问题

在 A* 搜索算法中，要想保证绝对不重复访问（revisit / re-expand）已经弹出的节点，必须同时满足两个核心条件：
**使用图搜索（Graph Search）架构 + 启发函数 $h(n)$ 是满足一致性（Consistent / Monotone）的。**

## 3.4 性质总结

### 1. 核心底层逻辑：评价函数 $f(n)$
* **Greedy Search**: $f(n) = h(n)$
  * **逻辑**：极度短视，只看未来。它总是扩展当前看起来离目标最近的节点（基于启发函数 $h(n)$ 的估计值），完全不考虑从起点走到当前节点已经花了多少代价。
* **A* Search**: $f(n) = g(n) + h(n)$
  * **逻辑**：统筹全局，平衡过去与未来。它不仅考虑未来的估计代价 $h(n)$，还加上了已经实际发生的代价 $g(n)$。这使得 A* 既有目标导向性，又不会盲目走入高代价的歧途。

### 2. 算法性质对比总结表格

| 算法特性 (Property) | 贪婪最佳优先搜索 (Greedy) | A* 搜索 (A*) |
| :--- | :--- | :--- |
| **评价函数** | $f(n) = h(n)$ | $f(n) = g(n) + h(n)$ |
| **完备性 (Complete)** | **否** (在 TSA 下遇环死循环) <br> *有限空间 GSA 下完备* | **是** <br> *(前提：分支因子有限，且单步代价 $\ge \epsilon > 0$)* |
| **最优性 (Optimal)** | **否** | **是** <br> *(前提：树搜索下 $h(n)$ 可采纳；图搜索下 $h(n)$ 一致)* |
| **时间复杂度 (Time)** | $O(b^m)$ 最坏情况 | $O(b^d)$ 最坏情况为指数级 |
| **空间复杂度 (Space)** | $O(b^m)$ 最坏情况 | $O(b^d)$ 指数级，**内存耗尽是其最大瓶颈** |

> **参数说明**：
> * $b$ = 搜索树的分支因子 (Branching factor)
> * $m$ = 状态空间的最大深度 (Maximum depth)
> * $d$ = 最浅最优解的深度 (Depth of the optimal solution)


### 3. 性质详细解析

#### **完备性 (Completeness)**
* **Greedy Search**：通常被认为是**不完备**的。如果在树搜索（TSA）中运行，它很容易在一个局部最优的死胡同里来回弹跳（例如遇到环路），从而陷入无限循环。即使在图搜索（GSA）中，如果状态空间是无限的，它也可能沿着一条错误的无限路径越走越远。
* **A* Search**：**完备**。只要图中每个节点的后继节点数量（分支因子 $b$）是有限的，并且每一步的行动代价都有一个大于 $0$ 的下界（即代价 $\ge \epsilon > 0$），A* 就一定能找到目标。因为 $g(n)$ 会随着深度不断增加，A* 最终会被迫放弃那条无尽的路径，回头探索其他分支。

#### **最优性 (Optimality)**
* **Greedy Search**：**不最优**。因为它只关注眼前的 $h(n)$ 最小，极有可能绕远路。比如遇到一堵墙，它会沿着墙边一直走（因为看起来离目标近），而忽略了其实退后两步有一条更短的大道。
* **A* Search**：**最优**。这是 A* 最强大的特性，但有严格的前提条件：
    1. 如果使用树搜索（TSA），$h(n)$ 必须是**可采纳的（Admissible）**，即启发函数永远不会高估到达目标的实际代价（$h(n) \le h^*(n)$）。
    2. 如果使用图搜索（GSA），$h(n)$ 必须是**一致的/单调的（Consistent/Monotonic）**，即满足三角不等式：$h(n) \le c(n, a, n') + h(n')$。

#### **时间复杂度 (Time Complexity)**
* 两者的最坏情况时间复杂度都非常高（指数级）。
* **Greedy Search** 的时间复杂度高度依赖于启发函数 $h(n)$ 的质量。一个完美的启发函数可以将时间复杂度降到 $O(m)$，但最坏情况下（例如 $h(n)$ 给出极差的引导）它会遍历整个空间 $O(b^m)$。
* **A* Search** 的时间复杂度取决于启发函数的误差。除非 $h(n)$ 的误差随路径长度的增长呈对数级或更低，否则 A* 依然需要扩展指数级的节点。

#### **空间复杂度 (Space Complexity)**
* **这是 A* 算法最致命的弱点**。因为 A* 必须把所有生成过的节点保留在内存中（不仅在 Open List/Fringe 中排序，还要在 Closed List 中查重），所以它的空间复杂度也是 $O(b^d)$。在实际的复杂应用中，**A* 往往在耗尽时间之前，就已经先把内存撑爆了**（因此后续演化出了 IDA* 或 SMA* 等优化内存的算法）。
* **Greedy Search** 同样需要将节点保留在内存中，最坏情况下的空间复杂度为 $O(b^m)$。


---

# 4 Local Search

## 4.1 规划与识别 (Planning vs. Identification)
* **规划问题 (Planning)**: 侧重于**动作序列 (sequences of actions)**。
  * 到达目标状态的**路径 (Path)** 是最重要的。
  * 不同的路径具有不同的成本 (costs) 和深度 (depths)。
  * 通常需要使用启发式函数 (Heuristics) 来引导搜索，并使用搜索边界 (Frontier) 来保留备选路径。
* **识别问题 (Identification)**: 侧重于**变量赋值 (assignments to variables)**。
  * **目标状态本身**是最重要的，而到达该状态的路径并不重要。
* **结论**: 对于特定类型的识别问题，局部搜索 (Local Search) 往往能以更快的速度找到解决方案。

## 4.2 局部搜索 (Local Search)
* **核心思想**: 算法只保留一个（或少数几个）**当前状态**，对其进行评估和修改，而不是系统性地从初始状态展开多条搜索路径。
* **适用场景**: 非常适合那些“只关心最终解是什么样，而完全不在乎是怎么走到这一步的（路径成本）”的问题。
* **两大核心优势**: 尽管局部搜索算法不具有系统性（不保证能探索完全部空间），但它们在实际应用中极为有效：
  1. **极低的内存消耗**: 通常只需要常量级别的内存，因为它不需要记住搜索树或已探索的节点。
  2. **应对庞大空间**: 经常能在规模极其巨大的状态空间中，快速寻找到合理的解决方案。

---

# 5 Constraint Satisfaction Problems, 

## 5.1 基本概念
### 5.1.1 CSP 的核心概念与优势
* **因子化表示 (Factored representation)**: CSPs 对状态使用因子化表示，即状态被分解为一组**变量 (Variables)**，每个变量都可以被赋予一个**值 (Value)**。
* **求解目标**: 当所有的变量都被赋予了满足特定**约束 (Constraints)** 的值时，问题即被解决。
* **高效性**: 相比于普通的搜索算法，CSPs 通常能更高效地求解。因为它们能够通过及早识别出违反约束的“变量/值”组合，从而直接**消除极大部分的搜索空间 (eliminate large portions of the search space)**。

### 5.2 CSP 的严格定义 (Defining CSPs)
一个标准的约束满足问题主要由以下三个基本组件构成：
* **变量集合 (Variables)**: $X = \{X_1, ..., X_n\}$
* **值域集合 (Domains)**: $D = \{D_1, ..., D_n\}$。其中 $D_i = \{v_1, ..., v_k\}$ 代表变量 $X_i$ 可以选取的全部候选值的集合。
* **约束集合 (Constraints)**: $C$。它明确规定了变量之间被允许的值的组合方式。

**状态空间的定义**:
* 在求解 CSP 时，一个**状态 (State)** 是通过为部分或全部变量赋值来定义的，形式如：$\{X_i = v_i, X_j = v_j, ...\}$。

### 5.3 CSP 的解决方案 (Solutions to CSPs)
评估一个赋值是否为 CSP 的最终解，需要依赖以下几个概念：
* **一致的赋值 (Consistent assignment)**: 如果当前的变量赋值**没有违反任何约束**，我们称这种赋值是一致的（或合法的）。
* **完整的赋值 (Complete assignment)**: 如果问题中的**每一个变量**都已经被分配了一个值，我们称这种赋值是完整的。
* **最终解 (Solution)**: CSP 的最终解决方案，必须是一个**既一致又完整 (both consistent and complete)** 的赋值（即所有变量都有值，且没有任何冲突）。

---

## 5.2 回溯搜索
### 5.2.1 回溯搜索 (Backtracking Search)
* **定义**: 解决约束满足问题 (CSPs) 的基本算法。
* **核心思想**: 
  1. **每次只考虑一个变量的赋值**: 因为变量赋值具有交换律 (commutative)，顺序不影响最终结果，所以搜索树的每个节点只需要展开一个变量。
  2. **每次只允许合法的赋值**: 只考虑那些与先前已赋值变量**不冲突**的值（即增量目标测试）。
* **结论**: 将上述两个思想结合到**深度优先搜索 (DFS)** 中，就形成了回溯搜索。

### 5.2.2 改进回溯搜索 (Improving Backtracking)
* **核心动机**: 能否尽早发现“不可避免的失败”以减少无谓的搜索？(Can we detect inevitable failure early?)
* **两大主要策略**:
  1. 前向检查 (Forward Checking, FC)
  2. 约束传播 (Constraint propagation, 如 AC-3 算法)

### 5.2.3 过滤与前向检查 (Filtering & Forward Checking)
* **过滤 (Filtering) 的概念**: 持续跟踪未赋值变量的值域 (domains)，并及时划掉（剔除）那些肯定会导致失败的坏选项。
* **前向检查 (Forward Checking)**: 
  * 当给当前变量分配一个值后，立刻检查与其相关的未赋值变量。
  * 将那些加入当前赋值后会**违反约束的值**，从未来变量的值域中划掉。

### 5.2.4 弧一致性与约束传播 (Arc Consistency & Constraint Propagation)
#### 弧一致性 (Consistency of an Arc)
* **定义**: 对于一条有向弧 $X \rightarrow Y$（表示变量 X 依赖于变量 Y），当且仅当对于尾部 X 的值域中的**每一个**值 $x$，在头部 Y 的值域中都存在**至少一个**值 $y$ 可以与其合法组合（不违反约束）时，这条弧就是一致的。
* **核心操作**: 如果 X 中某个值 $x$ 在 Y 中找不到任何合法的 $y$ 来匹配，就必须把这个 $x$ **从尾部 X 的值域中删除** ("Delete from tail!")。

#### 约束传播 (Constraint Propagation)
* **机制**: 通过不断地强制执行约束，使整个约束网络达到一致状态。
* **连锁反应**: 弧的状态可能会因为其他操作变得不一致。**如果变量 X 的值域中丢失了一个值，那么 X 的所有邻居变量都需要被重新检查**，因为它们原本依赖于 X 的某些合法组合可能已经不复存在了。
* **优势与应用**:
  * 相比于前向检查，弧一致性能**更早地**探测到失败路径。
  * 它可以作为搜索前的预处理步骤运行，也可以在回溯搜索的每一步赋值之后运行以加速搜索。


### 5.2.5 变量排序 (Variable Ordering) - 决定“先处理谁”

在解决约束满足问题 (CSP) 时，除了及早发现失败（如前向检查），我们还可以通过聪明地决定**下一步先给哪个变量赋值**以及**给这个变量赋什么值**来大幅提升搜索效率。

#### 最少剩余值启发式 (Minimum Remaining Values, MRV)
* **核心策略**: 优先选择其值域中**剩余合法选项最少**的变量进行赋值。
* **别名与动机**:
  * **受限最严重的变量 (Most constrained variable)**: 它能挑出当前选择最局促的变量。
  * **最先失败启发式 (Fail-first heuristic)**: 这是一个非常重要的思想。通过优先处理最容易无路可走的变量，如果注定要失败，就能尽早触发回溯 (Fail early)，从而避免在注定失败的搜索树分支上浪费大量时间。

#### 度启发式 (Degree Heuristic, Deg) - MRV 的平局决胜
* **应用场景**: 当使用 MRV 发现有多个变量剩余的合法值数量相同时，用来打破僵局 (Tie-breaker)。
* **核心策略**: 选择对其他**尚未赋值的剩余变量**拥有**最多约束**的变量。
* **目的**: 优先处理牵涉最广的变量，可以有效地减少其他剩余变量的值域，从而加速后续的搜索过程。


### 5.2.6 值排序 (Value Ordering) - 决定“先尝试哪个值”

#### 最少约束值启发式 (Least Constraining Value, LCV)

* **核心策略**: 针对已经选定的变量，在尝试赋值时，优先选择那个**排除掉（划掉）剩余变量最少合法选项**的值。
* **动机**: 
  * 与变量排序追求的“尽早失败”策略截然相反，值排序追求的是**“尽最大努力一次成功”**。
  * 选择最宽容、最不苛刻的值，可以为后续变量留下最大的灵活性和最多的选择余地，从而最大程度地避免触发回溯，增加直接找到最终解的概率。

---

# 6 Adversarial Search

## 6.1 基本概念
### 6.1.1 对抗搜索基础 (Adversarial Search)
* **环境特征**: 这是一个多智能体竞争环境 (multi-agent competitive environment)。
* **核心挑战**: 我们需要在这样一个世界中提前做计划 (plan ahead)：其他智能体同样也在做计划，并且他们的计划是**针对我们**的。
* **目标关系**: 各个智能体的目标通常是**冲突的**（零和博弈中必然冲突，但也并非绝对在所有博弈中都完全冲突）。

### 6.1.2 游戏的严格定义 (Game Definition)
一个正式的游戏（博弈）可以通过以下组件来定义：
* **s**: 状态集合 (States)
* **$s_0$**: 初始状态 (Initial state)
* **Player(s)**: 定义在状态 s 时，轮到哪个玩家行动。
* **Actions(s)**: 返回在状态 s 下所有合法的移动操作集合。
* **Result(s, a)**: 定义执行动作 a 后的结果状态（即转移模型）。
* **TerminalTest(s)**: 终止测试。如果游戏结束则返回 True，否则返回 False。
* **Utility(s, p)**: 效用函数（收益函数）。定义了游戏以状态 s 结束时，玩家 p 获得的最终数值收益。

**博弈树 (Game Tree)**:
基于以上定义，可以构建出一棵博弈树，其中**节点代表游戏状态**，**边代表移动动作**。

---

## 6.2 极小化极大算法原理 (Minimax Search)
### 6.2.1 基本属性
* **基本机制**: 
  * 在状态空间搜索树上进行。
  * 玩家交替进行回合 (Players alternate turns)。我们通常假设自己是 MAX 玩家，对手是 MIN 玩家。
* **计算 Minimax 值**: 
  * 算法的核心是计算每个节点的 minimax 值：即在面对一个完全理性的（会选择最优策略的）对手时，我们能获得的**最佳可实现的效用 (best achievable utility)**。
* **递归公式**:
  * 如果 s 是终止状态：`MINIMAX(s) = UTILITY(s)`
  * 如果轮到 MAX 玩家：`MINIMAX(s) = max(MINIMAX(RESULT(s, a)))` （遍历所有合法动作 a）
  * 如果轮到 MIN 玩家：`MINIMAX(s) = min(MINIMAX(RESULT(s, a)))` （遍历所有合法动作 a）

### 6.2.2 Minimax 的属性与表现 (Minimax Properties)

#### 最优性探讨
* **它能导致绝对的“最优游戏”吗？(Will minimax lead to optimal play?)**
  * **否 (No)**。因为在现实中，对手可能犯错，针对犯错的对手，可能存在能获取更高收益的“风险策略”。
* **它能导致最优策略吗？(It will lead to an optimal strategy)**
  * **是 (Yes)**。它的最优性是建立在**“对手完美无瑕” (optimal against perfect play)** 的假设上的。它保证了我们在最坏情况下的最佳收益 (Best achievable payoff against best play)。

#### 对手不完美的情况 (What if Min does not play optimally?)
* 如果 MIN 玩家没有采取最优策略（例如没有选择对 MAX 最不利的走法），那么 MAX 玩家在实际游戏中，**平均而言能够获得比 minimax 预测值更好的结果**。
* *(注：参考课件图例，若 MIN 犯错选择了右边分支，MAX 最终可能拿到 100 的收益，远超保守估计的 10)*

#### 复杂度分析 (Minimax performs a complete DFS exploration)
由于 Minimax 本质上是对整棵博弈树执行了一次完整的**深度优先搜索 (Complete DFS exploration)**，因此它的复杂度与 DFS 相同：
* **完备性 (Complete?)**: **是 (Yes)**，只要树的深度是有限的。
* **最优性 (Optimal?)**: **是 (Yes)**，对抗一个理性的对手时。
* **时间复杂度 (Time complexity)**: $O(b^m)$，极其庞大，需要遍历所有可能的棋局走向。
* **空间复杂度 (Space complexity)**: $O(b \times m)$ 或 $O(m)$，取决于具体实现，但它是线性的，这是深度优先搜索的优势。
  * *(其中 b 是最大分支因子，m 是游戏的最大深度)*


### 6.2.3 深度限制搜索 (Depth-Limited Search, DLS)
* **核心概念**: 它本质上是带有**深度限制**和**评估函数**的深度优先树搜索 (DFS-TSA)。
* **运行机制**: 
  * 算法只在搜索树中向下探索到有限的深度 `l` (Cut the tree here)。
  * 对于深度到达 `l` 的非终端节点，它不再继续生成后继节点，而是使用**评估函数 (Evaluation function)** 的得分来替代该位置的真实终端效用值 (Terminal utilities)。
* **DLS 的属性 (Properties)**:
  * **完备性 (Complete?)**: **否 (No)**。如果目标/解存在于深度限制 `l` 之下，算法将无法找到它。
  * **最优性 (Optimal?)**: **否 (No)**。因为使用了近似的评估函数而非搜索到真正的结局，**丧失了最优博弈的保证 (Guarantee of optimal play is gone)**。
  * **时间复杂度 (Time)**: $O(b^l)$ （其中 $b$ 为分支因子，$l$ 为深度限制）。
  * **空间复杂度 (Space)**: 继承了 DFS 的优势，为线性空间 $O(b \times l)$ 或 $O(l)$。
* **面临的主要挑战**: 必须人为设计一个高质量的评估函数。


### 6.2.4 评估函数 (Evaluation Function)
* **定义**: `Eval(s)` 用于在 DLS 中为非终端节点打分。它是对给定状态下，游戏**预期效用 (expected utility)** 的一种经验估计。
* **理想函数 (Ideal function)**: 最完美的评估函数给出的估值，应该完全等于该位置在计算到底时的**真实 Minimax 值**。
* **重要性**: 一个游戏对弈程序的最终表现，**极大地依赖于其评估函数的质量**。
* **数学表达 (线性组合)**: 通常通过提取游戏状态的各种特征 (features) 并赋予权重 (weights) 来计算：
  $$Eval(s) = w_1f_1(s) + w_2f_2(s) + ... + w_nf_n(s)$$
* **实例分析 (国际象棋 Chess)**:
  * 特征 $f_i$ 可以是棋盘上某类棋子的数量，权重 $w_i$ 是其价值（例如：兵价值 1，马或象价值 3，车价值 5，王后价值 9）。
  * 也可以包含更抽象的特征，比如“王的安全性 (king safety)”或“良好的兵阵结构 (good pawn structure)”，这些特征可能会被赋予相当于“半个兵”的权重。最终将所有特征的加权值组合起来得到总分。

### 6.2.5 视界效应 (Horizon Effect)
* **场景描述**: 考虑这样一种情况，对手走了一步极具威胁的棋，将会造成严重的损失，且这种损失在逻辑上**最终是不可避免的 (ultimately unavoidable)**。
* **引发原因**: 由于 AI 的搜索深度存在限制 (low depth limit)，它如同目光短浅一般，**看不到搜索“视界”之外的事情**，因此它并没有意识到这个灾难最终是躲不掉的。
* **致命后果**: 为了在当前的“视界”内暂时避免或掩盖这个损害，AI 可能会采取**拖延战术 (delaying tactics)**，牺牲其他子力把灾难发生的时间点往后推（推到搜索深度之外）。这往往会导致在拖延的过程中遭受**更加惨痛的损失 (cause even more damage)**。

### 6.2.6 代码简介

以下是该算法的精简版 Python 逻辑和详细讲解。

#### 1. Minimax 伪代码 / 精简版代码

```python
def minimax(state, depth, is_maximizing):
    # 1. 递归终止条件：达到最大深度或游戏结束
    if depth == 0 or is_game_over(state):
        return evaluate(state)  # 返回当前局面的静态评估分

    if is_maximizing:
        # MAX 玩家：尝试所有动作，选得分最高的
        max_eval = -float('inf')
        for child in get_children(state):
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        # MIN 玩家：假设对手绝顶聪明，会选让我方得分最低的
        min_eval = float('inf')
        for child in get_children(state):
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval
```

#### 2. 核心逻辑讲解

* **A. 两个角色**
  * **MAX 玩家（通常是 AI 自己）**：在决策时，会遍历所有可能的动作，并选择那个能带来 **最大值 (Maximum)** 的分支。
  * **MIN 玩家（假设的对手）**：算法假设对手也是完美的决策者。由于是零和博弈，我方的得分就是对手的损失，因此对手会选择能让我方得分 **最小值 (Minimum)** 的分支。

* **B. 递归与回溯**
  * Minimax 是一种深度优先搜索 (DFS)：它会一直向下搜索到指定的 `depth`（深度）或叶子节点。
  * 在叶子节点，使用一个评估函数 (Evaluation Function) 算出当前局面的分数（例如：我方多一个子得 10 分，少一个子扣 10 分）。
  * 分数从下往上回溯，每一层根据当前是 MAX 层还是 MIN 层，分别取 `max()` 或 `min()`。

* **C. 数学表达**
  对于状态 $s$，其 Minimax 价值 $V(s)$ 可以定义为：
  $$V(s) = \begin{cases} \text{evaluate}(s) & \text{if } s \text{ is terminal} \\ \max_{a \in \text{Actions}(s)} V(\text{result}(s, a)) & \text{if player is MAX} \\ \min_{a \in \text{Actions}(s)} V(\text{result}(s, a)) & \text{if player is MIN} \end{cases}$$

#### 3. 与之前概念的联系

* **与 Expectimax 的区别**：
  * Minimax 是极其“稳健且悲观”的。它假设对手永远走最强的动作（取 `min`）。
  * Expectimax 则是“理性的赌徒”。它不取 `min`，而是取期望值（加权平均）。如果对手可能犯错（比如 20% 概率走错路），Expectimax 会把这个概率算进去。

* **性能瓶颈**：
  * Minimax 的搜索空间随着深度指数级增长。在实际应用（如深蓝、AlphaGo 之前版本）中，通常必须配合 Alpha-Beta 剪枝 (Alpha-Beta Pruning) 来剪掉那些明显不需要探索的分支，从而在相同时间内搜得更深。

> **总结**：Minimax 的本质是在一棵充满竞争的决策树中，通过假设对手完美应对，来找到最安全的最优解。
> 
> *思考题：既然提到了爬山法和 Minimax，你觉得这两者在面对“状态空间大小”时，各自的局限性主要体现在哪方面？*


---

## 6.3 博弈树剪枝

### 6.3.1 博弈树剪枝的核心理念 (Game Tree Pruning)
* **核心问题**: 是否有可能在不检查博弈树中每一个节点的情况下，计算出正确的 Minimax 值？
* **解决方案**: 引入**剪枝 (Pruning)** 技术。$\alpha-\beta$ 剪枝算法能够在不遍历所有节点的前提下，准确得出与朴素 Minimax 完全相同的最优解。

### 6.3.2 $\alpha-\beta$ 剪枝算法原理 ($\alpha-\beta$ Pruning Algorithm)
以 **Min 节点版本** 的剪枝逻辑为例：
* 考虑 Min 玩家在某个节点 $n$ 处的估值。
* 当逐步检查 $n$ 的后继子节点时，节点 $n$ 的值只会**不断下降（或保持不变）**，因为 Min 总是力求选择更小的值。
* 假设 $m$ 是 Max 玩家在从根节点到当前节点路径上的任何选择点所能获得的**最佳（最大）保底值**。
* **触发剪枝**: 如果在探索过程中，节点 $n$ 的值变得**比 $m$ 更差（即 $n < m$）**：
  * Max 玩家在之前的决策点上绝不会选择走向节点 $n$ 这个分支（因为 Max 已经有更好的选择 $m$ 了）。
  * 因此，算法可以**立即停止**考虑节点 $n$ 剩余的其他子节点（即完成剪枝）。
* **Max 节点版本**: 其逻辑与上述过程完全对称。

### 6.3.3 $\alpha-\beta$ 剪枝的属性 ($\alpha-\beta$ Pruning Properties)
* **对根节点无影响**: 剪枝**绝对不会影响**根节点的最终 Minimax 值计算。它保证能找到与未剪枝前完全一致的最优移动。
* **中间节点的局限性**: 某些中间节点的值可能是“不准确的”（仅仅记录了边界值而非精确的最优效用）。因此，这种简单版本的 $\alpha-\beta$ 剪枝所计算出的中间节点值，不适合直接用于中间状态的动作选择。

### 6.3.4 移动排序的重要性 (Move Ordering)
* **核心现象**: $\alpha-\beta$ 剪枝的实际效率**极度依赖于**节点/状态被检查的顺序。
* **启发式策略**: 算法应该尽量**优先检查那些最可能是最佳选择的后继节点** (examine first the successors that are likely best)。
* **复杂度优化**: 如果能做到理想的节点排序，$\alpha-\beta$ 剪枝在最坏情况下只需要检查 **$O(b^{m/2})$** 个节点就能选出最佳移动，而朴素 Minimax 需要检查 **$O(b^m)$** 个节点。
  * *实际意义*: 这意味着在消耗相同算力/时间的情况下，采用优秀排序策略的 $\alpha-\beta$ 剪枝能够将 AI 的**前瞻搜索深度直接翻倍**。

