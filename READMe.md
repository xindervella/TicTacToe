Tic Tac Toe
=============

>使用类似西洋跳棋的问题的算法，实现一个更简单的 tic-tac-toe 游戏。

>把学习到的函数 Vestimate 表示为自选的棋局参数的线性组合。

>在训练这个程序时，让它和它的另一个拷贝反复比赛，后者使用一个手工建立的固定评估函数。

>绘制出你的程序的获胜率随训练次数的变化情况。


先把 Vestimate 表示一下：

*   x1 : 有一个 X

*   x2 : 有一个 O

*   x3 : 有两个 X 和一个空格

*   x4 : 有两个 O 和一个空格

*   x5 : 有三个 X

*   x4 : 有三个 O

这样得到了目标函数：

      Vest( b ) = w0 + w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6

* * *

初始时把w0,w1, ..., w6全部设为 0.5 然后开始和另一个随机落子的对手比赛，每次结束后通过训练样例修改权重，然后再继续，使用的训练法则和所谓西洋跳棋差不多。

*   如果获胜 Vtrain( b ) = 100

*   如果失败 Vtrain( b ) = -100

*   如果平局 Vtrain( b ) = 0

*   中间过程 Vtrain( b ) = Vest( successor( b ) )

successor( b ) 表示程序走了一步，对手回应一步之后的棋局

然后用LMS更新法则更新 wi

      wi = wi + n * ( Vtrain( b ) - Vest( b ) * xi        n是用来调整 wi 更新幅度的一个小常数。

* * *

Experiment Generator 以当前学到的函数作为输入，输出一个新的问题, 在这里偷懒每次都提供一个空棋局来玩。

Performance  System 以新问题的实例作为输入，输出一组解答， 在这里我把对弈历史作为输出，采用下一步走法的策略是由学到的函数 Vest 来决定的。

Critic 以对弈历史作为输入，输出目标函数的一系列训练样例子，每个训练样例对应路线中某棋盘状态和目标函数对此棋盘状态的评估值 Vtrain. Vtrain←Vest( successor( b ))

Generalizer 以训练样例作为输入，输出一个假设作为对目标函数的评估，这里对应的就是LMS更新法则。

实现过程中通过一个随机落子的player2 和 一个有学习能力的player1 不断训练，使player1从特定的训练样例中泛化，猜测一个一般函数，使其能够覆盖这些样例以及样例之外的情形。

* * *

实验发现player1胜率稳定在80%左右，和局15%左右。
