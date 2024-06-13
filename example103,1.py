import pandas as pd

def cal_co2(c):
    data = pd.read_csv('C:\\Users\\YOONES-NIA\\Desktop\\csv_files\\Car.csv', index_col='Car')
    data1=data.loc[[c]]
    s_co2=data1['CO2']
    l_co2=s_co2.tolist()
    t_co2=0
    for e in l_co2:
        t_co2+=e
    ave_co2=t_co2/len(l_co2)
    return ave_co2

if __name__=='__main__':
    data=pd.read_csv('C:\\Users\\YOONES-NIA\\Desktop\\csv_files\\Car.csv')
    s_car=data['Car']
    l_car=s_car.tolist()
    fl_car=set(l_car)

    file=open('C:\\Users\\YOONES-NIA\\PycharmProjects\\pythonProject4,1\\cars1_co2.txt','w')
    for c in fl_car:
        ave_co2=cal_co2(c)
        file.write(c+': '+str(ave_co2)+'\n')
        print(c,': ',ave_co2)
    file.close()






