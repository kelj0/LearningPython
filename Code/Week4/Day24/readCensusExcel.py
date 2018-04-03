# readCensusExcel.oy -Tabulates population and nuber of census trats for each country

import openpyxl , pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('D:\\--python\\Bookmaterials\\censuspopdata.xlsx')

sheet = wb.worksheets[0]
countryData = {}

print('Reading rows...')
for row in range(2,sheet.max_row+1):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value
    countryData.setdefault(state,{})
    countryData[state].setdefault(county,{'tracts':0,'pop':0})
    countryData[state][county]['tracts']+=1
    countryData[state][county]['pop']+= int(pop)
print('Writing results...')
resultFile = open('census2010.py','w')
resultFile.write('allData = '+pprint.pformat(countryData))
resultFile.close()
print('Done.')

wb.close()