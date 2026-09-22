date = input("Enter the date in US format (MM/DD/YY): ")

month = date[0:2]
day = date[3:5]
year = date[6:8]

iso_date = "20" + year + "-" + month + "-" + day

print("The date in ISO 8601 extended format is:", iso_date)