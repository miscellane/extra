
Aggregates <- function () {

  T <- read.csv(file = file.path(getwd(), 'warehouse', 'expenditure', 'metrics', 'aggregates.csv'))
  str(object = T)

  T <- dplyr::rename(T, annual_segment_rate = 'annual_segment_.', series_delta_rate = 'series_delta_.')
  str(object = T)


  T %>%
    dplyr::select(segment_code, year, annual_segment_total, annual_segment_rate, series_delta_rate) %>%
    tidyr::gather(key = 'partition', value = 'value', -c('segment_code', 'year')) %>%
    ggplot(mapping = aes(x = year, y = value, colour = segment_code)) +
    geom_point(alpha = 0.25) +
    facet_wrap(~partition, nrow = 3, ncol = 1, scales = 'free_y') +
    theme_minimal() +
    theme(panel.spacing = unit(x = 2, units = 'lines'),
          panel.grid.minor = element_blank())


}