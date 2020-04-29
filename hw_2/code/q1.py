

import numpy as np
from matplotlib import pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np



def main():


    beta_list = np.linspace(start = 1, stop = 30, num = 30, dtype = int)
    fail_prob_list =  np.linspace(start = 0, stop = 1.0, num = 11, dtype=float)


    calc_s_new = lambda B, p : (1-(p**2)) / (2 + B)
    calc_s_original = lambda B, p: (1-p) / (1 + B)

    s_new_arr           = np.empty((len(beta_list),len(fail_prob_list)))
    s_original_arr      = np.empty((len(beta_list),len(fail_prob_list)))
    s_difference        = np.empty((len(beta_list),len(fail_prob_list)))
    s_difference_binary = np.empty((len(beta_list),len(fail_prob_list)))

    for B_idx, B in enumerate(beta_list):
        for p_idx, p in enumerate(fail_prob_list):
            s_new_arr[B_idx][p_idx] = calc_s_new(B,p)
            s_original_arr[B_idx][p_idx] = calc_s_original(B,p)
            s_difference[B_idx][p_idx] = s_original_arr[B_idx][p_idx]  - s_new_arr[B_idx][p_idx] 

            if s_difference[B_idx][p_idx] > 0 :
                s_difference_binary[B_idx][p_idx] = 1
            else:
                s_difference_binary[B_idx][p_idx] = 0

    # for the plot
    s_new_rot = np.fliplr(np.rot90(s_new_arr, axes=(1,0)))
    s_original_rot = np.fliplr(np.rot90(s_original_arr, axes=(1,0)))
    s_diff_rot = np.fliplr(np.rot90(s_difference, axes=(1,0)))
    s_binary_rot = np.fliplr(np.rot90(s_difference_binary, axes=(1,0)))

    beta_grid, p_grid = np.meshgrid(beta_list, fail_prob_list)

    fig = plt.figure()
    ax = fig.gca(projection='3d')



    # Plot the surface.
    surf = ax.plot_surface(beta_grid, p_grid, s_diff_rot, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    plt.show()



    fig, ax = plt.subplots()
    ax.imshow(s_binary_rot)

    ax.set_xticks(np.arange(len(beta_list)))
    ax.set_yticks(np.arange(len(fail_prob_list)))

    ax.set_xticklabels(beta_list)
    ax.set_yticklabels(np.round(fail_prob_list, 3))

    ax.set_xlabel("Beta")
    ax.set_ylabel("P")

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()

