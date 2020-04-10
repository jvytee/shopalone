import io
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from datetime import datetime


def plot_visits(visits: list) -> bytes:
    t = np.arange(0, 24, 1/60)
    load = load_function(t, visits)

    fig, ax = plt.subplots()
    ax.plot(t, load)

    image = io.BytesIO()
    FigureCanvasAgg(fig).print_png(image)

    return image


def load_function(t: np.ndarray, visits: list) -> np.ndarray:
    today = datetime.today().date()
    load = np.zeros(t.shape)

    for visit in visits:
        visit_time = visit.tstamp

        if visit_time.date() == today:
            visit_minutes = 60*visit_time.hour + visit_time.minute
            load[visit_minutes:visit_minutes+30] += np.ones(30)

    return load
