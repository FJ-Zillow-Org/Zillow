clist = []
labels = []

for county in train.county_name.unique():
    clist.append(train[train.county_name == county].logerror)
    labels.append(county)

plt.hist(clist, color=['orange', 'dodgerblue', 'green'], label=labels)
plt.legend()
plt.show()
