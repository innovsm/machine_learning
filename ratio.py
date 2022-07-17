from resources import  *
list_company = ["BAJAJAUTO"] # enter the list of companies here
list_1 = [url_maker(i) for i in list_company]   # enter the list of companies here
x1 = raw_data(list_1)
counter = 0
for data in x1:
    
    enter_data(ratio(data),"stats/"+list_company[counter])
    counter += 1
    print("hello world")