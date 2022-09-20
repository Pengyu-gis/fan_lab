import pandas as pd
path = 'file.csv'


# 使用pandas读入
data = pd.read_csv(path)

# 按列分离数据
lng_o = data['lng_o']
lat_o = data['lat_o']

# print(lat_o,lng_o)

# 用zip()函数使两个list变成list of tuple
zipped = zip(lng_o,lat_o)
geolocations = list(zipped)
print(geolocations)
