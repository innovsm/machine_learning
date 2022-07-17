
#important comments :
# ast.literal_eval(data)
from selenium import webdriver
# the ratio functions:-

def info(data_list):
    j = 0 # upper circular
    y1 = []
    for i in data_list:
        y = data_list[j].split('\n\u202a')
        
        
        y1.append(y)
        j += 1
              
    return y1

#----------------------------------------------------------------------------

def get_data(data):
    data_1 = []
    number_code = 1
    number = ""
    for i in data:
        if(i == "B"):
            number_code = 1000000000
        if(i == "M"):
            number_code = 10000000
        if ((i.isdigit() == True) or (i == ".")):
            data_1.append(i)

    for alfa in data_1:
        number += alfa
    if(number != ""):
        return (float(number)*number_code)

#----------------------------------------------------------------

def ratio(data):
    x = info(data)
    
    dict_11 = {}
    main_name = []
    for anshu in x:
        main_name.append(anshu[0])
        delta = []
        
        for himanshu in anshu:
            print(himanshu)
            
            alfa = get_data(himanshu)
            if(alfa != None):
                delta.append(alfa)
                
        
        dict_11[anshu[0]] = delta
        
            
    return dict_11
                
#------------------------------
def true_value(data):
    if "M" in data:
        if "−" in data:
            temp_data = data[1:9]
            list_1 = temp_data.split("M")
            return -(float(list_1[0])*10000000)
        else:
            
            temp_data = data[0:8]
            list_1= temp_data.split("M")
            return (float(list_1[0])*10000000)
    if "B" in data:
        if "−" in data:
            temp_data = data[1:6]
            list_1= temp_data.split("B")
            return -(float(list_1[0])*1000000000)
        else:
            temp_data = data[0:5]
            list_1= temp_data.split("B")
            return (float(list_1[0])*1000000000)
    
        
    else:
        return data


#------------------------------

def income_stat(alfa):               #alfa is list of list 
    main_dict = {}
    for i in info(alfa):
        gama  = i[0]
        data_temp = []
        print(i[0])
        temp_list = i
        temp_list.remove(temp_list[0])
        for data in temp_list:
            print(true_value(data))
            data_temp.append(true_value(data))
        main_dict[gama] = data_temp
    return main_dict

#----------------------------------------------------------------

def url_maker(company_name,signal_name = 0): # enter signal 1 for income-statement
    if(signal_name == 1):
        url_final = "https://in.tradingview.com/symbols/NSE-"+str(company_name)+"/financials-income-statement/"
        return url_final    
    else:
        url_final = "https://in.tradingview.com/symbols/NSE-"+str(company_name)+"/financials-statistics-and-ratios/"
        
        return url_final


#----------------------------------------------------------------
#------------------------------


def trimmer(dict_main):

    dict_final = dict_main
    del_keys = ['Equity in earnings','Discontinued operations','Preferred dividends','After tax other income/expense','Dilution adjustment','Basic earnings per share (Basic EPS)','Diluted earnings per share (Diluted EPS)']
    for i in del_keys:
        try:
            del dict_final[i]
        except:
            
            continue
    return dict_final


#---------------------------------------------------

def enter_data(data,company_name):
    if(True):
        data_input = open(str(company_name)+".txt",'a')
        data_input.write(str(data)+"\n")


#---------------------------------------------------

def raw_data(url_list):
    main_list = []

    for i in url_list:
        driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")
        driver.get(i)
        data_1 = []
        titles = driver.find_elements_by_class_name('container-jKD0Exn-')
        for t in titles:
            data_1.append(t.text)
            
       
        print(data_1)  
        main_list.append(data_1)
    return main_list

# user-friendly NSE_CODE SEARCH ENGINE
