import sqlite3
import pandas as pd
from math import e
import datetime


#sigma_1:远月波动率
def calculate_sigma(TRADE_DT, OPTION_ENDTRADE, option_string):

    #连接.db文件
    my_db = sqlite3.connect('D:\\pc\\Desktop\\Algo_Trading\\assignment_1\\option.db')

    #对数据库进行操作，取出所需数据
    c = my_db.cursor()
    select_part = "SELECT K,CALL_PUT,CLOSE"
    from_part="FROM " + option_string + ""
    condition_part  = 'WHERE TRADE_DT= {x} AND OPTION_ENDTRADE={y}'\
    .format(x=TRADE_DT,y=OPTION_ENDTRADE)
    order_part = "ORDER BY K"
    c.execute(select_part + " " + from_part + " " + condition_part + " " + order_part)
    tables = c.fetchall()
    result = pd.DataFrame(tables)
    result.columns = ['K', 'CALL_PUT', 'CLOSE']
    result['K'] = result['K'].astype(float)
    result['CALL_PUT'] = result['CALL_PUT'].astype(str)
    result['CLOSE'] = result['CLOSE'].astype(float)

    #将日期的格式从数字转化为20xx-xx-xx
    d1 = datetime.datetime(TRADE_DT // 10000, (TRADE_DT % 10000) // 100, TRADE_DT % 100)
    d2 = datetime.datetime(OPTION_ENDTRADE // 10000, (OPTION_ENDTRADE % 10000) // 100, OPTION_ENDTRADE % 100)

    #计算间隔天数
    NT = d2 - d1
    T = NT.days / 365

    # 计算K_i：由小到大的所有执行价(i = 1,2,3, … . )
    c = result.shape[0] // 2
    K_i = [0] * c
    price_call = [0] * c
    price_put = [0] * c
    for i in range(c):
        K_i[i] = result.loc[2 * i, 'K']
        price_call[i] = result.loc[2 * i, 'CLOSE']
        price_put[i] = result.loc[2 * i + 1, 'CLOSE']

    # 计算S：认购期权价格与认沽期权价格相差最小的执行价
    price_difference = price_call[0] - price_put[0]
    k = 0
    for i in range(1, c):
        if abs(price_call[i] - price_put[i]) < price_difference:
            price_difference = abs(price_call[i] - price_put[i])
            k = i
    S = K_i[k]

    # 计算F：S + eRT × [认购期权价格(S) − 认沽期权价格(S)]
    F = S + e ** (R * T) * (price_call[k] - price_put[k])

    # 计算k_0：小于 F 且最接近于 F 的执行价
    k_0 = 0
    for i in range(c - 1):
        if F > K_i[c - 1]:
            k_0 = K_i[c - 1]
            break
        if K_i[i] < F and K_i[i + 1] >= F:
            k_0 = K_i[i]
            break

    # 计算∆Ki，第i个执行价所对应的执行价间隔，一般为K_i+1 − K_i−1/2
    delta_k_i = [0] * c
    for i in range(1, c - 1):
        delta_k_i[i] = (K_i[i + 1] - K_i[i - 1])*0.5
    price_k_i = [0] * c
    for i in range(1, c - 1):
        if K_i[i] < k_0:
            price_k_i[i] = price_put[i]
        elif K_i[i] > k_0:
            price_k_i[i] = price_call[i]
        else:
            price_k_i[i] = (price_put[i] + price_call[i])*0.5

    # 计算sigma_1:近月波动率
    sigma_square = (F / k_0 - 1) ** 2 / T
    for i in range(1, c - 1):
        sigma_square += 2 / T * delta_k_i[i] * e ** (R * T) * price_k_i[i] / K_i[i] ** 2
    return sigma_square



def vix(trade_date, option_end_date_1,option_end_date_2,option_string):
    sigma_1=calculate_sigma(trade_date, option_end_date_1,option_string)
    sigma_2=calculate_sigma(trade_date, option_end_date_2, option_string)
    # 将日期的格式从数字转化为20xx-xx-xx
    d1 = datetime.datetime(trade_date // 10000, (trade_date % 10000) // 100, trade_date % 100)
    d2 = datetime.datetime(option_end_date_1 // 10000, (option_end_date_1 % 10000) // 100, option_end_date_1 % 100)
    d3 =datetime.datetime(option_end_date_2 // 10000, (option_end_date_2 % 10000) // 100, option_end_date_2 % 100)
    NT_1 = (d2 - d1).days
    NT_2=(d3 - d1).days
    T_1= NT_1/ 365
    T_2 =NT_2/ 365
    ivx=100*((T_1*sigma_1**2*(NT_2-30)/(NT_2-NT_1)+T_2*sigma_2**2*(30-NT_1)/(NT_2-NT_1))*365/30)**0.5
    return ivx



if __name__=='__main__':
    trade_date = 20150209
    option_end_date_1 = 20150325
    option_end_date_2 = 20150422
    option_string = 'OPTION_LOCAL_510050'
    R = 0.029
    vix=vix(trade_date,option_end_date_1,option_end_date_2,option_string)
    print(vix)









