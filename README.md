<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>




<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">VicRoads CrashStats</h3>

  <p align="center">
    Halving fatality rate by 2030
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## Overview & Files

This is an analysis of the [VicRoads CrashStats](https://discover.data.vic.gov.au/dataset/crash-stats-data-extract), aiming to provide value and realistic plans to help achieve the targets of [Victorian Road Safety Strategy 2021-2030](https://www.tac.vic.gov.au/road-safety/victorian-road-safety-strategy/victorian-road-safety-strategy-2021-2030).

**Target of repository:** Lower fatality rate by establishing additional emergency response sites thor.

All of the code files in this directory were ran locally.


Dependencies include scikit-learn, geopy, darts, and others. The Dependency list will be updated later.

There is 6 files/folders included:
* `data_preprocessing.ipynb`
* `Initial_EDA.ipynb`
* `hospital_EDA.ipynb`
* `fatality_forecast.ipynb`
* `generate_hospital_recommendation.ipynb`
* `./utils`
<br>


### data_preprocessing.ipynb, Initial_EDA.ipynb, hospital_EDA.ipynb

Scrath pad notebooks to quickly visualize data and test out ideas. Code is not cleaned up and should not be used in production.

### fatality_forecast.ipynb

Includes forecast model and measuring the impact if we established more emergency response sites.

### generate_hospital_recommendation.ipynb

Generate recommended emergency response sites produced by K means.

### ./utils

Common functions used between notebooks. Currently only contains the data_loader.

<br>

