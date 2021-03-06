import numpy as np
from matplotlib import pyplot as plt


def plot_gaussian(mu, lmbda, color='b', label='', alpha=1.0, ax=None,
                  artists=None):
    ax = ax if ax else plt.gca()

    # t = np.hstack([np.arange(0, 2 * np.pi, 0.01), 0])
    # circle = np.vstack([np.sin(t), np.cos(t)])
    # ellipse = np.dot(np.linalg.cholesky(lmbda), circle)

    ti = np.linspace(0, 2 * np.pi, 50)
    vec = np.array([np.cos(ti), np.sin(ti)]).transpose()
    eig_val, eig_vec = np.linalg.eig(lmbda)
    ellipse = 1.96 * np.dot(np.dot(vec, np.diag(np.sqrt(eig_val))), eig_vec.transpose())

    if artists is None:
        point = ax.scatter([mu[0]], [mu[1]], marker='D', color=color, s=4,
                           alpha=alpha)

        line, = ax.plot(ellipse[:, 0] + mu[0], ellipse[:, 1] + mu[1],
                        linestyle='-', linewidth=2, color=color, label=label,
                        alpha=alpha)
    else:
        line, point = artists
        point.set_offsets(mu)
        point.set_alpha(alpha)
        point.set_color(color)
        line.set_xdata(ellipse[0, :] + mu[0])
        line.set_ydata(ellipse[1, :] + mu[1])
        line.set_alpha(alpha)
        line.set_color(color)

    return (line, point) if point else (line,)
