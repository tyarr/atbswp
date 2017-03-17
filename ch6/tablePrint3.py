tableData = [['apples', 'oranges', 'cherries', 'bannana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# define function & parameter
def table_printer(args):
    # zips list | *args unpacks the list into positional argument
    for data in zip(*args):
        # template is a function that has been aligned inside field 10 chars in length
        template = '{:>10}'*len(data)
        # template is a string that has a string function of format to format the unpacked * data
        print(template.format(*data))

table_printer(tableData)