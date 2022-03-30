from calendar import calendar, monthcalendar


def return_10 ():
    return 10

def  add (first_number, second_number):
    return (first_number + second_number)
    
def  subtract (first_number, second_number):
    return (first_number - second_number)

def  multiply (first_number, second_number):
    return (first_number * second_number)

def  divide (first_number, second_number):
    return (first_number / second_number)

def  length_of_string (self):
    return len("A string of length 21")

def join_string (string_1, string_2):
    return (string_1 + string_2)

def  add_string_as_number (word_1, word_2):
    return int(word_1) + int(word_2)



def number_to_full_month_name (months_number):
    months = {1 : "January", 
2 : "February", 
 3 : "March", 
4 : "April" , 
5 : "May" , 
6 : "June", 
 7 : "July", 
8 : "August" , 
 9 : "September", 
10 : "October" , 
 11 : "November",
 12 : "December" 
} 

    return months[months_number]



def number_to_short_month_name(months_number):
    short_months = {1 : "Jan", 
2 : "Feb", 
 3 : "March", 
4 : "Apr" , 
5 : "May" , 
6 : "Jun", 
 7 : "Jul", 
8 : "Aug" , 
 9 : "Sep", 
10 : "Oct" , 
 11 : "Nov",
 12 : "Dec"}

    return short_months[months_number]


# def  test_volume_of_cube (first_number):
#     return (first_number **2)

  #Given the length of a side of a cube calculate the volume
  
def get_cube_volume(cube_length):
    return cube_length **2

def back_wards (word):
    return word[::-1]

def f_to_c (temp):
    return (temp - 32) * 5/9




    
    
    