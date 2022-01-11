setwd("C:\\Users\\DELL\\Trip0\\")
data <- read.csv(file = "dulieucrawl1.csv", header = TRUE)
View(data)
names(data)
str(data)

#Thong ke mo ta du lieu
#chuyen du lieu tu dang factor ve numeric
data$price_max <- as.numeric(as.character(data$price_max))
data$price_min <- as.numeric(as.character(data$price_min))
data$number_images_Traveler <- as.numeric(as.character(data$number_images_Traveler))
data$number_room_dining <- as.numeric(as.chara?ter(data$number_room_dining))
data$number_room_suite <- as.numeric(as.character(data$number_room_suite))
data$room_number <- as.numeric(as.character(data$room_number))
data$review_number <- as.numeric(as.character(data$review_number))
data$rank <- as.numeric(as.character(data$rank))
# Tao ham tinh mean, median, sd, sai so chuan, min, max
desc <- function(x, na.rm = TRUE)
{
  av <- mean(x, na.rm = TRUE)
  tv <- median(x, na.rm = TRUE)
  sd <- sd(x, na.rm = TRUE)
  se <- sd/sqrt(length(x))
  min <- min(x, na.rm = TRUE)
  max <- max(x, na.rm = TRUE)
  c(MEAN=av, MEDIAN=tv, SD=sd, STD=se, MIN=min, MAX=max)
}  

desc(data$price_max)
desc(data$price_min)
desc(data$number_images_Traveler)
desc(data$number_room_dining)
desc(data$number_room_suite)
desc(data$room_number)
desc(data$review_number)
desc(data$rank)

#Tinh mode
getmode <- function(v, na.rm = TRUE) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}  
  
getmode(data$price_max, na.rm = TRUE)
getmode(data$price_min)
getmode(data$number_images_Traveler)
getmode(data$number_room_dining, na.rm = TRUE)
getmode(data$number_room_suite, na.rm = TRUE)
getmode(data$room_number, na.rm = TRUE)
getmode(data$review_number, na.rm = TRUE)
getmode(data$rank, na.rm = TRUE)


#Tom tat cac truong du lieu bang summary()
summary(data)

#Su dung thu vien ggplot2 de ve bieu do
#install.packages("ggplot2", lib="C:/Users/DUC-PC/Documents/R/win-library/3.3")
#update.packages("ggplot2")
library(ggplot2)

#Ve bieu do
#Tao cac list chua tong cua tung du lieu trong tap du lieu
sum_data <- c(sum(data$price_max, na.rm=TRUE),
              sum(data$price_min, na.rm=TRUE),
              sum(data$review_number, na.rm=TRUE),
              sum(data$room_number, na.rm=TRUE),
              sum(data$number_images_Traveler, na.rm=TRUE),
              sum(data$number_room_dining, na.rm=TRUE),
              sum(data$number_room_suite, na.rm=TRUE),
              sum(data$rank, na.rm =TRUE))

sum_data_names <- c("price_max",
                    "price_min",
                    "review_numbers",
                    "room_number",
                    "number_images_Travaler",
                    "number_room_dining",
                    "number_room_suite",
                    "rank")

#Tao data frame tu 2 list tren
data01 <- data.frame(sum_data, sum_data_names)


#Ve bieu do the hien tong gia tri
#cua tung du lieu dinh luong cua tap du lieu
ggplot(data01, aes(x = sum_data, y = sum_data_names)) +
geom_col(aes(colour = sum_data_names)) + 
geom_text(aes(label=sum_data), vjust=0) +
  scale_x_log10() +
  labs(title="Tong gia tri cua du lieu dinh luong",
       x = "Count",
       y = "Columns")

# Tao cac list theo tung muc gia tu thap nhat
#den cao nhat va khong co gia (NA)
low = subset(data[,9], data$price_max <= 500000)
avg = subset(data[,9], data$price_max <= 1000000 & data$price_max > 500000)
high = subset(data[,9], data$price_max > 1000000)
na_price = subset(data[,9], is.na(data$price_max) == TRUE)

#Tao list chua length cua tung muc do gia
price <- c(length(low),
           length(avg),
           length(high),
           length(na_price))
price_classify <- c("Low",
                    "Average",
                    "High",
                    "N/A")

#tao data frame tu 2 list tren
data02 <- data.frame(price, price_classify)

#Ve bieu thi the hien so luong gia tung khach san
#theo tung muc do tu thap den cao va khong co gia (NA)
ggplot(data02, aes(x = price, y = price_classify ,fill = price_classify)) +
  geom_bar(stat = "identity") +
  geom_text(aes(label=price), vjust=0) +
  labs(title="So luong khach san voi muc gia theo cap do",
       x = "Count",
       y = "Columns")

#Ve bieu do the hien chat luong danh gia cua tung khach san
#theo tung luot review
ggplot(data = data, mapping = aes(x = review)) +
  geom_bar(binwidth = 5,                    # chieu rong cua cot
           aes(fill = review),              # mau cua cot
                     alpha = 1) +           # do trong suot cua cot
  labs(title= "Danh gia chat luong cua tung khach san",
       x = "Review")


#Ve bieu do the hien so luong khach san
#su dung cung loai ngon ngu
ggplot(data = data[1:100,], mapping = aes(x =languages)) +
  geom_bar(binwidth = 1,                # chieu rong cua cot
           color = "red",               # mau vien
           fill = "yellow",               # mau cua cot
           alpha = 1) +               # do trong suot cua cot
  labs(title="So luong khach san su dung ngon ngu giong nhau ",
       x = "Language") + 
  theme(axis.text.x = element_text(size = 10, angle = 90))


