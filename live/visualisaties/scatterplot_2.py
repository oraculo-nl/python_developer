# read Smartphone_Usage_Productivity_Dataset_50000.csv
import csv
import matplotlib.pyplot as plt


def read_csv_to_dict(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# Example usage:
dataset = read_csv_to_dict("../bestanden/Smartphone_Usage_Productivity_Dataset_50000.csv")


def extract_column_values(dataset, column_name, data_type=str):
    """
    Extract values from a specified column in the dataset.
    Filters rows where the value cannot be converted to the specified data type.
    """
    return [data_type(row[column_name]) for row in dataset if row[column_name].isdigit()]


ages = extract_column_values(dataset, "Age", int)

print(ages)
# Extract Age and Daily_Phone_Hours columns
daily_phone_hours = [float(row["Daily_Phone_Hours"]) for row in dataset if
                     row["Daily_Phone_Hours"].replace('.', '', 1).isdigit()]

print (daily_phone_hours)
# daily_phone_hours: List of float numbers representing the hours of daily phone usage extracted from the dataset.
#
# Create scatterplot
plt.scatter(ages[:10], daily_phone_hours[:10], alpha=0.5, label="Age vs. Daily Phone Hours")
plt.title("Scatterplot of Age vs. Daily Phone Hours")
plt.xlabel("Age")
plt.ylabel("Daily Phone Hours")
plt.legend()
plt.grid(True)
plt.show()
#
# # create a scatterplot of Age vs. Daily_Phone_Hours from the dataset
#
#
#

