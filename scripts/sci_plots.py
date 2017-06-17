import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from astropy import log

from functionality import *

def sci_plots(etable):
    #GRID SET UP
    figure2 = plt.figure(figsize = (11, 8.5), facecolor = 'white')
    sci_grid = gridspec.GridSpec(5,7)
    plt.style.use('grayscale')

    #IDS, num_events, stdev, colors = hist_use(etable)

    #Light Curve
    log.info('Building light curve')
    plt.subplot(sci_grid[1:5,:2])
    meanrate = plot_light_curve(etable,binsize=1.0)

    #Fast / Slow (Slow x, Fast y)
    log.info('Building fast/slow')
    plt.subplot(sci_grid[1:3,2:5])
    plot_slowfast(etable)

    #Energy Spectrum
    log.info('Building energy spectrum')
    plt.subplot(sci_grid[3:5,2:5])
    plot_energy_spec(etable)

    #Power SPpectrum
    log.info('Building power spectrum')
    fourier = plt.subplot(sci_grid[3:5,5:7])
    #power_spec = plot_fft_of_power(time, data1)

    #PULSE PROFILE
    log.info('Building pulse profile')
    pulse = plt.subplot(sci_grid[1:3,5:7])
##    pulse = pulse_profile(data1, pulse, event_flags)

    #Making the plot all nice and stuff
    plt.subplots_adjust(left = .07, right = .99, bottom = .05, top = .9, wspace = .7, hspace = .8)

    figure2.suptitle('Object: {0} at {1}'.format(etable.meta['OBJECT'],etable.meta['DATE-OBS']),
        fontsize=18)

    # Add text info here:
    plt.figtext(.07, .9, 'Mean count rate {0:.3f} c/s'.format(meanrate), fontsize = 10)


    return figure2
