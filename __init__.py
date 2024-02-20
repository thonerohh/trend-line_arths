from random import randint, seed
import sys

# Set a seed for reproducibility
seed_value = 12345  # You can change this value to any integer
seed(seed_value)

# length
N = 4
NH = N // 2

# create random data for x and y as N+1
x = [randint(1, N) for _ in range(N)]
x = [1, 2, 3, 4]

# x_sorted = sorted(x)

def test3(x):
  x1 = x[NH:]
  x0 = x[:NH]

  print ("x: ", x)
  print ("x1: ", x1)
  print ("x0: ", x0)

  x_sum = sum(x)
  x1_sum = sum(x1)
  x0_sum = sum(x0)

  diff_coef = x1_sum / x0_sum

  x_med = x_sum / N

  x_amount_below = sum(1 for i in x if i < x_med)
  x_amount_above = sum(1 for i in x if i > x_med)

  x1_amount_below = sum(1 for i in x1 if i < x_med)
  x1_amount_above = sum(1 for i in x1 if i > x_med)

  x0_amount_below = sum(1 for i in x0 if i < x_med)
  x0_amount_above = sum(1 for i in x0 if i > x_med)

  print ("Above Median X: ",x_amount_above)
  print ("Below Median X: ",x_amount_below)

  print ("Above Median X1: ",x1_amount_above)
  print ("Below Median X1: ",x1_amount_below)

  print ("Above Median X0: ",x0_amount_above)
  print ("Below Median X0: ",x0_amount_below)

  x1_med = x1_sum / (N // 2)
  x0_med = x0_sum / (N // 2)

  print ('Median: ',x_med)
  print ('Median x1: ', x1_med)
  print ('Median x0: ', x0_med)

  x_amp = abs(x1_med - x0_med)

  print ('X amplitude: ', x_amp)

  x_stab = abs(x_med - x1_med)
  x1_stab = x_med - x1_med
  x0_stab = x_med - x0_med

  print("X Stable Step: ", x_stab)
  print("X1 Stable Step: ", x1_stab)
  print("X0 Stable Step: ", x0_stab)

  x1_stab_coef = x_med / x1_med
  x0_stab_coef = x_med / x0_med

  print("X1 Median inside X median: ",x1_stab_coef)
  print("X0 Median inside X median: ",x0_stab_coef)

  stab_coef_amp = abs(x1_stab_coef - x0_stab_coef) / 2
  debug_sca = stab_coef_amp * x_med

  error_appr = abs(debug_sca - x_stab)
  error_appr_coef = error_appr / x_stab

  print ("Amplitude of Error: ", error_appr)
  print("Amplitude of Error Percentage: {:.2f} %".format(error_appr_coef * 100))

__name__ == "__main__" and test3(x)
  
