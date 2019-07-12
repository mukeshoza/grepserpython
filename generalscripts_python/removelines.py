removelines = ['amazon']

with open('C:\myfiles\QA\projectfiles\\vericred_project\\201907110929-amazon_uk_listings_2019-07-09.csv\\201907110929-amazon_uk_listings_2019-07.csv',
          buffering=90000000, encoding='latin') as oldfile, \
        open('C:\myfiles\QA\projectfiles\\vericred_project\\201907110929-amazon_uk_listings_2019-07-09.csv\\201907110929-amazon_uk_listings_2019-07_new.csv', 'w',
             buffering=90000000, encoding='latin') as newfile:
    for line in oldfile:
        if not any(wordline in line for wordline in removelines):
            newfile.write(line)