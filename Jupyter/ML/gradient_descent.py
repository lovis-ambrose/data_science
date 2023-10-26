import numpy as np
# notice that you need to keep adjusting the learning_rate and stop as soon as you get the minimum error rate
# privided we have our two lines and we want to derive a line of best fit
def gradient_descent(x,y):
    # define m currents and # of steps
    m_curr = b_curr = 0
    iterations = 1000   # will then fine tune it
    n = len(x)      # n is lentgh of the data points
    # define learning_rate ie start with like 0.001, gradually improve it. its like trial and error and seeing how alg behaves
    learning_rate = 0.001
    
    
            
    # we will start with few parameters and then see how the algorothm behaves
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)]) # val**2 deals with negative values
        # calculate m derivative and b derivative
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        # adjust the m_curr - learning rate
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        # print the values at each iteration
        print("m {}, b {}, cost {}, iterations {}".format(m_curr,b_curr,cost,i))
        
        

# lets use numpy array coz its faster that a python list
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])
