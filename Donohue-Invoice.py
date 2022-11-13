#Programmed by Sarah Donohue
#10/22/22
#Donohue-Invoice.py
#this application calculates the total cost for one, three-credit class at Cstate
books = 52.99
lab_fees = 25.00
tuition = 157.93
credit_hours = 3
tuition_sum = tuition * credit_hours
total_tuition = books + lab_fees + tuition_sum
stars = '*' * 50 
breaks  = '-' * 50
address = '\t Columbus State Community College\n \t 550 East Spring Street\n \t Columbus, OH 43215'
thankyou = 'Thank you for being a Columbus State Student'


print(stars, '\n', address, '\n', breaks, '\n \t Product Name: \t Product Price', '\n \t Books \t \t $', 
      books, '\n \t Lab Fees \t $', lab_fees, '\n \t Tuition \t $', tuition_sum, '\n', breaks, '\n \t \t \t Total', '\n \t \t \t $', 
      total_tuition, '\n', breaks, '\n', thankyou, '\n', stars)
