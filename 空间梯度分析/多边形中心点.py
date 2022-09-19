import math

def center_geolocation(geoloactions):
    """
    输入多个经纬度坐标,格式:[[lon1,lat1],[lon2,lat2],......[lonn,latn]],找出中心点
    :param geoloactions:多个经纬度坐标
    :return: 中心点坐标--[lon,lat]
    """

    #求平均数,  同时角度弧度转化，得到中心点
    x = 0   # lon
    y = 0   # lat
    z = 0
    lenth = len(geoloactions)
    for lon, lat in geoloactions:
        lon = math.radians(float(lon))
        # radians()    Convert angle x from degrees to radians
        #               把角度x从度数转化为弧度
        lat = math.radians(float(lat))

        x += math.cos(lat) * math.cos(lon)
        y += math.cos(lat) * math.sin(lon)
        z += math.sin(lat)

        x = float(x/lenth)
        y = float(y/lenth)
        z = float(z/lenth)
    return (math.degrees(math.atan2(y, x)), math.degrees(math.atan2(z, math.sqrt(x*x + y*y))))



# 得到离中心点里程最近的里程
def geodistance(lon1, lat1, lon2, lat2):
    """
    得到两个经纬度坐标距离
    :param lon1: 坐标1 维度
    :param lat1: 坐标1 经度
    :param lon2: 坐标2 维度
    :param lat2: 坐标2 经度
    :return: distance 单位：千米
    """

    lon1, lat1, lon2, lat2 = map(math.radians, [float(lon1), float(lat1), float(lon2), float(lat2)])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) + math.sin(dlon/2)**2
    distance = 2 * math.asin(math.sqrt(a)) * 6371 * 1000    # 地球瓶颈半径 6371km
    distance = round(distance/1000, 3)
    print(distance)
    return distance


def getMaxestDistance(geolocations, centre):
    distances=[]
    for lon, lat in geolocations:
        d = geodistance(lat, lon, centre[1], centre[0])
        distances.append(d)
    # print(distances)
    return max(distances)


def getOnePolyygen(geolocations):

    '''
    输入多个经纬度坐标(格式：[[lon1, lat1],[lon2, lat2],....[lonn, latn]])，找出距该多边形中心点最远的距离
    :param geolocations:多个经纬度坐标(格式：[[lon1, lat1],[lon2, lat2],....[lonn, latn]])
    :return:center,neartDistance  多边形中心点  最远距离
    '''

    center=center_geolocation(geolocations) # 得到中心点
    neartDistance=getMaxestDistance(geolocations,center)
    # print(center,"-----------------",neartDistance)
    return center, neartDistance