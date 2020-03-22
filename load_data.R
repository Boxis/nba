library(tidyverse)
library(data.table)

# load players bio
players <- read.csv("D:/my docs/github/nba/datasets/Players.csv")

names(players)[names(players) == "collage"] <- "college"

players <- subset(players, select = -c(X, born, birth_city, birth_state))

# load season data
season_stats <- read.csv("D:/my docs/github/nba/datasets/Seasons_Stats.csv")

season_stats <- subset(season_stats, select = -c(X))

merged_table <- left_join(season_stats, players)

# identify categorical variables
names(merged_table)[map(merged_table, class) == "factor" | map(merged_table, class) == "character"]

merged_table <- subset(merged_table, select = -c(college))

# keep first record of the player of the year
DT <- data.table(merged_table, key = "Year,Player")

DT <- DT[, head(.SD, 1), by = key(DT)]

DT <- DT[2:nrow(DT), ]
