# COMP7404 - Assignment

### A1
**Question:**
Consider a Perceptron with 2 inputs and 1 output. Let the weights of the Perceptron be $w_1 = 1$ and $w_2 = 1$ and let the bias be $w_0 = -1.5$. Calculate the output of the following inputs:(0, 0), (1, 0), (0, 1), (1, 1)

**中文解答:**
感知机的输出由激活函数决定，这里使用阶跃函数（Step function）：$y = \text{step}(w_1 x_1 + w_2 x_2 + w_0)$。当加权总和大于等于0时输出1，否则输出0。
- 对于输入 (0, 0)：$1(0) + 1(0) - 1.5 = -1.5 < 0$，输出为 **0**。
- 对于输入 (1, 0)：$1(1) + 1(0) - 1.5 = -0.5 < 0$，输出为 **0**。
- 对于输入 (0, 1)：$1(0) + 1(1) - 1.5 = -0.5 < 0$，输出为 **0**。
- 对于输入 (1, 1)：$1(1) + 1(1) - 1.5 = 0.5 \geq 0$，输出为 **1**。
（这实际上实现了一个逻辑 AND 运算）

---

### A2
**Question:**
Define a perceptron for the following logical functions: AND, NOT, NAND, NOR

**中文解答:**
为以下逻辑函数定义感知机的权重和偏置：假设输出为 $y = \text{step}(w_1 x_1 + w_2 x_2 + w_0)$ （对于NOT为单输入 $w_1 x_1 + w_0$）。
- **AND（与）**: $w_1 = 1, w_2 = 1, w_0 = -1.5$
  - 只有当 $x_1=1, x_2=1$ 时，$1+1-1.5=0.5 \ge 0$，输出1。其他情况均小于0，输出0。
- **NOT（非）**: $w_1 = -1, w_0 = 0.5$ (单输入 $x_1$)
  - 当 $x_1=0$ 时，$-1(0) + 0.5 = 0.5 \ge 0$，输出1。
  - 当 $x_1=1$ 时，$-1(1) + 0.5 = -0.5 < 0$，输出0。
- **NAND（与非）**: $w_1 = -1, w_2 = -1, w_0 = 1.5$
  - 只有当 $x_1=1, x_2=1$ 时，$-1-1+1.5=-0.5 < 0$，输出0。其他情况均大于等于0，输出1。
- **NOR（或非）**: $w_1 = -1, w_2 = -1, w_0 = 0.5$
  - 当 $x_1=0, x_2=0$ 时，$0+0+0.5=0.5 \ge 0$，输出1。
  - 其他情况（只要有至少一个1），加权和为 $-0.5$ 或 $-1.5$，均小于0，输出0。

---

### A3
**Question:**
The parity problem returns 1 if the number of inputs that are 1 is even, and 0 otherwise. Can a perceptron learn this problem for 3 inputs?

**中文解答:**
**不能**。
单层感知机只能学习**线性可分**的模式。对于3输入的奇偶校验问题（实际上是XOR问题在更高维度的推广，例如输入(0,0,0)输出1（0个1，偶数），(1,0,0)输出0，(1,1,0)输出1等），其正负样本在三维空间中交错分布，无法用一个二维平面（超平面）将输出为1和输出为0的情况完全分离开来。因此，单层感知机无法解决3输入的奇偶校验问题，需要具有隐藏层的多层感知机。

---

### A4
**Question:**
Suppose that the following are a set of point in two classes:
*   Class1: $(1, 1), (1, 2), (2, 1)$
*   Class2: $(0, 0), (1, 0), (0, 1)$

Plot them and find the optimal separating line. What are the support vectors, and what is the meaning?

**中文解答:**
在二维平面上绘制这些点可以看出：
- Class 1 (正类) 的点集中在右上方。
- Class 2 (负类) 的点集中在左下方。
可以观察到这两类点之间的“缝隙”。距离两类点集最近的边界上的点是 $(1,1)$ 和 $(1,0), (0,1)$。
最优分割线（最大间隔超平面）应位于 $(1,1)$ 与线段 $(1,0)-(0,1)$ 的正中间。
Class 1 最靠近边界的点是 $(1,1)$，满足方程 $x_1+x_2 = 2$。
Class 2 最靠近边界的点是 $(1,0)$ 和 $(0,1)$，满足方程 $x_1+x_2 = 1$。
因此，最优分割线位于这两个平行边界正中间，方程为 $x_1 + x_2 = 1.5$（或 $x_1 + x_2 - 1.5 = 0$）。

**支持向量（Support Vectors）**：
支持向量是那些最靠近最优分割线（即位于间隔边界上）的训练样本点。
在这个例子中，支持向量是 **$(1, 1)$（属于Class 1）** 以及 **$(1, 0)$ 和 $(0, 1)$（属于Class 2）**。

**意义**：
支持向量是决定最优分割线位置的唯一元素。如果移动或删除非支持向量的训练点，最优分割线不会改变；但如果移动支持向量，则会改变分割线的位置。它们“支持”了分类边界的构建，构成了支持向量机（SVM）模型的核心。

---

### A5
**Question:**
Suppose that the probability of five events are $P(first) = 0.5, P(second) = P(third) = P(fourth) = P(fifth) = 0.125$. Calculate the entropy and write down in words what this means.

**中文解答:**
信息熵 $H(X)$ 的计算公式为：$H(X) = - \sum_{i} P(x_i) \log_2 P(x_i)$。
代入概率值计算：
$$H = - [ 0.5 \log_2(0.5) + 4 \times 0.125 \log_2(0.125) ]$$
$$H = - [ 0.5 \times (-1) + 4 \times 0.125 \times (-3) ]$$
$$H = - [ -0.5 - 1.5 ] = 2.0$$ 
所以，熵为 **2.0 bits**。

**含义**：
信息熵衡量了该概率分布的不确定性或信息量。熵为2.0意味着，如果我们想对这五个事件发生的结果进行编码以进行通信，平均每次需要 2 个比特（bits）的信息量来表示发生了哪个事件。它也代表了我们对结果平均的不确定程度。

---

### A6
**Question:**
Design a decision tree that computes the logical AND function. How does it compare to the Perceptron solution?

**中文解答:**
计算逻辑 AND 函数的决策树设计如下：
```text
如果 x_1 == 0:
    返回 0
否则 (x_1 == 1):
    如果 x_2 == 0:
        返回 0
    否则 (x_2 == 1):
        返回 1
```
（也可以将 $x_1$ 和 $x_2$ 的判断顺序互换）

**与感知机解决方案的比较**：
- **感知机**：通过寻找一个线性边界（直线）将输入空间一分为二。它是通过权重的加权和与阈值比较来一次性做出决定的（即判断 $w_1 x_1 + w_2 x_2 + w_0 \ge 0$）。在AND问题中，它用一条斜线切分空间。
- **决策树**：通过一系列基于单个特征的正交（轴平行）切分来对空间进行划分。它分阶段做出决定，每次只查看一个特征。在AND问题中，决策树用平行于坐标轴的线段切分出右上角的 $1 \times 1$ 正方形区域。
两者都能完美解决逻辑AND问题，但决策边界的形状（斜线 vs. 轴平行折线）和决策过程（一次性加权和 vs. 分步条件判断）不同。

---

### A7
**Question:**
Turn the following politically incorrect data into a decision tree to classify which attributes make a person attractive, and then extract the rules. Use the Gini Impurity.

| Height  | Hair  | Eyes  | Attractive?  |
|:-:|:-:|:-:|:-:|
| Small  | Blonde  | Brown  | No  |
| Tall  | Dark  | Brown  | No  |
| Tall  | Blonde  | Blue  | Yes  |
| Tall  | Dark  | Blue  | No  |
| Small  | Dark  | Blue  | No  |
| Tall  | Red  | Blue  | Yes  |
| Tall  | Blonde  | Brown  | No  |
| Small  | Blonde  | Blue  | Yes  |

**中文解答:**
数据共8个样本：Yes = 3, No = 5。
初始基尼不纯度：$G_{root} = 1 - (3/8)^2 - (5/8)^2 = 30/64 \approx 0.46875$

**1. 计算各特征作为根节点的加权基尼不纯度：**
- **按 Height 划分**：
  - Small (3个): 1 Yes, 2 No. $G_{Small} = 1 - (1/3)^2 - (2/3)^2 = 4/9 \approx 0.444$
  - Tall (5个): 2 Yes, 3 No. $G_{Tall} = 1 - (2/5)^2 - (3/5)^2 = 12/25 = 0.48$
  - 加权 Gini = $(3/8) \times (4/9) + (5/8) \times (12/25) = 1/6 + 3/10 = 14/30 \approx 0.4667$
- **按 Hair 划分**：
  - Blonde (4个): 2 Yes, 2 No. $G_{Blonde} = 1 - (1/2)^2 - (1/2)^2 = 0.5$
  - Dark (3个): 0 Yes, 3 No. $G_{Dark} = 0$
  - Red (1个): 1 Yes, 0 No. $G_{Red} = 0$
  - 加权 Gini = $(4/8) \times 0.5 + (3/8) \times 0 + (1/8) \times 0 = 0.25$
- **按 Eyes 划分**：
  - Brown (3个): 0 Yes, 3 No. $G_{Brown} = 0$
  - Blue (5个): 3 Yes, 2 No. $G_{Blue} = 1 - (3/5)^2 - (2/5)^2 = 0.48$
  - 加权 Gini = $(3/8) \times 0 + (5/8) \times 0.48 = 0.3$

显然，**按 Hair 划分** 的基尼不纯度最低 (0.25)，因此选择 Hair 作为根节点。

**2. 继续分支：**
- 如果 **Hair == Dark**，分类全为 No（纯节点）。
- 如果 **Hair == Red**，分类全为 Yes（纯节点）。
- 如果 **Hair == Blonde**，共有4个样本（2 Yes, 2 No）：
  - (Small, Blonde, Brown, No)
  - (Tall, Blonde, Blue, Yes)
  - (Tall, Blonde, Brown, No)
  - (Small, Blonde, Blue, Yes)
  在这个分支中，继续按Eyes划分：
  - Brown (2个): 0 Yes, 2 No. $G = 0$ (纯节点)
  - Blue (2个): 2 Yes, 0 No. $G = 0$ (纯节点)
  可见，在Blonde分支下选择 **Eyes** 进行划分即可得到完美的纯节点。（如果选Height，基尼不纯度仍为0.5，无法区分）。

**构建的决策树结构**：
```text
Hair?
 ├── Dark: 返回 No
 ├── Red: 返回 Yes
 └── Blonde: 继续判断 Eyes?
      ├── Brown: 返回 No
      └── Blue: 返回 Yes
```

**提取的规则 (Rules)**：
- Rule 1: IF Hair = Dark THEN Attractive = No
- Rule 2: IF Hair = Red THEN Attractive = Yes
- Rule 3: IF Hair = Blonde AND Eyes = Brown THEN Attractive = No
- Rule 4: IF Hair = Blonde AND Eyes = Blue THEN Attractive = Yes

---

### A8
**Question:**
Suppose we collect data for a group of students in a postgraduate machine learning class with features $x_1$ = hours studies, $x_2$ = undergraduate GPA and label $y$ = receive an A. We fit a logistic regression and produce estimated weights as follows: $w_0 = -6$, $w_1 = 0.05$, $w_2 = 1$.

1.  Estimate the probability that a student who studies for 40h and has an undergraduate GPA of 3.5 gets an A in the class
2.  How many hours would the student in part 1. need to study to have a 50% chance of getting an A in the class?

**中文解答:**
逻辑回归模型的线性部分为：$z = w_0 + w_1 x_1 + w_2 x_2 = -6 + 0.05 x_1 + x_2$
概率预测公式为：$P(y=1) = \frac{1}{1 + e^{-z}}$

**1.** 估计学习40小时且GPA为3.5的学生获得A的概率：
代入 $x_1 = 40$, $x_2 = 3.5$：
$z = -6 + 0.05(40) + 3.5 = -6 + 2.0 + 3.5 = -0.5$
概率 $P = \frac{1}{1 + e^{-(-0.5)}} = \frac{1}{1 + e^{0.5}} \approx \frac{1}{1 + 1.6487} \approx 0.3775$
该学生获得A的概率约为 **37.75%**。

**2.** 计算该学生需要学习多少小时才能有50%的机会获得A：
获得 50% 机会意味着 $P(y=1) = 0.5$。
对于逻辑回归，当 $P = 0.5$ 时，对应的对数几率 $z = 0$。
即：$-6 + 0.05 x_1 + x_2 = 0$
代入该学生的GPA $x_2 = 3.5$：
$-6 + 0.05 x_1 + 3.5 = 0$
$-2.5 + 0.05 x_1 = 0$
$0.05 x_1 = 2.5$
$x_1 = \frac{2.5}{0.05} = 50$
该学生需要学习 **50小时** 才能有 50% 的机会获得 A。

---

### A9
**Question:**
Suppose that we take a data set, divide it into equally-sized training and test sets, and then try out two different classification procedures. First we use logistic regression and get an error rate of 20% on the training data and 30% on the test data. Next we use 1-nearest neighbors (i.e., K=1) and get an average error rate (averaged over both test and training data sets) of 18%. Based on these results, which method should we prefer to use for classification of new observations? Why?

**中文解答:**
我们应该更倾向于使用 **逻辑回归（Logistic Regression）**。

**原因**：
对于 1-最近邻（1-NN）算法，它在训练集上的错误率总是 **0%**（因为每个训练样本自己就是它最近的邻居，预测一定正确）。
题目给出 1-NN 的平均错误率（训练集和测试集的均值）为 18%。由于训练集和测试集大小相等，平均错误率计算为：
$$ \frac{\text{Training Error} + \text{Test Error}}{2} = 18\% $$
代入训练集错误率 0%：
$$ \frac{0\% + \text{Test Error}}{2} = 18\% $$
解得 1-NN 在**测试集上的错误率为 36%**。

评估模型对新数据（未知数据）分类能力的核心指标是**测试集错误率**：
- 逻辑回归的测试集错误率为 **30%**。
- 1-最近邻的测试集错误率为 **36%**。

由于逻辑回归在未见过的数据（测试集）上表现更好，错误率更低（30% < 36%），这表明它具有更好的泛化能力。而 1-NN 出现了严重的过拟合现象。因此，为了对新观察值进行分类，我们应优先选择逻辑回归。

---

### A10
**Question:**
Suppose the features in your training set have very different scales. Which algorithms discussed in class might suffer from this, and how? What can you do about it?

**中文解答:**
**受影响的算法及原因**：
1. **K-最近邻 (KNN)**：依赖于距离度量（如欧氏距离）。尺度大的特征会在距离计算中占据绝对主导地位，使得算法几乎忽略小尺度的特征，导致分类效果变差。
2. **支持向量机 (SVM)**：基于距离寻找最大化间隔边界。未缩放的特征会导致间隔计算扭曲，从而严重影响最优超平面的确定。
3. **基于梯度下降优化的算法（如感知机、逻辑回归、神经网络等）**：当特征尺度差异极大时，损失函数的等高线会变得像极度拉长的椭圆。在梯度下降过程中，这会导致算法在某些方向上更新缓慢，而在另一些方向上剧烈震荡，极大降低收敛速度，甚至难以找到最优解。L1/L2正则化也会对大尺度和小尺度特征产生不公平的惩罚。

*(注：基于决策树的算法如随机森林、AdaBoost 则不受影响，因为它们只关注单一特征的排序和切分，不涉及跨特征的距离计算。)*

**解决方法**：
可以通过**特征缩放（Feature Scaling）**来解决。常见的方法有：
- **标准化 (Standardization)**：将特征转换为均值为0，标准差为1的分布（$x' = \frac{x - \mu}{\sigma}$）。大多数机器学习算法首选这种缩放。
- **最小-最大归一化 (Min-Max Normalization)**：将特征值线性映射到特定范围（通常是 $[0, 1]$）内（$x' = \frac{x - \min}{\max - \min}$）。

---

### A11
**Question:**
If your AdaBoost ensemble underfits the training data, which hyperparameters should you tweak and how?

**中文解答:**
AdaBoost 欠拟合意味着模型过于简单，没有捕捉到数据中的复杂模式。为了增加模型的拟合能力和复杂度，可以调整以下超参数：
1. **增加估计器的数量（`n_estimators`）**：这是最直观的方法。增加弱学习器（基分类器）的数量允许模型在后续迭代中不断纠正前序模型的错误，从而提升整体表达能力。
2. **增加弱学习器的复杂度**：默认情况下，AdaBoost 常使用深度仅为1的决策树（Decision Stump）。可以通过增加单棵树的**最大深度（`max_depth`）**或减少内部节点再划分所需的最小样本数（`min_samples_split`）来让基础估计器变得更强。
3. **增加学习率（`learning_rate`）**：学习率决定了每个弱学习器对最终集成的贡献权重。稍微提高学习率可以使每个弱分类器的权重更新步长更大，从而更快地拟合训练数据。（注：增加学习率时通常需要注意不要过大，并常与 `n_estimators` 一起权衡）。

---

### A12
**Question:**
What is the benefit of out-of-bag evaluation?

**中文解答:**
在使用装袋法（Bagging）或随机森林构建集成模型时，由于使用了有放回的随机重采样（Bootstrap sampling）构建每个基分类器的训练集，大约有 $36.8\%$ 的原始训练实例不会被特定的基分类器采样到。这些未被采样的实例被称为该分类器的“包外”（out-of-bag, OOB）实例。

**包外评估的好处**：
1. **无需划分独立的验证集，最大化利用数据**：OOB 实例可以自动作为验证集，用于评估模型的泛化性能。由于模型在训练时没有“见过”这些 OOB 实例，因此评估结果是无偏的，我们无需牺牲宝贵的训练数据去刻意切分出一个验证集。
2. **计算效率高，实时评估**：可以在模型集成的过程中同时进行验证和性能评估，这比进行 K-折交叉验证（K-Fold Cross Validation）计算成本更低、速度更快，因为它避免了反复切分数据和重新训练模型的开销。

---

### A13
**Question:**
What is the difference between hard and soft voting classifiers?

**中文解答:**
硬投票和软投票是集成学习中组合多个基础分类器预测结果的两种不同机制：

- **硬投票（Hard Voting / Majority Voting）**：每个基础分类器独立地对样本进行预测，输出一个明确的类别标签。硬投票分类器简单地统计每个类别的得票数，将**得票数最多（多数票）**的类别作为最终集成的预测结果。它只关注最终的“决定”。
- **软投票（Soft Voting）**：要求所有的基础分类器都能估算并输出各个类别的概率（例如具有 `predict_proba()` 方法）。软投票分类器会将所有模型对每个类别预测的**概率值进行平均（或加权平均）**，然后选择平均概率最高的类别作为最终结果。

**主要区别与优势**：
软投票相比硬投票能给予高度自信的预测更大的权重。例如，如果一个模型以 90% 的概率预测类别A，而另两个模型以 51% 的概率预测类别B，软投票会倾向于类别A，而硬投票会选择类别B。在多数情况下，**软投票的表现通常优于硬投票**，因为它考虑了模型预测的不确定性，包含了更多细致的概率置信度信息。
