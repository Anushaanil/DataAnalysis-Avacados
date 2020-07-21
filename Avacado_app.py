import pandas as pd

def filter_year(df,year):
    return df.query("year == @year").drop(columns='year')


def average_per_year(df):
    average = {}
    years = df.year.unique()
    for year in years:
        average_obtained = filter_year(df,year).groupby("region").mean()
        average.update({year:average_obtained})
    return average


def min_max_values(df,returntype):
    dmax = dmin = []
    if returntype =='max':
        for year,data in df.items():
            maximum = data.Price.max()
            location = data.query("Price == @maximum").index[0]
            highest = {'Year': year, 'Max_price in($)': maximum, 'Location': location}
            dmax +=[highest]
        return dmax
    elif returntype == 'min':
        for year, data in df.items():
            minimum = data.Price.min()
            location = data.query("Price == @minimum").index[0]
            Lowest = {'Year': year, 'Min_price in($)': minimum, 'Location': location}
            dmin += [Lowest]
        return dmin


#print(f"Highest {item_type} Avacados were grown and sold in the year ({year}) at {location} for ${maximum:.2f}")
#print(f"Lowest  Avacados were grown and sold in the year ({year}) at {location} for ${minimum:.2f}")

with open("avacados.csv","r") as aprices:
    df = pd.read_csv(aprices)
df = df[["year","AveragePrice","type","region"]]
df.rename(columns={"AveragePrice":"Price","type":"Avacadotype"},inplace=True)

conventional = df.query("Avacadotype=='conventional'").copy()
conventional.drop(columns='Avacadotype',inplace=True)

organic = df.query("Avacadotype=='organic'").copy()
organic.drop(columns='Avacadotype',inplace=True)

con_max_df = pd.DataFrame(min_max_values(average_per_year(conventional),"max"))
con_min_df = pd.DataFrame(min_max_values(average_per_year(conventional),"min"))
print(f"Year-wise Highest & Lowest Prices on conventional Avacados:\n{con_max_df}\n\n{con_min_df}")

org_max_df = pd.DataFrame(min_max_values(average_per_year(organic),"max"))
org_min_df = pd.DataFrame(min_max_values(average_per_year(organic),"min"))
print()
print(f"Year-wise Highest & Lowest Prices on organic Avacados:\n{org_max_df}\n\n{org_min_df}")

#if anything else except min,max passed  then func returns empty dataframe
#min_max_values(average_per_year(organic),"organic")

print()
print("Total Result on Both types of Avacados")
highest_price = conventional.Price.max()
print(f"Highest price - conventional Avacados - ${highest_price}")
lowest_price = conventional.Price.min()
print(f"Lowest price - conventional Avacados - ${lowest_price}")
print()
highest_price = organic.Price.max()
print(f"Highest price - organic Avacados - ${highest_price}")
lowest_price = organic.Price.min()
print(f"Lowest price - organic Avacados - ${lowest_price}")

#print(filter_year(conventional,2018))
#print(average_per_year(conventional))
