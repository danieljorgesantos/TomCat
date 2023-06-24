import numpy as np
import pandas as pd

data = np.array([
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
])

df = pd.DataFrame(data, columns=['Open', 'High', 'Low', 'Close', 'Volume'])

print('data', data)

# python class
class Enviroment:
    def __init__(self, cashAvaiable):
        
        self.portfolio = []
        self.cashAvaiable = cashAvaiable
        self.totalInvested = 0
        self.profitLoss = 0
        self.portfolioValue = 1000
        
    # resets the enviroment to initial state    
    def reset(self):
        self.portfolio = []
        self.cashAvaiable = 1000
        self.totalInvested = 0
        self.profitLoss = 0
        self.portfolioValue = 1000
        
    # observes the enviroment and agent state    
    def observation(self):
        print([
            self.portfolio,
            self.cashAvaiable,
            self.totalInvested,
            self.profitLoss,
            self.portfolioValue
        ])
        pass
    
    # action 1 buy a certain quantity
    def action(self, action):
        self.cashAvaiable -= 200
        print('----> buy', quantity)
        pass

    # action 2 sell a certain quantity
    def sell(self, quantity):
        print('----> sell', quantity)
        pass

env = Enviroment(1000)
env.observation()
#env.buy(200)
env.observation()
env.reset()
env.observation()
    