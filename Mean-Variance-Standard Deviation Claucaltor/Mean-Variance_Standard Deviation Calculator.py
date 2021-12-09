import numpy as np

def calculate(list):
  
  # Checking for the length of the list 
  if len(list) == 9:
    list = np.reshape(list, (3,3))
  else:
    raise ValueError("List must contain nine numbers.")

  # Empty Dictionary
  calculations = {}

  # Getting all the elements row-wise and column wise
  yaxis = [[list[i][j] for i in range(3)] for j in range(3)]
  xaxis = [[list[j][i] for i in range(3)] for j in range(3)]

 
  # Mean row-wise, column-wise and after flattening
  yaxis_mean = [np.mean(i) for i in yaxis]
  xaxis_mean = [np.mean(i) for i in xaxis]
  flatten_mean = np.mean(list.flatten())

  # Variance row-wise, column-wise and after flattening
  yaxis_variance = [np.var(i) for i in yaxis]
  xaxis_variance = [np.var(i) for i in xaxis]
  flatten_variance = np.var(list.flatten())

  # Standard Deviation row-wise, column-wise and after flattening
  yaxis_std = [np.std(i) for i in yaxis]
  xaxis_std = [np.std(i) for i in xaxis]
  flatten_std = np.std(list.flatten())

  # Maximum Value row-wise, column-wise and after flattening
  yaxis_max = [np.max(i) for i in yaxis]
  xaxis_max = [np.max(i) for i in xaxis]
  flatten_max = np.max(list.flatten())

  # Minimum Value row-wise, column-wise and after flattening
  yaxis_min = [np.min(i) for i in yaxis]
  xaxis_min = [np.min(i) for i in xaxis]
  flatten_min = np.min(list.flatten())

  # Sum row-wise, column-wise and after flattening
  yaxis_sum = [np.sum(i) for i in yaxis]
  xaxis_sum = [np.sum(i) for i in xaxis]
  flatten_sum = np.sum(list.flatten())

  # Adding it all to the dictionary using keys-values pair
  calculations["mean"] = [yaxis_mean, xaxis_mean, flatten_mean]
  calculations["variance"] = [yaxis_variance, xaxis_variance, flatten_variance]
  calculations["standard deviation"] = [yaxis_std, xaxis_std, flatten_std]
  calculations["max"] = [yaxis_max, xaxis_max, flatten_max]
  calculations["min"] = [yaxis_min, xaxis_min, flatten_min]
  calculations["sum"] = [yaxis_sum, xaxis_sum, flatten_sum]

  return calculations