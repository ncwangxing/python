#读取单个股票历史数据
import tushare as ts  
d = ts.get_tick_data('601318',date='2017-06-26')  
print (d)  
e = ts.get_hist_data('601318',start='2017-06-23',end='2017-06-26')  
print (e) 

#每5秒取一次股票数据，并在上证指数高于3100点，或601318低于49元时提醒。
import os  
import time  
import tushare as ts  
import pandas as pd  
  
def check(code, low, high):  
    df = ts.get_realtime_quotes(code)  
    e = df[['code','name','price','time']]  
    p = df[u'price']  
    print (e)   
    if float(p[0]) > low and float(p[0]) < high:  
        return True  
    else :  
        return False  
      
while True:  
    if check('sh', 3100, 10000) or check('601318',0,49):  
        #os.system('play bell.wav')  
        print ("检测报警！！！！")
        exit()  
    time.sleep(5) 
