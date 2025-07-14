# Customized from donnemartin/data-science-ipython-notebooks
# Original: https://github.com/donnemartin/data-science-ipython-notebooks
# Cloned on: 2025-07-14

ann = ANN(2, 10, 1)
%timeit -n 1 -r 1 ann.train(zip(X,y), iterations=2)
plot_decision_boundary(ann)
plt.title("Our next model with 10 hidden units")
