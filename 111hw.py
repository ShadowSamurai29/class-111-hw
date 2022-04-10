import statistics
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
import statistics
import csv

df = pd.read_csv("medium_data2.csv")
data = df["publication"].tolist()

fig = ff.create_distplot([data], ["publication"], show_hist=False)
fig.show()

dataset = []
for i in range (0, 100) :
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print("Mean of publication:-", mean)
print ("std_deviation of publication:-", std_deviation)

def random_set_of_mean(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["publication"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode = "lines", name = "MEAN"))
    fig.show()


mean_list = []
for i in range (0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
show_fig(mean_list)

mean = statistics.mean(mean_list) 
std_deviation = statistics.stdev(mean_list)
print("Mean of publication distribution:-", mean)

first_std_start, first_std_end = mean-std_deviation, mean+std_deviation
second_std_start, second_std_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_start, third_std_end = mean-(3*std_deviation), mean+(3*std_deviation)


df = pd.read_csv("sample_2.csv")
score_list = df["reading_time"].to_list()
mean1 = statistics.mean(score_list)
print("Mean of Sample 1 is{}".format(mean1))

fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.2], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.2], mode = "lines", name = "mean of stundets with worksheets"))
fig.add_trace(go.Scatter(x = [first_std_end,first_std_end],y = [0,0.2], mode = "lines", name = "std_end"))
fig.add_trace(go.Scatter(x = [second_std_end,second_std_end],y = [0,0.2], mode = "lines", name = "std_end2"))
fig.add_trace(go.Scatter(x = [third_std_end,third_std_end],y = [0,0.2], mode = "lines", name = "std_end3"))
fig.show()