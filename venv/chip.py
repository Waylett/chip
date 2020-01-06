import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

df = pd.read_csv(url, '\t')
chip = df

def describe():
    print(chip.info())

# will print the number of columns
def column_num():
    print(chip.shape[1])

# will print name of columns
def column_names():
    for col in chip.columns:
        print(col)

# will print index of dataframe
def col_index():
    print(chip.index)

# will print most featured item name
def most_ordered_item():
    print(chip.item_name.mode())

# will print number of times the items have been ordered
def num_of_chicken_bowl():
    print(chip.item_name.value_counts())

# will print most ordered choice description
def most_ordered_choice_description():
    print(chip.choice_description.mode())

# will print number of times diet coke is ordered
def num_of_diet_coke():
    print(chip.choice_description.value_counts())

def dt_float():
    dollarise = lambda x: float(x[1:-1])
    chip.item_price = chip.item_price.apply(dollarise)


def print_item_data_type():
    print(chip.dtypes)

def revenue():
    revenue = (chip['quantity'] * chip['item_price']).sum()

    print('Revenue was: $' + str(np.round(revenue, 2)))


def order_total():
    orders = chip.order_id.value_counts().count()
    print(orders)

def average_revenue():
    chip['revenue'] = chip['quantity'] * chip['item_price']
    order_grouped = chip.groupby(by=['order_id']).sum()
    order_grouped.mean()['revenue']


def diff_items_sold():
    print(chip.item_name.value_counts().count())

dt_float()
revenue()
#order_total()
print(average_revenue())
diff_items_sold()
print_item_data_type()
