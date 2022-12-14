import os
import csv
import numpy
import matplotlib.pyplot as plt

data = []

def load_file(file_path):
    global data
    data = numpy.genfromtxt(file_path, delimiter=', ', skip_header=1)

def scatter_timelapse():
    for time, value, value2 in data:
        plt.plot(time, value, 'ro')
        plt.pause(0.000001)
    
def line_plot(column):
    plt.plot(data[:,0], data[:,column])

def generate_graphs():
    os.makedirs("plots", exist_ok=True)
    for file in os.listdir('output'):
        load_file("output/"+file)
        line_plot(1)
        plt.savefig('plots/' + os.path.splitext(file)[0] + '_value.png')
        plt.clf()
        line_plot(2)
        plt.savefig('plots/' + os.path.splitext(file)[0] + '_value2.png')
        plt.clf()

def generate_statistics():
    statistics = []
    for file in os.listdir('output'):
        load_file("output/" + file)
        values = data[:,1]
        statistics.append({
            "file": file.strip() + "_value",
            "std": values.std(),
            "mean": values.mean(),
            "median": numpy.median(values),
        })

        values2 = data[:,2]
        statistics.append({
            "file": file.strip() + "_value2",
            "std": values2.std(),
            "mean": values2.mean(),
            "median": numpy.median(values2),
        })
        
    os.makedirs("plots", exist_ok=True)
    with open("plots/statistics.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=statistics[0].keys())
        writer.writeheader()
        writer.writerows(statistics)
        
def find_bad_regions():
    global data
    load_file("output/"+"transistor_reverse_5.csv")
    data = data[:200000]
    plt.figure(0)
    line_plot(1)
    plt.figure(1)
    line_plot(2)
    plt.show()

generate_graphs()
generate_statistics()

def analyze_large_dataset():
    load_file("output/"+"all_2.csv")

    def cut_in_half(array):
        return array[len(array)//4:]

    timestamps = (cut_in_half(data[:,0]))

    zero_element = timestamps.argmin()
    numpy.delete(timestamps, zero_element)

    value1 = (cut_in_half(data[:,1]))
    value1 = numpy.delete(value1, zero_element)

    value2 = (cut_in_half(data[:,2]))
    value2 = 4095 - value2
    value2 = numpy.delete(value2, zero_element)

    print(value1.std(), value1.mean())
    print(value2.std(), value2.mean())

    plt.figure(0)
    plt.plot(timestamps, value1)
    plt.figure(1)
    plt.plot(timestamps, value2)
    plt.show()