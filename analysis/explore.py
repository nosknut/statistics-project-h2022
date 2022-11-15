import os
import csv
import numpy
import matplotlib.pyplot as plt

data = []

def load_file(file_path):
    global data
    data = numpy.genfromtxt(file_path, delimiter=', ', skip_header=1)

def scatter_timelapse():
    for time, value in data:
        plt.plot(time, value, 'ro')
        plt.pause(0.000001)
    
def line_plot():
    plt.ylim([1920, 1860])
    plt.plot(data[:,0], data[:,1])

def generate_graphs():
    os.makedirs("plots", exist_ok=True)
    for file in os.listdir('output'):
        load_file("output/"+file)
        line_plot()
        plt.savefig('plots/' + os.path.splitext(file)[0] + '.png')
        plt.clf()

def generate_statistics():
    statistics = []
    for file in os.listdir('output'):
        load_file("output/" + file)
        values = data[:,1]
        statistics.append({
            "file": file.strip(),
            "std": values.std(),
            "mean": values.mean(),
        })

    os.makedirs("plots", exist_ok=True)
    with open("plots/statistics.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=statistics[0].keys())
        writer.writeheader()
        writer.writerows(statistics)
        
generate_graphs()
generate_statistics()