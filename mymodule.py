import matplotlib.pyplot as plt

def intensity_histogram(img):
    by_color = img.ravel(order = 'F').reshape((3,img.shape[0] * img.shape[1]))
    colors = ['red', 'green', 'blue']
    plt.hist(by_color.T, 30, density=True, histtype='step', color=colors, label=colors)
    plt.title("Intensity by RGB colors")