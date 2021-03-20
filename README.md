# 1. models
## 1.1 Back propagation (BP) neural network model
BP neural network model is a three-layer feed forward network composed of input layer, hidden layer and output layer. Each layer contains several disconnected neuron nodes, and the adjacent nodes are connected according to a certain weight. The direction of information transmission is from input layer to hidden layer to output layer. There is transfer matrix between input layer and hidden layer, and transfer matrix exists between hidden layer and output layer. If the difference between the actual output and the expected output can not meet the required error, the error value is fed back layer by layer along the network path, and the connection weights and thresholds of each layer are corrected.

## 1.2 Artificial bee colony algorithm optimization of BP neural network model
Artificial bee colony (ABC) algorithm is inspired by the intelligent behavior of bees. In ABC algorithm, the location of food represents a possible solution of the optimization problem, while the amount of nectar represents the quality or fitness of the corresponding solution.

Firstly, the algorithm generates the initial population randomly, and then sets the limit and the maximum number of cycles. After initialization, the bees begin to search circularly: using greedy mechanism to search the neighborhood of the old solution. If the fitness of the new solution is greater than that of the old solution, the bee will forget the old solution and remember the new one. Then the possible values (Pi) of these new solutions are calculated, and the onlookers begin to use the greedy mechanism to search for new solutions and solutions remembered by bees near the possible values (Pi). If the latest solutions obtained can no longer be updated, the Scout will abandon these solutions and replace them with new ones. This cycle reaches the maximum number of cycles. There is only one scout per cycle.

## 1.3 Monte Carlo simulation
The principle of Monte Carlo simulation option pricing can be understood in this way. First, according to the given price movement process of the underlying asset, the price change of the underlying asset is simulated. When the number of simulations reaches a certain number, the average value is taken to obtain the expected value. According to the law of large numbers, the Monte Carlo simulation results finally meet the convergence. Compared with the BS model, this method has the following advantages: First, it is flexible, easy to implement and improve; Second, the error and convergence speed of the simulation estimation have nothing to do with the dimensionality of the problem, and it can better solve the multi-asset option pricing and The path depends on the issue of option pricing. However, in order to obtain high accuracy, thousands of simulations are usually required, so the Monte Carlo method usually takes more time than the BS model.

# 2. prediction results and option trading strategy
## 2.1 data and statistics
The correlation among three kinds of volatilities can be seen in the Table below.
|                      |IV               |Realized Volatility  |VIX           |
|----------------------|-----------------|---------------------|--------------|
|IV                    |1                |0.5028               |0.7220        |
|Realized Volatility   |0.5028           |1                    |0.6988        |
|VIX                   |0.7220           |0.6899               |1             |

The figure below shows the comparisons between predicted and sample true values based on ABC-BP neural network model.
![Image text](https://github.com/algo21-220040088/Assignment1/blob/main/screenshots/fig_1.jpg)

The figure below shows the comparisons based on BP and ABC-BP neural network model optimal and true value.
![Image text](https://github.com/algo21-220040088/Assignment1/blob/main/screenshots/fig_2.jpg)

The figure below shows comparison of MSE based on BP neural network model and ABC-BP neural network model.we can conclude that MSE decreases with the increase of iterations, and the MSE of ABC-BP neural network model is obviously smaller than that of BP neural network model under the optimal fitting condition.
![Image text](https://github.com/algo21-220040088/Assignment1/blob/main/screenshots/fig_3.jpg)

## 2.2 out-of-sample testing

