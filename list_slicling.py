my_list = [2, 3, 4, 6, 77, 43, 33, -22]
print(my_list)
print(my_list[0:4]) #first 4
print(my_list[-3:]) #last 3

print(my_list[:4]) #first 4

#steps of 2
print(my_list[0:len(my_list):2])
print(my_list[-1::-1]) #Reversing the list order with a step of 1

sample_url = 'http://maniksoni.com'
#Reversing the string
print(sample_url[::-1])

#Get the top level domain of the string
print(sample_url[sample_url.index('.'):])

#Print the url without the http
print(sample_url[sample_url.index('/')+2:])

#Print without http and top level domain
print(sample_url[sample_url.index('/')+2: sample_url.index('.com')])