# Description
# The program calculates the gross income for a movie show 
# based on a user inputs of sold adult and child tickets and 
# determines the amounts distributed to the theater and the movie distributor
# ---------------------------------------------

# This function will display the start of the project
def projectStart():
    print('-' * 50 + '\n')
    print('\tDistribution of revenues for a Movie Theatre')
    print('-' * 50 + '\n')

# This function will display the end of the project
def projectEnd():
    print('-' * 50 + '\n')
    print('End of Project')

# This function will return an integer input from the user
def getIntegerData(prompt):
    value = int(input(prompt))
    return value

# This function will return a float input from the user
def getFloatData(prompt):
    value = float(input(prompt))
    return value

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

def main(): 
    # Calls function to display the start of project
    projectStart()

    # Getting the name of the movie from user
    name_of_movie = getStringData('Enter the name of the movie: ')

    # Getting the number of adult tickets sold
    adult_tickets = getIntegerData('Enter the number of adult tickets sold: ')

    # Getting the number of child tickets sold
    child_tickets = getIntegerData('Enter the number of child tickets sold: ')

    # Calculating gross income
    adult_price = 20.00
    child_price = 10.00
    gross_income = (adult_tickets * adult_price) + (child_tickets * child_price)

    # Calculating distribution amounts to the movie distributor and the theater
    theater_percent = 0.4
    distributor_percent = 0.6
    theater_income = gross_income * theater_percent
    distributor_income = gross_income * distributor_percent

    # Displaying the results
    print(f'Name of movie: {name_of_movie}')
    print(f'Adult tickets sold: {adult_tickets}')
    print(f'Child tickets sold: {child_tickets}\n')
    print(f'Box office revenue: ${gross_income:.2f}')
    print(f'Movie distributor income: ${distributor_income:.2f}')
    print(f'Theater income: ${theater_income:.2f}\n')

    # Calls function to display the end of project
    projectEnd()
      
main() 


