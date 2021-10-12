library(ggplot2)
setwd("C:\\Users\\DELL\\Trip0\\")
data <- read.csv(file = "output1.csv", header = TRUE)
data <- data.frame(data)
names(data)

#Ve do thi
ggplot(data, aes(x=rank, color=hotel_name)) +
  geom_col(aes(x=rank, y=hotel_name, fill =hotel_name)) + 
  theme_grey() +
  labs(title="Đồ thị thể hiện xếp hạng của từng khách sạn")

ggplot(data, aes(x=review_number, y=hotel_name)) +
  geom_point(aes(colour = review_number)) +
  labs(title="Đồ thị thể hiện số lượt đánh giá của từng khách sạn")

ggplot(data, aes(x=review, y=hotel_name)) +
  geom_point(aes(colour = review)) +
  labs(title="Đồ thị thể hiện đánh giá chất lượng của từng khách sạn")