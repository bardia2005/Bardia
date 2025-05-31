# from scipy.special import comb
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# N = 100000

# theta_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# prior_probability = [0.05, 0.05, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.05, 0.05]
# likelihood = [float(format((comb(20, 12) * (i ** 12) * ((1 - i) ** (20 - 12))), 'f')) for i in theta_values]
# unnormalized_posterior = [prior_probability[i] * likelihood[j] for i in range(10) for j in range(10) if i == j]
# normalized_posterior = [i / sum(unnormalized_posterior) for i in unnormalized_posterior]

# data = {
#     "Theta Values": theta_values,
#     "Prior Probality": prior_probability,
#     "Likelihood": likelihood,
#     "Unnormalized Posterior": unnormalized_posterior,
#     "Normalized Posterior": normalized_posterior
# }

# fig, ax = plt.subplots()    

# df = pd.DataFrame(data)
# print(df)

# """
# # Re-import necessary packages after code execution state reset
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import beta

# # Range of theta
# theta = np.linspace(0, 1, 500)

# # Define different priors
# flat_prior = beta.pdf(theta, a=1, b=1)          # Uniform
# right_skewed_prior = beta.pdf(theta, a=2, b=5)  # Skewed toward 0
# left_skewed_prior = beta.pdf(theta, a=5, b=2)   # Skewed toward 1

# # Plotting
# plt.figure(figsize=(10, 6))
# plt.plot(theta, flat_prior, label='Flat Prior (Beta(1,1))', color='gray')
# plt.plot(theta, right_skewed_prior, label='Right-Skewed Prior (Beta(2,5))', color='red')
# plt.plot(theta, left_skewed_prior, label='Left-Skewed Prior (Beta(5,2))', color='green')

# plt.title('Different Prior Distributions for θ')
# plt.xlabel('θ')
# plt.ylabel('Density')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# """

# # import numpy as np
# # import matplotlib.pyplot as plt

# # fig = plt.figure()
# # ax = fig.add_subplot(111)

# # x=[1,2,3,4,5,6,7,8,9,10]
# # y=[1,1,1,2,10,2,1,1,1,1]
# # line, = ax.plot(x, y)

# # ymax = max(y)
# # xpos = y.index(ymax)
# # xmax = x[xpos]

# # ax.annotate('local max', xy=(xmax, ymax), xytext=(xmax, ymax+5),
# #             arrowprops=dict(facecolor='black', shrink=0.05),
# #             )

# # ax.set_ylim(0,20)
# # plt.show()

# Re-import required packages due to code execution state reset
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Observed data
s = 12
n = 20

# Range of theta
theta = np.linspace(0, 1, 500)

# Prior: Uniform Beta(1, 1)
prior = beta.pdf(theta, a=1, b=1)

# Likelihood (up to constant): θ^s * (1-θ)^(n-s)
likelihood = theta**s * (1 - theta)**(n - s)
likelihood /= np.max(likelihood)  # scale for plotting

# Posterior: Beta(13, 9)
posterior = beta.pdf(theta, a=1 + s, b=1 + n - s)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(theta, prior, label='Prior: Beta(1, 1)', color='green')
plt.plot(theta, likelihood, label='Likelihood (scaled)', color='orange')
plt.plot(theta, posterior, label='Posterior: Beta(13, 9)', color='blue')
plt.title('Bayesian Updating: Prior × Likelihood → Posterior')
plt.xlabel('θ')
plt.ylabel('Density (scaled)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
