import pandas

data = pandas.read_csv("C:\\Users\\hp\\Downloads\\python\\squirrel-data-analysis\\Squirrel-Data.csv")
data_list = data['Primary Fur Color'].to_list()
gray_count = 0
cinnamon_count = 0
black_count = 0
for i in data_list:
    if i == 'Gray':
        gray_count +=1
    elif i == 'Black':
        black_count +=1
    elif i == 'Cinnamon':
        cinnamon_count+=1

dictionary={"Primary Fur Color": ["gray","black","cinnamon"],"count":[gray_count,black_count,cinnamon_count]}

dataframe = pandas.DataFrame.from_dict(dictionary)
dataframe.to_csv('C:\\Users\\hp\\Downloads\\python\\squirrel-data-analysis\\primary_count.csv') 