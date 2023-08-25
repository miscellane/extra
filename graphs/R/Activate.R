
Activate <- function () {

  # Packages
  packages <- c('data.table', 'tidyverse', 'moments', 'rmarkdown', 'latex2exp',
                'roxygen2', 'healthcareai', 'equatiomatic', 'rstatix', 'matrixStats', 'patchwork',
                'kableExtra', 'bookdown', 'paletteer', 'ggthemes', 'ggcorrplot')


  # Activate
  .activate <- function (x){
    library(x, character.only = TRUE)
    if (x == 'rmarkdown') {library(tinytex)}
  }
  lapply(packages[!(packages %in% c('tidyverse', 'healthcareai', 'equatiomatic'))], .activate)


  # Special Case
  if ('tidyverse' %in% packages) {
    lapply(X = c('magrittr', 'dplyr', 'tibble', 'ggplot2', 'stringr', 'lubridate'), .activate)
  }


  # Active libraries
  sessionInfo()

}