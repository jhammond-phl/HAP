import xlwt
import os
import shutil
import xlrd
import csv

HAPData = open(r'G:\A_STAFF\Jessica\Housing\HAP Dashboard\Jan-DecemberCombined_Test.csv')

newRenter = 0
newHomeowner = 0
preservedRenter = 0
preservedHomeowner = 0
newRenter_Homeless = 0
newRenter_0to29 = 0
newRenter_30to50 = 0
newRenter_50to80 = 0
newRenter_80to120 = 0
newRenter_120Up = 0
newHomeowner_Homeless = 0
newHomeowner_0to29 = 0
newHomeowner_30to50 = 0
newHomeowner_50to80 = 0
newHomeowner_80to120 = 0
newHomeowner_120Up = 0
preservedRenter_Homeless = 0
preservedRenter_0to29 = 0
preservedRenter_30to50 = 0
preservedRenter_50to80 = 0
preservedRenter_80to120 = 0
preservedRenter_120Up = 0
preservedHomeowner_Homeless = 0
preservedHomeowner_0to29 = 0
preservedHomeowner_30to50 = 0
preservedHomeowner_50to80 = 0
preservedHomeowner_80to120 = 0
preservedHomeowner_120Up = 0
errors = 0
rowCount = 0
programs = {}


reader = csv.reader(HAPData)
for row in reader:
    if rowCount == 0:
        rowCount = rowCount + 1
    else:
        print row
        units = row[7]
        unitCount = int(units)
        print unitCount
        tenure = row[0]
        status = row[1]
        ami = row[5]
        program = row[2]
        print "Units: ", unitCount
        print(type(unitCount))
        print "Tenure: ", tenure
        print(type(tenure))
        print "Status: ", status
        print(type(status))
        print "AMI: ", ami
        print(type(ami))
        if program in programs:
            programs[program] += unitCount
        else:
            programs[program] = unitCount
        if tenure == "Renter":
            if status == "Preservation":
                print "Renter Preservation"
                preservedRenter = preservedRenter + unitCount
                if ami == "Homeless":
                    print "Homeless"
                    preservedRenter_Homeless = preservedRenter_Homeless + unitCount
                elif ami == "<30%":
                    print "<30%"
                    preservedRenter_0to29 = preservedRenter_0to29 + unitCount
                elif ami == "30-50%":
                    print "30-50%"
                    preservedRenter_30to50 = preservedRenter_30to50 + unitCount
                elif ami == "50-80%":
                    print "50-80%"
                    preservedRenter_50to80 = preservedRenter_50to80 + unitCount
                elif ami == "80-120%":
                    print "80-120%"
                    preservedRenter_80to120 = preservedRenter_80to120 + unitCount
                elif ami == ">120%":
                    print ">120%"
                    preservedRenter_120Up = preservedRenter_120Up + unitCount
                else:
                    print "Something went wrong with Renter Preservation"
                    errors = errors + 1
            elif status == "New":
                print "Renter New"
                newRenter = newRenter + unitCount
                if ami == "Homeless":
                    print "Homeless"
                    newRenter_Homeless = newRenter_Homeless + unitCount
                elif ami == "<30%":
                    print "<30%"
                    newRenter_0to29 = newRenter_0to29 + unitCount
                elif ami == "30-50%":
                    print "30-50%"
                    newRenter_30to50 = newRenter_30to50 + unitCount
                elif ami == "50-80%":
                    print "50-80%"
                    newRenter_50to80 = newRenter_50to80 + unitCount
                elif ami == "80-120%":
                    print "80-120%"
                    newRenter_50to80 = newRenter_50to80 + unitCount
                elif ami == ">120%":
                    print ">120%"
                    newRenter_120Up = newRenter_120Up + unitCount
                else:
                    print "Something went wrong with Renter New"
                    errors = errors + 1
            else:
               print "Error with Renters"
        if tenure == "Homeowner":
            if status == "Preservation":
                print "Homeowner Preservation"
                preservedHomeowner = preservedHomeowner + unitCount
                if ami == "Homeless":
                    print "Homeless"
                    preservedHomeowner_Homeless = preservedHomeowner_Homeless + unitCount
                elif ami == "<30%":
                    print "<30%"
                    preservedHomeowner_0to29 = preservedHomeowner_0to29 + unitCount
                elif ami == "30-50%":
                    print "30-50%"
                    preservedHomeowner_30to50 = preservedHomeowner_30to50 + unitCount
                elif ami == "50-80%":
                    print "50-80%"
                    preservedHomeowner_50to80 = preservedHomeowner_50to80 + unitCount
                elif ami == "80-120%":
                    print "80-120%"
                    preservedHomeowner_80to120 = preservedHomeowner_80to120 + unitCount
                elif ami == ">120%":
                    print ">120%"
                    preservedHomeowner_120Up = preservedHomeowner_120Up + unitCount
                else:
                    print "Something went wrong"
                    errors = errors + 1
            elif status == "New":
                print "Homeowner New"
                newHomeowner = newHomeowner + unitCount
                if ami == "Homeless":
                    print "Homeless"
                    newHomeowner_Homeless = newHomeowner_Homeless + unitCount
                elif ami == "<30%":
                    print "<30%"
                    newHomeowner_0to29 = newHomeowner_0to29 + unitCount
                elif ami == "30-50%":
                    print "30-50%"
                    newHomeowner_30to50 = newHomeowner_30to50 + unitCount
                elif ami == "50-80%":
                    print "50-80%"
                    newHomeowner_50to80 = newHomeowner_50to80 + unitCount
                elif ami == "80-120%":
                    print "80-120%"
                    newHomeowner_80to120 = newHomeowner_80to120 + unitCount
                elif ami == ">120%":
                    print ">120%"
                    newHomeowner_120Up = newHomeowner_120Up + unitCount
                else:
                    print "Something went wrong"
                    errors = errors + 1
            else:
                print "Something went wrong with Homeowner"

print "newRenter", newRenter
print "newHomeowner", newHomeowner
print "preservedRenter", preservedRenter
print "preservedHomeowner", preservedHomeowner
print "newRenter_Homeless", newRenter_Homeless
print "newRenter_0to29", newRenter_0to29
print "newRenter_30to50", newRenter_30to50
print "newRenter_50to80", newRenter_50to80
print "newRenter_80to120", newRenter_80to120
print "newRenter_120Up", newRenter_120Up
print "newHomeowner_Homeless", newHomeowner_Homeless
print "newHomeowner_0to29", newHomeowner_0to29
print "newHomeowner_30to50", newHomeowner_30to50
print "newHomeowner_50to80", newHomeowner_50to80
print "newHomeowner_80to120", newHomeowner_80to120
print "newHomeowner_120", newHomeowner_120Up
print "preservedRenter_Homeless", preservedRenter_Homeless
print "preservedRenter_0to29", preservedRenter_0to29
print "preservedRenter_30to50", preservedRenter_30to50
print "preservedRenter_50to80", preservedRenter_50to80
print "preservedRenter_80to120", preservedRenter_80to120
print "preservedRenter_120up", preservedRenter_120Up
print "preservedHomeowner_Homeless", preservedHomeowner_Homeless
print "preservedHomeowner_0to29", preservedHomeowner_0to29
print "preservedHomeowner_30to50", preservedHomeowner_30to50
print "preservedHomeowner_50to80", preservedHomeowner_50to80
print "preservedHomeowner_80to120", preservedHomeowner_80to120
print "preservedHomeowner_120up", preservedHomeowner_120Up
print "errors", errors

Total_New = newRenter + newHomeowner
Total_Preserved = preservedRenter + preservedHomeowner
Total = newRenter + newHomeowner + preservedRenter + preservedHomeowner
Total_Homeless = newRenter_Homeless + newHomeowner_Homeless + preservedRenter_Homeless + preservedHomeowner_Homeless
Total_0to29 = newRenter_0to29 + newHomeowner_0to29 + preservedRenter_0to29 + preservedHomeowner_0to29
Total_30to50 = newRenter_30to50 + newHomeowner_30to50 + preservedRenter_30to50 + preservedHomeowner_30to50
Total_50to80 = newRenter_50to80 + newHomeowner_50to80 + preservedRenter_50to80 + preservedHomeowner_50to80
Total_80to120 = newRenter_80to120 + newHomeowner_80to120 + preservedRenter_80to120 + preservedHomeowner_80to120
Total_120up = newRenter_120Up + newHomeowner_120Up + preservedRenter_120Up + preservedHomeowner_120Up

with open('H:\HAP\writeData.csv', mode='wb') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Housing Type', 'AMI', 'Owner Preserved Units', 'Owner New Units', 'Renter Preserved Units', 'Renter New Units', '2019','Annual Goal','10 Year Goal'])
    writer.writerow(['Homeless','',str(preservedHomeowner_Homeless), str(newHomeowner_Homeless), str(preservedRenter_Homeless), str(newRenter_Homeless), str(Total_Homeless), '250', '2500'])
    writer.writerow(['Affordable','<30%', str(preservedHomeowner_0to29), str(newHomeowner_0to29), str(preservedRenter_0to29), str(newRenter_0to29), str(Total_0to29), '3940', '39400'])
    writer.writerow(['Affordable', '30-50%', str(preservedHomeowner_30to50), str(newHomeowner_30to50), str(preservedRenter_30to50), str(newRenter_30to50), str(Total_30to50), '1220', '12200'])
    writer.writerow(['Affordable', '50-80%', str(preservedHomeowner_50to80), str(newHomeowner_50to80), str(preservedRenter_50to80), str(newRenter_50to80), str(Total_50to80), '1940', '19400'])
    writer.writerow(['Workforce', '80-120%', str(preservedHomeowner_80to120), str(newHomeowner_80to120), str(preservedRenter_80to120), str(newRenter_80to120), str(Total_80to120), '1150', '11500'])
    writer.writerow(['Market-Rate', '>120%', str(preservedHomeowner_120Up), str(newHomeowner_120Up), str(preservedRenter_120Up), str(newRenter_120Up), str(Total_120up), '1500', '15000'])
    writer.writerow(['Total','', str(preservedHomeowner), str(newHomeowner), str(preservedRenter), str(newRenter), str(Total), '10000', '100000'])

with open('H:\HAP\programData.csv', mode='wb') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Programs","Units"])
    for xprogram in programs:
        writer.writerow([xprogram,programs[xprogram]])
