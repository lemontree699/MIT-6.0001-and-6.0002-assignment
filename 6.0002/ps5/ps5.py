# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: myz
# Collaborators (discussion):
# Time: 20190619

import pylab
import re
import math

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    
    coefficients = []  # 存储系数
    for i in range(len(degs)):
        coefficients.append(pylab.polyfit(x,y,degs[i]))
    # print(coefficients)
    return coefficients

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    # TODO
    
    mean = y.mean()  # 计算y的平均值
    temp1 = (y - estimated) ** 2
    temp2 = (y - mean) ** 2
    return 1 - temp1.sum() / temp2.sum()

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    # TODO
    
    for model in models:
        p = pylab.poly1d(model)
        r_2 = r_squared(y, p(x))  # 计算r^2
        pylab.figure()
        pylab.plot(x, y, 'b.', label = 'Data points')  # 用蓝色的散点代表数据点
        pylab.plot(x, p(x), 'r-', label = 'Curve Fitting')  # 用红色的实线代表拟合的曲线
        pylab.legend()
        if len(model) == 2:  # 如果是一条直线，即最高项次数为1
            pylab.title('Degree of this model: ' + str(len(model) - 1) + '\n' + 'R^2: ' + str(r_2) + '\n' + 'Ratio of Standard Error: ' + str(se_over_slope(x, y, p(x), model)))
        else:  # 如果最高项次数大于1
            pylab.title('Degree of this model: ' + str(len(model) - 1) + '\n' + 'R^2: ' + str(r_2))
        pylab.xlabel('Years')
        pylab.ylabel('Degrees Celsius')
        pylab.show()


def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    # TODO
    
    temperature_data = []  
    for year in years:
        total_temp = 0  # 某一年所有城市的总气温
        for city in multi_cities:
            total_temp += climate.get_yearly_temp(city, year).mean()
        avg_temp = total_temp / len(multi_cities)  # 某一年所有城市的平均气温
        temperature_data.append(avg_temp)
    return temperature_data

def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    # TODO
    
    moving_avg = []
    for i in range(1, len(y) + 1):
        if i < window_length:  # 如果当前长度小于window_length，则只计算目前已经存在的数的平均数
            moving_avg.append(pylab.array(y[:i]).mean())
        else:  # 如果当前长度大于等于window_length，则选取window_length个数，求平均值
            moving_avg.append(pylab.array(y[i - window_length:i]).mean())
    return moving_avg

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    # TODO
    
    return math.sqrt(((y - estimated) ** 2).sum() / len(y))

def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    # TODO
    
    temperature_data = []  
    for year in years:
        temperature_avg = []  # 存储各个城市每一天的平均气温
        for i in range(len(multi_cities)):
            if i == 0:  # 如果是第一个城市，就将本年的气温数据赋值给temperature_avg
                temperature_avg = climate.get_yearly_temp(multi_cities[i], year)
            else:  # 如果是之后的城市，将气温数据相加
                temperature_avg += climate.get_yearly_temp(multi_cities[i], year)
        temperature_avg /= len(multi_cities)  # 求出各个城市每一天的平均气温
        temperature_data.append(temperature_avg.std())  # 再将各个城市一年中每天的平均气温求标准差
    return temperature_data

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    # TODO
    
    for model in models:
        p = pylab.poly1d(model)
        RMSE = rmse(y, p(x))  # 计算rmse
        pylab.figure()
        pylab.plot(x, y, 'b.', label = 'Data points')  # 用蓝色的散点代表数据点
        pylab.plot(x, p(x), 'r-', label = 'Curve Fitting')  # 用红色的实线代表拟合的曲线
        pylab.legend()
        pylab.title('Degree of this model: ' + str(len(model) - 1) + '\n' + 'RMSE: ' + str(RMSE))
        pylab.xlabel('Years')
        pylab.ylabel('Degrees Celsius')
        pylab.show()

if __name__ == '__main__':

    climate = Climate('data.csv')

    # Part A.4
    # # A4.I
    # temperature_data = []  # 存储天气信息
    # for year in TRAINING_INTERVAL:
    #     temperature_data.append(climate.get_daily_temp('NEW YORK', 1, 10, year))
    # model = generate_models(pylab.array(TRAINING_INTERVAL), pylab.array(temperature_data), [1])  # 生成模型
    # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL), pylab.array(temperature_data), model)  # 画图

    # # A4.Ⅱ
    # temperature_data = []  # 存储天气信息
    # for year in TRAINING_INTERVAL:
    #     temperature_data.append(climate.get_yearly_temp('NEW YORK', year).mean())
    # model = generate_models(pylab.array(TRAINING_INTERVAL), pylab.array(temperature_data), [1])  # 生成模型
    # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL), pylab.array(temperature_data), model)  # 画图

    # Part B
    # temperature_data = gen_cities_avg(climate, CITIES, TRAINING_INTERVAL)
    # model = generate_models(pylab.array(TRAINING_INTERVAL), pylab.array(temperature_data), [1])  # 生成模型
    # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL), pylab.array(temperature_data), model)  # 画图

    # Part C
    # temperature_data = moving_average(gen_cities_avg(climate, CITIES, TRAINING_INTERVAL), 5)
    # model = generate_models(pylab.array(TRAINING_INTERVAL), pylab.array(temperature_data), [1])  # 生成模型
    # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL), pylab.array(temperature_data), model)  # 画图

    # Part D.2
    # # D2.Ⅰ
    # train_data = moving_average(gen_cities_avg(climate, CITIES, TRAINING_INTERVAL), 5)
    # model = generate_models(pylab.array(TRAINING_INTERVAL), pylab.array(train_data), [1, 2, 20])  # 生成模型
    # # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL), pylab.array(train_data), model)  # 画图

    # # D2.Ⅱ
    # test_data = moving_average(gen_cities_avg(climate, CITIES, TESTING_INTERVAL), 5)
    # evaluate_models_on_testing(pylab.array(TESTING_INTERVAL), pylab.array(test_data), model)  # 利用之前的模型预测数据画图

    # Part E
    # temperature_data = moving_average(gen_std_devs(climate, CITIES, TRAINING_INTERVAL), 5)
    # model = generate_models(pylab.array(TRAINING_INTERVAL), pylab.array(temperature_data), [1])  # 生成模型
    # evaluate_models_on_training(pylab.array(TRAINING_INTERVAL), pylab.array(temperature_data), model)  # 画图

