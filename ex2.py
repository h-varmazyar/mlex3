import matplotlib.pyplot as plt
from collections import defaultdict
data_dict = {}


def create_data_dictionary(data):
    for key, value in data:
        lab_name = key[0]
        lab_num = key[1:]
        sample_count = value

        if lab_name not in data_dict:
            data_dict[lab_name] = defaultdict(int)

        data_dict[lab_name][lab_num] = int(sample_count)


def add_sample(region, labNum, sample_count):
    data_dict[region][labNum] += sample_count


def remove_sample(region, labNum, sample_count):
    data_dict[region][labNum] -= sample_count


def add_lab(region):
    last_lab = 0
    for lab in data_dict[region]:
        if lab > last_lab:
            last_lab = lab

    data_dict[region][last_lab] = 0


def sample_count_bar_chart():
    lab_labels = []
    lab_sample_count = []
    for region in data_dict:
        for name in data_dict[region]:
            lab_labels.append("{}{}".format(region, name))
            lab_sample_count.append(data_dict[region][name])

    plt.bar(lab_labels, lab_sample_count)
    plt.show()


def sample_avg_per_region_bar_chart():
    region_labels = []
    avg_sample_count = []
    for region in data_dict:
        region_labels.append(region)
        count = 0
        summation = 0
        for name in data_dict[region]:
            summation += data_dict[region][name]
            count += 1
        avg = summation / count
        avg_sample_count.append(avg)

    plt.bar(region_labels, avg_sample_count)
    plt.show()


if __name__ == '__main__':
    data_str = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0], ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19], ['B1', 145],
                ['B2', 27], ['B3', 36], ['B4', 25], ['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12], ['C1', 122],
                ['C2', 87], ['C3', 36], ['C4', 3], ['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62], ['D5', 98], ['D6', 32]]

    data_list = [list(map(str, i)) for i in data_str]

    create_data_dictionary(data_list)

    sumOfLabs = 0
    sumOfSamples = 0
    for region in data_dict:
        for name in data_dict[region]:
            sumOfLabs += 1
            sumOfSamples += data_dict[region][name]

    print("Total count of labs: ", sumOfLabs)
    print("Total count of samples: ", sumOfSamples)

    sample_count_bar_chart()
    sample_avg_per_region_bar_chart()

    add_sample("A", 1, 2)
    add_lab("A")
