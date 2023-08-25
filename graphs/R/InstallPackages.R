
InstallPackages <- function (){

  packages <- c('data.table', 'tidyverse', 'moments', 'rmarkdown', 'latex2exp',
                'roxygen2', 'healthcareai', 'equatiomatic', 'rstatix', 'matrixStats', 'patchwork',
                'kableExtra', 'bookdown', 'paletteer', 'ggthemes', 'ggcorrplot')

  # Install
  .install <- function(x){
    if (!require(x, character.only = TRUE)) {
      install.packages(x, dependencies = TRUE)
      if (x == 'rmarkdown') {tinytex::install_tinytex()}
    }
  }
  lapply(packages, .install)

}