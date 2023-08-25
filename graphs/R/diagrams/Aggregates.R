
Aggregates <- function () {

  T <- read.csv(file = file.path(getwd(), 'warehouse', 'expenditure', 'metrics', 'aggregates.csv'))
  str(object = T)

  T <- dplyr::rename(T, annual_segment_rate = 'annual_segment_.', series_delta_rate = 'series_delta_.')
  str(object = T)

  structure <- T %>%
    dplyr::select(segment_code, year, annual_segment_total, annual_segment_rate, series_delta_rate) %>%
    tidyr::gather(key = 'partition', value = 'value', -c('segment_code', 'year'))
  structure$partition <- factor(structure$partition,
                                levels = c( 'annual_segment_total', 'annual_segment_rate', 'series_delta_rate'),
                                labels = c('Segment Total (m£)', 'Segment (%)', 'Delta (%)'))
  str(object = structure)

  descriptions <- data.table::fread(file = file.path(getwd(), 'data', 'expenditure', 'expenditure_transaction_types.csv'),
                                    select = c('segment_code', 'segment_description'), strip.white = TRUE,
                                    colClasses = c(segment_code = 'character', segment_description = 'character'),
                                    data.table = FALSE) %>% dplyr::distinct(.keep_all = TRUE)
  descriptions


  diagram <- structure %>%
    ggplot(mapping = aes(x = year, y = value, colour = segment_code)) +
    geom_point(alpha = 0.25, na.rm = TRUE) +
    facet_wrap(~partition, nrow = 3, ncol = 1, scales = 'free_y') +
    theme_minimal() +
    theme(panel.spacing = unit(x = 2, units = 'lines'),
          panel.grid.minor = element_blank(),
          panel.grid.major = element_line(linewidth = 0.1),
          axis.text.x = element_text(size = 9), axis.text.y = element_text(size = 9),
          axis.title.x = element_text(size = 11), axis.title.y = element_text(size = 11)) +
    xlab(label = '\nyear\n') +
    ylab(label = '\n\n')

  diagram



  plotly::ggplotly(diagram)


}