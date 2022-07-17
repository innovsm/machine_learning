from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from resources import income_stat,trimmer,url_maker


def enter_data(data,company_name):
    if(True):
        data_input = open(str(company_name)+".txt",'a')
        data_input.write(str(data)+"\n")
 







true_keys = ['Gross profit', 'Total revenue', 'Cost of goods sold', 'Operating expenses (excl. COGS)', 'Operating income', 'Non-operating income, total', 'Pretax income', 'Equity in earnings', 'Taxes', 'Non-controlling/minority interest', 'After tax other income/expense', 'Net income before discontinued operations', 'Discontinued operations', 'Net income', 'Dilution adjustment', 'Preferred dividends', 'Diluted net income available to common stockholders', 'Basic earnings per share (Basic EPS)', 'Diluted earnings per share (Diluted EPS)', 'Average basic shares outstanding', 'Diluted shares outstanding', 'EBITDA', 'EBIT', 'Total operating expenses']


def raw_data(url_list):
    main_list = []

    for i in url_list:
        driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")
        driver.get(i)
        data_1 = []
        titles = driver.find_elements_by_class_name('value-1WwaU3uo') #
     
        for t in titles:
            data_1.append(t.text)
            
       
        print(data_1)  
        main_list.append(data_1)
    #print(main_list)
    
    return main_list





# ========================= main_area =======================================

#list of companies here
company_list = ["RELIANCE"]
x1 = raw_data([url_maker(i,1) for i in company_list])   # change company here

data_1 = []
for i in x1:
    x_11 = income_stat(i)
    data_1.append(x_11)
    
print(data_1)

    

#print(data_1[0])  #  """here all the income indiactors will be added to the income.txt"""


# entering the values in the register
counter= 0
for income in data_1:
    values = income.values()
    print(values)
    dict_final = dict(zip(true_keys,values))
    enter_data(trimmer(dict_final),"income_statments/"+company_list[counter])
    counter += 1
    

