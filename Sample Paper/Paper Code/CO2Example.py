import csv                                    # Import the necessary library to work with csv files
import matplotlib.pyplot as plt                # Import the necessary library to plot results

data_entries = {'Heat Content':[],
                'Mauna Loa':[],
                'CO2 Dates':[],
                'South Pole':[],
                'Heat Content Dates':[],
                '+2 Standard Error':[],
                '-2 Standard Error':[],
                'Temperature Anomaly':[],
                'Temperature Dates':[],
                'trace6':[],
                'trace7':[],
                'trace8':[],
                'trace9':[],
                'trace10':[]}

data_file_name = './Data/CO2Data.csv'
with open(data_file_name, 'rb') as f:
    reader = csv.DictReader (f)
    for line in reader:
        for item in line:
            if 'Dates' not in item:
                if line[item]:
                    data_entries[item].append(float(line[item]))
            else:
                if line[item]:
                    data_entries[item].append(line[item])
                    #data_entries[item].append(int(line[item][0:4]))


get_ipython().magic(u'matplotlib inline')
plt.rcParams['figure.figsize'] = (16.0, 10.0)


years = []
for item in data_entries['Heat Content Dates']:
    years.append(int(item[0:4]))


fig = plt.figure()
fig.suptitle('Global Ocean Heat Content', fontsize=20)
#plt.xlabel('Year', fontsize=18)
plt.ylabel('Heat Content ($10^{22}$J)', fontsize=16)

plt.plot(years,data_entries['Heat Content'],linewidth=2)
plt.show()
fig.savefig('./Results/HeatContent_vs_Year.png')


co2_years = []
for item in data_entries['CO2 Dates']:
    co2_years.append(int(item[0:4]))

fig = plt.figure()
fig.suptitle('Global Ocean Heat Content', fontsize=20)
#plt.xlabel('Year', fontsize=18)
plt.ylabel('$CO_2$ (ppm)', fontsize=16)

plt.plot(co2_years,data_entries['South Pole'],linewidth=2,label='South Pole')
plt.plot(co2_years,data_entries['Mauna Loa'],linewidth=2,color='r',label='Mauna Loa')
plt.legend(loc='upper left')
plt.show()
fig.savefig('./Results/CO2_vs_Year.png')
