# interactive stratigraphic filter toy model


# IMPORT LIBLARIES
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widget
import utils

# SET PARAMETERS
time = 20
T = time
timestep = 1
dt = timestep
t = np.array(np.linspace(0, T, T+1/dt))

muInit = 0
mu = muInit
muMax = 1
muMin = -muMax

sigmaInit = 1
sigma = sigmaInit
sigmaMax = 5
sigmaMin = 0

yView = 25


# DEFINE FUNCTIONS
def generate_elevation(themu, thesigma):
    nt = len(t)
    elev = np.zeros(nt)
    elev[0] = 0
    for j in np.arange(1,nt):
        jt = t[j]
        jump = np.random.normal(themu, thesigma, 1)
        elev[j] = elev[j-1] + jump

    return elev


def generate_stratigraphy(elev):
    nt = len(t)
    strat = np.zeros(nt)
    strat[-1] = elev[-1]
    for j in np.flipud(np.arange(0, nt-1)):
        strat[j] = np.array([elev[j], strat[j+1]]).min()

    return strat


def run_model(event):
    # read values from the sliders
    themu = slide_mu.val
    thesigma = slide_sigma.val
    T = time
    dt = timestep
    
    t = np.linspace(0, T, T+1/dt)
    elev = generate_elevation(themu, thesigma)
    strat = generate_stratigraphy(elev)

    zero_line.set_ydata(np.zeros(len(t)))
    elev_line.set_data(t, elev)
    strat_line.set_data(t, strat)
    # if np.abs(themu*T) > yView:
    #     ax.set_ylim([-np.abs(themu)*T*1.5, themu*T*1.5])
    # else:
    #     ax.set_ylim([-yView, yView])

    # redraw the canvas
    fig.canvas.draw_idle()


def slider_wrapper(event):
    if chk_conn.get_status()[0]:
        run_model(event)


def reset(event):
    slide_mu.reset()
    slide_sigma.reset()

    fig.canvas.draw_idle()


# run the program once with the initial values
elev = generate_elevation(muInit, sigmaInit)
strat = generate_stratigraphy(elev)


# setup the figure
plt.rcParams['toolbar'] = 'None'
plt.rcParams['figure.figsize'] = 11, 7
fig, ax = plt.subplots()
fig.canvas.set_window_title('SedEdu -- stratigraphic filter toy')
plt.subplots_adjust(left=0.075, bottom=0.1, top=0.95, right=0.5)
background_color = 'white'
ax.set_xlabel("time")
ax.set_ylabel("elevation")
plt.ylim(-yView, yView)


# add plot elements
zero_line, = plt.step(t, np.zeros(len(t)), linestyle=":", lw=1.5, color='black')
strat_line, = plt.step(t, strat, lw=2, color='red') # plot preserved
elev_line, = plt.step(t, elev, lw=1.5, color='grey')


# add slider
widget_color = 'lightgoldenrodyellow'

ax_mu = plt.axes([0.55, 0.8, 0.325, 0.05], facecolor=widget_color)
slide_mu = utils.MinMaxSlider(ax_mu, 'mean of elevation change', muMin, muMax, 
    valinit=muInit, valstep=0.05, valfmt='%g', transform=ax.transAxes)

ax_sigma = plt.axes([0.55, 0.6, 0.325, 0.05], facecolor=widget_color)
slide_sigma = utils.MinMaxSlider(ax_sigma, 'std. dev. of change', sigmaMin, sigmaMax, 
    valinit=sigmaInit, valstep=0.1, transform=ax.transAxes)


# add gui buttons
btn_run_ax = plt.axes([0.7, 0.35, 0.2, 0.15])
btn_run = widget.Button(btn_run_ax, 'Run', color='lightskyblue', hovercolor='0.975')

chk_conn_ax = plt.axes([0.7, 0.15, 0.25, 0.15], facecolor=background_color)
chk_conn_dict = {'connect sliders to run':'wl'}
chk_conn = widget.CheckButtons(chk_conn_ax, 
                               chk_conn_dict,
                               [False])

btn_reset_ax = plt.axes([0.7, 0.075, 0.1, 0.04])
btn_reset = widget.Button(btn_reset_ax, 'Reset', color=widget_color, hovercolor='0.975')


# connect widgets
slide_mu.on_changed(slider_wrapper)
slide_sigma.on_changed(slider_wrapper)
btn_reset.on_clicked(reset)
btn_run.on_clicked(run_model)


# show the results
plt.show()
