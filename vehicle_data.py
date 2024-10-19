import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# # Read the log file
ev_data = pd.read_csv('C:/Users/Tafa/Desktop/Data/DataVehicles/Electric_Vehicle_Population_Data.csv')
#
# print(ev_data.head())
# ev_data.info()
# ev_data.isnull().sum()
#
# ev_data = ev_data.dropna()



# sns.set_style('whitegrid')
#
# plt.figure(figsize=(12, 6))
# ev_adoption_by_year = ev_data['Model Year'].value_counts().sort_index()
# sns.barplot(x=ev_adoption_by_year.index, y=ev_adoption_by_year.values, palette="viridis")
# plt.title('EV Adoption Over Time')
# plt.xlabel('Model Year')
# plt.ylabel('Number of Vehicles Registered')
# plt.xticks(rotation=45)
# plt.tight_layout()
# # plt.show()

# ev_county_distribution = ev_data['County'].value_counts()
# top_counties = ev_county_distribution.head(3).index
#
# # filtering the dataset for these top counties
# top_counties_data = ev_data[ev_data['County'].isin(top_counties)]
#
# # analyzing the distribution of EVs within the cities of these top counties
# ev_city_distribution_top_counties = top_counties_data.groupby(['County', 'City']).size().sort_values(ascending=False).reset_index(name='Number of Vehicles')
#
# # visualize the top 10 cities across these counties
# top_cities = ev_city_distribution_top_counties.head(10)
#
# plt.figure(figsize=(12, 8))
# sns.barplot(x='Number of Vehicles', y='City', hue='County', data=top_cities, palette="magma")
# plt.title('Top Cities in Top Counties by EV Registrations')
# plt.xlabel('Number of Vehicles Registered')
# plt.ylabel('City')
# plt.legend(title='County')
# plt.tight_layout()
# plt.show()

# ev_type_distribution = ev_data['Electric Vehicle Type'].value_counts()
#
# plt.figure(figsize=(10, 6))
# sns.barplot(x=ev_type_distribution.values, y=ev_type_distribution.index, palette="rocket")
# plt.title('Distribution of Electric Vehicle Types')
# plt.xlabel('Number of Vehicles Registered')
# plt.ylabel('Electric Vehicle Type')
# plt.tight_layout()
# plt.show()

## Analyze of distribution of electric range
# plt.figure(figsize=(12, 6))
# sns.histplot(ev_data['Electric Range'], bins=30, kde=True, color='royalblue')
# plt.title('Distribution of Electric Vehicle Ranges')
# plt.xlabel('Electric Range (miles)')
# plt.ylabel('Number of Vehicles')
# plt.axvline(ev_data['Electric Range'].mean(), color='red', linestyle='--', label=f'Mean Range: {ev_data["Electric Range"].mean():.2f} miles')
# plt.legend()
# plt.show()

# ev_registration_counts = ev_data['Model Year'].value_counts().sort_index()
# print(ev_registration_counts)



