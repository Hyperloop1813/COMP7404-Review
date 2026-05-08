# Perceptron & Adaline
最短的一集

# 1 Perceptron
## 1.1 人工神经元定义 (Artificial Neuron - Definition)

### 1.1 基本概念
* **任务场景**：二分类任务，我们将两个类别分别记为 $1$（正类）和 $-1$（负类）。
* **净输入 (Net Input)**：输入特征 $\mathbf{x}$ 与对应权重向量 $\mathbf{w}$ 的线性组合 $z$：
    $$z = w_1x_1 + \dots + w_mx_m$$
    其向量形式表示为：
    $$\mathbf{w} = \begin{bmatrix} w_1 \\ \vdots \\ w_m \end{bmatrix}, \mathbf{x} = \begin{bmatrix} x_1 \\ \vdots \\ x_m \end{bmatrix}$$

### 1.2 决策函数与偏置单元的引入
* **基础决策函数**：基于阈值 $\theta$ 进行判断：
    $$\phi(z) = \begin{cases} 1 & \text{if } z \ge \theta \\ -1 & \text{otherwise} \end{cases}$$
* **化简与偏置 (Bias Unit)**：为了简化公式，通常将阈值 $\theta$ 移至等号左侧，并定义**偏置单元** $w_0 = -\theta$ 以及常量输入 $x_0 = 1$。
    * **更新后的净输入**：
        $$z = w_0x_0 + w_1x_1 + \dots + w_mx_m = \mathbf{w}^T\mathbf{x}$$
    * **更新后的决策函数**：
        $$\phi(z) = \begin{cases} 1 & \text{if } z \ge 0 \\ -1 & \text{otherwise} \end{cases}$$

## 1.2 感知机学习规则 (Perceptron Learning Rule)

Rosenblatt 感知机规则的核心在于通过样本不断调整权重，具体步骤如下：
1.  **初始化**：初始化所有权重。
2.  **迭代**：对于每一个训练样本 $\mathbf{x}^{(i)}$，执行以下操作：
    * 计算预测的输出值 $\hat{y}^{(i)}$（即通过单位阶跃函数预测的类别标签）。
    * 更新权重。

### 1.2.1 权重更新公式
对于每一个权重 $w_j$，其更新规则为：
$$w_j := w_j + \Delta w_j$$
其中，权重更新量 $\Delta w_j$ 的计算公式为：
$$\Delta w_j = \eta \left( y^{(i)} - \hat{y}^{(i)} \right) x_j^{(i)}$$
* $\eta$：学习率 (Learning rate)
* $y^{(i)}$：第 $i$ 个样本的真实类别标签
* $\hat{y}^{(i)}$：第 $i$ 个样本的预测类别标签

### 1.2.2 同步更新原则
* **所有权重必须同步更新**。这意味着在计算出一个样本引发的所有权重的 $\Delta w_j$ 之前，不能提前用部分已更新的权重去重新计算预测值 $\hat{y}^{(i)}$。
* **二维数据集示例**（假设输入特征为 $x_1, x_2$，偏置项输入 $x_0=1$）：
    $$\Delta w_0 = \eta \left( y^{(i)} - output^{(i)} \right)$$
    $$\Delta w_1 = \eta \left( y^{(i)} - output^{(i)} \right) x_1^{(i)}$$
    $$\Delta w_2 = \eta \left( y^{(i)} - output^{(i)} \right) x_2^{(i)}$$
    *(注：此处的 $output^{(i)}$ 与前文的 $\hat{y}^{(i)}$ 含义相同)*

### 1.2.3 预测结果对权重的不同影响
根据模型预测是否准确，权重更新有以下两种情景：

* **情景 A：预测正确 (权重保持不变)**
    * 真实为 $-1$，预测为 $-1$：$\Delta w_j = \eta (-1 - (-1)) x_j^{(i)} = 0$
    * 真实为 $1$，预测为 $1$：$\Delta w_j = \eta (1 - 1) x_j^{(i)} = 0$
* **情景 B：预测错误 (权重向目标类别方向被“推移”)**
    * 真实为 $1$，预测为 $-1$：$\Delta w_j = \eta (1 - (-1)) x_j^{(i)} = \eta (2) x_j^{(i)}$
    * 真实为 $-1$，预测为 $1$：$\Delta w_j = \eta (-1 - 1) x_j^{(i)} = \eta (-2) x_j^{(i)}$

### 1.2.4 比例关系
* 从公式中可以明显看出，单个权重的更新步长 $\Delta w_j$ 与其对应的输入特征值 $x_j^{(i)}$ **成正比**：
    $$\Delta w_j = \eta \left( y^{(i)} - \hat{y}^{(i)} \right) x_j^{(i)}$$

## 1.3 线性可分性与感知机的局限 (Linearly Separable)

### 感知机的收敛条件
* 感知机算法只有在满足以下两个条件时，才被证明能够保证收敛：
  1. 两个类别是**线性可分**的（Linearly separable）。
  2. 学习率（Learning rate）足够小。

### 处理非线性可分数据
* 如果两个类别无法被线性决策边界分开，感知机将会无限循环地更新权重，永远无法停止。
* **解决策略**：
  * 设置最大遍历训练数据集的次数（即 **Epochs** 的上限）。
  * 设置一个可容忍的错误分类数量的**阈值**（Threshold for tolerated misclassifications）。

---

# 2 自适应线性神经元 (Adaptive Linear Neuron - Adaline)

## 2.1 基本概念
* **Adaline** (ADAptive LInear NEuron) 是对经典感知机算法的改进，由 Bernard Widrow 和 Ted Hoff 于 1960 年发表。
* **核心区别**：在 Adaline 中，权重的更新是基于**线性激活函数**（Linear activation function）进行的，而不是像感知机那样基于阶跃函数。
    $$\phi(\mathbf{w}^T\mathbf{x}) = \mathbf{w}^T\mathbf{x}$$
* **预测机制**：虽然在学习（更新权重）阶段使用的是线性激活函数，但在最终进行类别预测时，仍然会使用一个阈值函数（Threshold function）来输出离散的类标。

## 2.2 目标函数 (Objective Function)

### 监督学习与代价函数
* 监督学习算法的一个核心要素是需要优化的**目标函数**，通常是我们希望最小化的**代价函数**（Cost function）。

### 误差平方和 (SSE)
* 在 Adaline 中，代价函数 $J$ 被定义为计算出的连续值与真实类标之间的**误差平方和**（Sum of Squared Errors, SSE）：
    $$J(\mathbf{w}) = \frac{1}{2} \sum_i \left( y^{(i)} - \phi(z^{(i)}) \right)^2$$
* **数学性质**：可以证明代价函数 $J$ 是**可微的**（Differentiable）且是**凸函数**（Convex）。这使得使用**梯度下降法**（Gradient Descent）来寻找全局最小值变得非常容易。

## 2.3 权重更新与梯度下降 (Weight Update)

### 梯度下降原理
* 通过向代价函数 $J(\mathbf{w})$ 梯度 $\nabla J(\mathbf{w})$ 的**相反方向**迈出一步来更新权重：
    $$\mathbf{w} := \mathbf{w} + \Delta\mathbf{w}$$
* 权重变化量 $\Delta\mathbf{w}$ 定义为负梯度乘以学习率 $\eta$：
    $$\Delta\mathbf{w} = -\eta \nabla J(\mathbf{w})$$

### 梯度的数学推导
* 为了计算代价函数的梯度，我们需要求代价函数对每个权重 $w_j$ 的偏导数：
    $$\frac{\partial J}{\partial w_j} = \frac{\partial}{\partial w_j} \frac{1}{2} \sum_i \left( y^{(i)} - \phi(z^{(i)}) \right)^2$$
* 利用链式法则展开推导后，最终得到偏导数为：
    $$\frac{\partial J}{\partial w_j} = -\sum_i \left( y^{(i)} - \phi(z^{(i)}) \right) x_j^{(i)}$$

### 最终的权重更新公式
* 结合上述偏导数，单个权重 $w_j$ 的更新量可以写为：
    $$\Delta w_j = -\eta \frac{\partial J}{\partial w_j} = \eta \sum_i \left( y^{(i)} - \phi(z^{(i)}) \right) x_j^{(i)}$$

### 批量梯度下降 (Batch Gradient Descent)
* **注意**：上述公式中的求和符号 $\sum_i$ 表明，权重的更新是基于训练集中**所有样本**的误差累加计算出来的。
* 这种在遍历完整个训练集后才进行一次权重更新的方法被称为**批量梯度下降**（与每次处理一个样本就更新一次的增量更新/随机梯度下降不同）。

---

# 3 机器学习的常用技巧

## 3.1 特征缩放 (Feature Scaling)

### 为什么需要特征缩放？
* 许多机器学习算法需要对特征进行缩放以获得最佳性能。
* **例如**：如果数据服从标准分布，**梯度下降 (Gradient Descent)** 的收敛速度会大大加快。

### 标准化 (Standardization)
标准化是特征缩放的一种常用方法，其目标是将特征缩放至：
* 均值 (mean) 为 $0$
* 标准差 (standard deviation) 为 $1$

### 标准化公式
对于数据集中的第 $j$ 个特征，我们可以用该特征的值减去其样本均值 $\mu_j$，再除以其标准差 $\sigma_j$：
$$x_j' = \frac{x_j - \mu_j}{\sigma_j}$$
* $x_j$：包含所有训练样本中第 $j$ 个特征值的向量。
* $\mu_j$：第 $j$ 个特征的样本均值。
* $\sigma_j$：第 $j$ 个特征的标准差。
* **注意**：这种标准化技术需要独立应用到数据集中的每一个特征 $j$ 上。

## 3.2 随机梯度下降 (Stochastic Gradient Descent, SGD)

### 3.2.1 批量梯度下降的局限性
* 在面对拥有数百万数据点的超大型数据集时（这在 ML 应用中很常见），**批量梯度下降 (Batch Gradient Descent)** 的计算成本极高。
* 因为每次仅仅是为了向前迈出一步（更新一次权重），就需要重新评估整个训练数据集。

### 3.2.2 SGD 的核心思想
* SGD 是批量梯度下降的流行替代方案。
* 与批量梯度下降基于所有样本的累积误差总和 $\Delta\mathbf{w} = \eta \sum_i \left( y^{(i)} - \phi(z^{(i)}) \right)\mathbf{x}^{(i)}$ 来更新权重不同，**SGD 为每一个单独的训练样本进行增量式的权重更新**。

### 3.2.3 SGD 的优势
1. **收敛速度更快**：因为权重更新的频率远高于批量梯度下降。
2. **更容易逃离局部最优解**：在处理非线性代价函数时，由于每次更新具有一定的随机性，SGD 更容易跳出浅层的局部极小值 (shallow local minima)。
3. **支持在线学习 (Online Learning)**：模型可以在新训练数据到达时“即时”进行训练。

### 3.2.4 SGD 的最佳实践
* 必须以**随机的顺序**提供训练数据。
* 在每一个 Epoch（遍历完一次训练集）开始前，**打乱 (shuffle)** 训练集，以防止模型陷入循环更新。

### 3.2.5 小批量学习 (Mini-Batch Learning)

#### 核心概念
* 小批量学习是批量梯度下降 (Batch GD) 和随机梯度下降 (SGD) 之间的一种**折中方案 (compromise)**。
* 它的做法是将批量梯度下降应用于训练数据的**较小子集**上（例如：每次处理 32 个样本）。

#### 小批量学习的优势
1. **对比批量梯度下降**：由于权重更新更加频繁，通过小批量学习可以更快地达到收敛。
2. **对比随机梯度下降**：小批量学习允许我们将 SGD 中逐个样本遍历的 `for` 循环替换为**向量化操作 (vectorized operations)**，从而大幅提升计算效率（特别是在使用 GPU 时）。

---

# 隋唐小测试

### **Q1: 特征缩放的影响**
**英文题目**: Suppose the features in your training set have very different scales. What can you do about it?
**中文题目**: 假设你的训练集中的特征具有非常不同的尺度（缩放比例）。你能对此做些什么？

* **English Answer**: 
    You should apply **Feature Scaling** to the data. Common methods include **Standardization** (subtracting the mean and dividing by the standard deviation, bringing the mean to 0 and variance to 1) or **Normalization/Min-Max scaling** (scaling values to a [0,1] range). Feature scaling ensures that Gradient Descent converges much faster and prevents features with larger scales from dominating the weight updates.
* **中文解答**: 
    你应该对数据进行**特征缩放 (Feature Scaling)**。常用的方法包括**标准化 (Standardization)**（将数据减去均值并除以标准差，使其均值为0，方差为1）或**归一化 (Normalization)**（将数据缩放到 [0,1] 区间）。特征缩放可以确保梯度下降算法更快地收敛，并防止尺度较大的特征在权重更新中占据主导地位。

---

### **Q2: 逻辑回归与局部最优**
**英文题目**: Can Gradient Descent get stuck in a local minimum when training a Logistic Regression model?
**中文题目**: 在训练逻辑回归模型时，梯度下降会陷入局部最小值吗？

* **English Answer**: 
    **No.** The cost function used for a Logistic Regression model (Log-Loss / Cross-Entropy) is a strictly **convex function**. A convex function has a bowl-like shape with no local minima, only one single global minimum. Therefore, Gradient Descent is guaranteed to find the global minimum (provided the learning rate is appropriate and it runs for enough iterations).
* **中文解答**: 
    **不会。** 逻辑回归模型所使用的代价函数（对数损失 / 交叉熵）是一个严格的**凸函数 (Convex function)**。凸函数具有类似碗的形状，没有局部最小值，只存在唯一的一个全局最小值。因此，只要学习率设置合适并且迭代次数足够，梯度下降算法一定能找到全局最小值。

---

### **Q3: 算法最终模型的差异性**
**英文题目**: Do all Gradient Descent algorithms lead to the same model, provided you let them run long enough?
**中文题目**: 只要运行时间足够长，所有的梯度下降算法都会得到相同的模型吗？

* **English Answer**: 
    **Not necessarily.** If the optimization problem is strictly convex and the learning rate is fixed and appropriate, Batch Gradient Descent will converge to the exact global minimum. However, **Stochastic Gradient Descent (SGD)** and **Mini-batch Gradient Descent** will bounce around the minimum due to their inherent randomness. They will end up hovering very close to the minimum but may never completely settle on the exact same mathematical point unless the learning rate is gradually reduced (using a learning schedule). Furthermore, for non-convex problems (like deep neural networks), different GD algorithms or even the same algorithm with different random initialization might converge to completely different local minima.
* **中文解答**: 
    **不一定。** 如果优化问题是严格凸的，且学习率合适，批量梯度下降 (Batch GD) 会收敛到精确的全局最小值。然而，**随机梯度下降 (SGD)** 和 **小批量梯度下降 (Mini-batch GD)** 由于具有内在的随机性，会在最小值附近不断震荡。除非随着时间推移逐渐降低学习率（学习率衰减），否则它们只会在最小值附近徘徊，而无法精确停在同一点。此外，对于非凸问题（如深度神经网络），不同的算法或不同的初始随机权重，可能会导致模型收敛到完全不同的局部最小值。

---

### **Q4: 验证误差持续上升**
**英文题目**: Suppose you use Batch Gradient Descent and you plot the validation error at every epoch. If you notice that the validation error consistently goes up, what is likely going on? How can you fix this?
**中文题目**: 假设你使用批量梯度下降，并在每个 epoch 绘制验证误差。如果你发现验证误差持续上升，这可能是什么情况？你该如何解决？

* **English Answer**: 
    There are two main possibilities:
    1.  **Divergence (Learning rate too high):** If the *training error* is **also** consistently going up, it means the algorithm is diverging because the learning rate ($\eta$) is too high. **Fix:** Reduce the learning rate.
    2.  **Overfitting:** If the *training error* is going **down** while the validation error goes up, your model is overfitting the training data and losing its generalization ability. **Fix:** Apply Early Stopping (stop training), add regularization (L1/L2), or gather more training data.
* **中文解答**: 
    主要有两种可能性：
    1.  **算法发散 (学习率过高)**：如果**训练误差也在**持续上升，说明算法正在发散，因为跳跃步长太大（学习率 $\eta$ 太高）。**解决方法**：降低学习率。
    2.  **过拟合 (Overfitting)**：如果**训练误差在下降**，而验证误差在上升，说明你的模型正在死记硬背训练数据，失去了泛化能力。**解决方法**：采用早停法 (Early Stopping) 停止训练、添加正则化项 (L1/L2)，或者获取更多的训练数据。

---

### **Q5: 小批量梯度下降的早停策略**
**英文题目**: Is it a good idea to stop Mini-batch Gradient Descent immediately when the validation error goes up?
**中文题目**: 当验证误差上升时，立即停止小批量梯度下降是个好主意吗？

* **English Answer**: 
    **No.** Because Mini-batch Gradient Descent updates weights based on a random subset of data at each step, its learning curve is naturally noisy and erratic. The validation error will fluctuate and may temporarily go up even if the overall trend is still going down. Instead of stopping immediately, you should save the model at regular intervals and only stop training if the validation error has been consistently going up for a specified number of epochs (this parameter is often called "patience").
* **中文解答**: 
    **不是个好主意。** 因为小批量梯度下降在每步更新时只基于数据的一个随机子集，这导致其学习曲线天生带有噪声和波动。验证误差产生上下波动是正常的，即使整体趋势仍在下降，它也可能出现暂时的上升。正确的做法是定期保存模型的最佳状态，并且只有在观察到验证误差已经连续上升了多个 epoch（这个等待的阈值通常被称为“耐心值/Patience”）之后，才决定停止训练。