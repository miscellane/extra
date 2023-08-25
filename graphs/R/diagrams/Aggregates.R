
Aggregates <- function () {

  T <- read.csv(file = file.path(getwd(), 'warehouse', 'expenditure', 'metrics', 'aggregates.csv'))
  str(object = T)

  T <- dplyr::rename(T, annual_segment_rate = 'annual_segment_.', series_delta_rate = 'series_delta_.')
  str(object = T)

  T %>%
    dplyr::select(segment_code, epoch, annual_segment_total, annual_segment_rate, series_delta_rate)
}