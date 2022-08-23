# Own neural network

## I present here my own neural network to predict positions (short or long) in daily.

- I was inspired by Gabriel Molina's paper "Stock Trading with Recurrent Reinforcement Learning (RRL)".
  http://cs229.stanford.edu/proj2006/Molina-StockTradingWithRecurrentReinforcementLearning.pdf 
- I used BTC data from Binance and added indicators from the Talib library to the dataset.
- The weights of the network are adjusted by maximizing a Sharpe ratio to the returns on investment calculated from the predicted positions of the algorithm.
- The algorithm automatically adds the actual positions (short or long) of the previous days to the input sequences.
- In addition, I have added the position it predicts (as mentioned in the paper) as an input.
- Although the network is not particularly powerful, it is still interesting and instructive to know how to code your own neural network without the help of state-of-the-art libraries like Keras/Tensorflow.

### Next? I am currently working on a new neural network (DRL) to predict market positions.
