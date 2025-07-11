import openpyxl
import csv

# Load the Excel file
wb = openpyxl.load_workbook('E-mails.xlsx')

# Select the active sheet or by name
sheet = wb.active  # or wb['Sheet1']

# Open a CSV file to write
with open('E-mails.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # Loop through Excel rows and write to CSV
    for row in sheet.iter_rows(values_only=True):
        writer.writerow(row)

# Open the CSV file in read mode
file = open("E-mails.csv", "r", newline="")
# Create a CSV reader object
reader = csv.reader(file)
# Read and print each row
data = list(reader)
#create an empty list to append only emails in it
emails=[]
for i in range(1,len(data)):
    emails.append(data[i][3])
    
# using map i just clean emails from any spaces
cleaned_emails=list(map(str.strip,emails))

#create function that split emails to domains from("@")
def split_fun():
    # i made it global to re-use it in main file
  global domainCollector
  domainCollector=list(map(lambda x:x.split("@")[1],cleaned_emails))
  
split_fun()
print(f"number of domains before removing the redunduncy domains is : {len(domainCollector)}")
# tranform the list into set to remove any repeating domains
myset_email=set(domainCollector)
print(myset_email)
print(f"number of domains after removing the redunduncy domains is : {len(myset_email)}")
