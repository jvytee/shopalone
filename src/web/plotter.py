import io
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from dateutil import parser


def plot_visits(visits: list) -> bytes:
    t = np.arange(0, 24*60)
    f = np.sin(1/60 * t)

    fig, ax = plt.subplots()
    ax.plot(t, f)

    image = io.BytesIO()
    FigureCanvasAgg(fig).print_png(image)

    return image
