"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""
def print_sales_report(sales_report):
    """Print salesperson's name and the number of melons they sold.
    """

    salespeople_melons_sold = {}

    filename = open(sales_report)

    for line in filename:
        line = line.rstrip()
        entries = line.split("|")
        salesperson = entries[0]
        melons = int(entries[2])

        # If salesperson not in dictionary, then default the melon value to 0. If salesperson in
        # dictionary then update the melon value with the number of melons the salesperson sold.
        salespeople_melons_sold[salesperson] = salespeople_melons_sold.get(salesperson, 0) + melons

    for salesperson_name, melon_count in salespeople_melons_sold.items():
        print "{} sold {:,} melons.".format(salesperson_name, melon_count)

    filename.close()

print_sales_report("sales-report.txt")
