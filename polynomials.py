import scipy as sp
import matplotlib.pyplot as plt


def error(function, function_x, function_y):
    """Approximation error. Squared distance of the model's prediction to the real data"""
    return sp.sum((function(function_x) - function_y)**2)

def generate_polynomial(sample_values, x_values, y_values, degree):
    """Generates polynomial for error checking"""
    # Parameters of function of degree 1
    # f(x) = FP1[0] * x + FP1[1]
    func_params = sp.polyfit(x_values, y_values, degree)
    # Curve fitting
    # Creating function from parameters
    function = sp.poly1d(func_params)
    # Draw line using FX values
    plt.plot(sample_values, function(sample_values), linewidth=4)
    # Legend in upper-left corner
    plt.legend(["d=%i" % function.order], loc="upper left")
    # How function values differ from real data
    error_val = error(function, x_values, y_values)
    print("Error %d: %f" % (degree, error_val))
    return error_val


DATA = sp.genfromtxt("web_traffic.tsv", delimiter="\t")

X = DATA[:, 0]
Y = DATA[:, 1]

X = X[~sp.isnan(Y)]
Y = Y[~sp.isnan(Y)]

# Generate 1000 values from 0 to X[-1] (which probably means: length)
FX = sp.linspace(0, X[-1], 1000)

generate_polynomial(FX, X, Y, 1)
generate_polynomial(FX, X, Y, 2)
generate_polynomial(FX, X, Y, 3)
generate_polynomial(FX, X, Y, 4)

plt.scatter(X, Y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w * 7 * 24 for w in range(10)],
           ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)

plt.grid()
plt.show()
