---
title: 'Theory of the stratigraphic filter'
author:
- Andrew J. Moodie
date: \today
bibliography: refs.bib
---

## Elevation and stratigraphy

Sedimentary rocks record the conditions of Earth's surface at various times in the past.
Sediments are retained in the rock record only if they are *never* eroded at some later time.
This theory, coupled with the observation that measured sedimentation rates decreases with increasing time span measured over (often called the Sadler effect [@sadler_1981]), lead researchers to try and understand why the stratigraphy records only a vanishingly small fraction of time---in other words, the stratigraphic record is remarkably incomplete [@paola_2019].
<!-- This fact leads to the concept of *accommodation*, which is a measure of how space is available for sediment accumulation and preservation.
Accommodation is generally largest in river and delta systems, where deposition is driven by the process of migrating bedforms.
 -->
@tipper_1983 was the first to apply a random walk model to the problem of stratigraphic completeness, wherein he presented a model for how erosional events eliminate positive elevation changes from deposition, and thus preclude large periods of time from the stratigraphic record.

<!-- posited that because erosional events remove periods of time from the rock record, the averaged sedimentation rates will appear slower.  -->
Consider Figure 1, which depicts the surface elevation at a single location over time (black line), where the surface elevation  is changed by a random amount ($dz$) each timestep ($dt$); thus, the resulting  timeseries of elevation is called a *random walk*. 
The *stratigraphic filter* is the process by which periods of time (typically when the elevation was relatively high) are removed by erosive events.
Stratigraphy is calculated by finding the most recent time that the surface elevation was equal to the corresponding stratigraphic position [@schumer_2011].

![Schematic drawing of a random walk model for stratigraphic development. Each timestep the elevation is changed by adding a randomly drawn $\Delta z$ value from a probability distribution. The stratigraphy is calculated after the model run is completed, by the routine presented in the following section.](figures/schematic.png){ width=600px }

For more information, see the review of time and stratigraphy given by @paola_2019.

## Varying the distribution of the random walk

### Aggradation and "drift"

### Variance of elevation change


## Discussion questions

1. 
1. Write an algorithm (or mathematical expression) for calculating the stratigraphy. 

## References
