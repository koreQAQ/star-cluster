# About Dataset
## Context
Stars mostly form in clusters and associations rather than in isolation. Milky Way star clusters are easily observable with small telescopes, and in some cases even with the naked eye. Depending on a variety of conditions, star clusters may dissolve quickly or be very long lived.
The dynamical evolution of star clusters is a topic of very active research in astrophysics. Some popular models of star clusters are the so-called direct N-body simulations [1, 2], where every star is represented by a point particle that interacts gravitationally with every other particle. This kind of simulation is computationally expensive, as it scales as O(N^2) where N is the number of particles in the simulated cluster. In the following, the words "particle" and "star" are used interchangeably.

恒星大多以星团和联合体的形式形成，而不是孤立的。 银河系星团很容易用小型望远镜观测到，在某些情况下甚至用肉眼即可观测到。 根据各种条件，星团可能会迅速溶解或寿命很长。
星团的动力学演化是天体物理学中非常活跃的研究课题。 一些流行的星团模型是所谓的直接 N 体模拟，其中每颗恒星都由一个点粒子表示，该点粒子与其他所有粒子相互作用。 
这种模拟的计算成本很高，因为它的规模为 O(N^2)，其中 N 是模拟簇中的粒子数。 在下文中，术语“粒子”和“星形”可互换使用。

## Content
This dataset contains the positions and velocities of simulated stars (particles) in a direct N-body simulation of a star cluster. In the cluster there are initially 64000 stars distributed in position-velocity space according to a King model [3]. Each .csv file named c_xxxx.csv corresponds to a snapshot of the simulation at time t = xxxx. For example, c_0000.csv contains the initial conditions (positions and velocities of stars at time t=0). Times are measured in standard N-body units [4]. This is a system of units where G = M = −4E = 1 (G is the gravitational constant, M the total mass of the cluster, and E its total energy).
该数据集包含星团直接 N 体模拟中模拟恒星（粒子）的位置和速度。 根据 King 模型 [3]，星团中最初有 64000 颗恒星分布在位置速度空间中。 每个名为 c_xxxx.csv 的 .csv 文件对应于时间 t = xxxx 时的模拟快照。 例如，c_0000.csv 包含初始条件（时间 t=0 时恒星的位置和速度）。 时间以标准 N 体单位测量[4]。 这是一个单位制，其中 G = M = −4E = 1（G 是引力常数，M 是星团的总质量，E 是总能量）。

### x, y, z
Columns 1, 2, and 3 of each file are the x, y, z positions of the stars. They are also expressed in standard N-body units [4]. You can switch to units of the median radius of the cluster by finding the cluster center and calculating the median distance of stars from it, and then dividing x, y, and z by this number. In general, the median radius changes in time. The initial conditions are approximately spherically symmetric (you can check) so there is no particular physical meaning attached to the choice of x, y, and z.
每个文件的第 1、2 和 3 列是星星的 x、y、z 位置。 它们也以标准 N 体单位表示[4]。 您可以通过查找星团中心并计算恒星与其之间的中值距离，然后将 x、y 和 z 除以该数字来切换为星团中值半径的单位。 一般来说，中值半径随时间变化。 初始条件近似球对称（您可以检查），因此 x、y 和 z 的选择没有特定的物理意义。

### vx, vy, vz
Columns 4, 5, and 6 contain the x, y, and z velocity, also in N-body units. A scale velocity for the stars can be obtained by taking the standard deviation of velocity along one direction (e.g. z). You may check that the ratio between the typical radius (see above) and the typical velocity is of order unity.
第 4、5 和 6 列包含 x、y 和 z 速度，也采用 N 体单位。 恒星的标度速度可以通过沿一个方向（例如 z）取速度的标准差来获得。 您可以检查典型半径（见上文）和典型速度之间的比率是否具有单位量级。

### m
Column 7 is the mass of each star. For this simulation this is identically 1.5625e-05, i.e. 1/64000. The total mass of the cluster is initially 1. More realistic simulations (coming soon) have a spectrum of different masses and live stelar evolution, that results in changes in the mass of stars. This simulation is a pure N-body problem instead.
第 7 列是每颗恒星的质量。 对于此模拟，这与 1.5625e-05 相同，即 1/64000。 星团的总质量最初为 1。更真实的模拟（即将推出）具有不同质量的光谱和实时恒星演化，这会导致恒星质量的变化。 该模拟是一个纯 N 体问题。

### Star id number
The id numbers of each particle are listed in the last column (8) of the files under the header "id". The ids are unique and can be used to trace the position and velocity of a star across all files. There are initially 64000 particles. At end of the simulation there are 63970. This is because some particles escape the cluster.

## Acknowledgements
This simulation was run on a Center for Galaxy Evolution Research (CGER) workstation at Yonsei University (Seoul, Korea), using the NBODY6 software (https://www.ast.cam.ac.uk/~sverre/web/pages/nbody.htm).

## Inspiration
Some stars hover around the center of the cluster, while some other get kicked out to the cluster outskirts or even leave the cluster altogether. Can we predict where a star will be at any given time based on its initial position and velocity? Can we predict its velocity?

How correlated are the motions of stars? Can we predict the velocity of a given star based on the velocity of its neighbours?

The size of the cluster can be measured by defining a center (see below) and finding the median distance of stars from it. This is called the three-dimensional effective radius. Can we predict how it evolves over time? What are its properties as a time series? What can we say about other quantiles of the radius?

How to define the cluster center? Just as the mode of a KDE of the distribution of stars? How does it move over time and how to quantify the properties of its fluctuations? Is the cluster symmetric around this center?

Some stars leave the cluster: over time they exchange energy in close encounters with other stars and reach the escape velocity. This can be seen by comparing later snapshots with the initial one: some IDs are missing and there is overall a lower number of stars. Can we predict which stars are more likely to escape? When will a given star escape?

有些恒星在星团中心周围盘旋，而另一些则被踢到星团外围，甚至完全离开星团。 我们能否根据恒星的初始位置和速度来预测恒星在任何给定时间的位置？ 我们可以预测它的速度吗？

恒星运动的相关性如何？ 我们可以根据邻近恒星的速度来预测给定恒星的速度吗？

星团的大小可以通过定义一个中心（见下文）并找到恒星与其中心的中值距离来测量。 
这称为三维有效半径。 我们可以预测它如何随时间演变吗？ 作为时间序列，它有什么属性？ 关于半径的其他分位数我们能说什么？

如何定义聚类中心？ 就像KDE的模式一样分配星星吗？ 它如何随时间变化以及如何量化其波动的特性？ 该簇围绕该中心对称吗？

一些恒星离开星团：随着时间的推移，它们在与其他恒星的近距离接触中交换能量并达到逃逸速度。 通过将后来的快照与最初的快照进行比较可以看出这一点：缺少一些 ID，并且总体上星星数量较少。 我们能否预测哪些恒星更有可能逃脱？ 某颗恒星什么时候会逃脱？