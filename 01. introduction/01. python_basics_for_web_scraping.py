# ==== python basics for web scraping ====

# imports go a the top of the file
import pandas as pd

# == list ==
states = ['California', 'Texas', 'Florida', 'New York']
population = [39613493, 29730311, 21944577, 19299981]

# == dictionary ==
dict_states = {'States': states, 'Population': population}


# == calling and printing a list item by its index ==
# print(states[0])
# print(states[3])
# print(states[-1])
# print(states[-4])


# == for loops and if statements ==
# for state in states:
#     if state == 'Florida':
#         print(state)
#     print(state)


# == working with and exporting data in python ==

# 1. (with open as pattern)
# with open('filename', 'mode') as file:
#     file.write('Data successfully scraped!')


# = mode =
# w (write) - deletes the existing file content, creating the file if it doesn't already exist, and then allows you to write to the file

# = this creates the file =
# with open('test.txt', 'w') as file:
#     file.write('Data successfully scraped!')

# = this crates the file in the current working directory =


# 2. (data frame with Pandas library)
df_states = pd.DataFrame.from_dict(dict_states)
# print(df_states)

# the output has the format of an excel spreadsheet

# = to export the data frame to a csv file =
# df_states.to_csv('states.csv')

# = to not export the index to the file =
# df_states.to_csv('states_2.csv', index=False)

# = these crates the file in the current working directory =


# == handling exception errors ==
# for this we will use the try-except statement

# we will use this list to create an error
new_list = [2, 4, 6, 'California']

for element in new_list:
    try:
        print(element/2)
    except:
        print('The element is not a number!')


# == while break statement ==
# this is part of a work around when there are some limitation to the web scraping tool we are using
# when a web scraping tool lacks some functionality you have two options.
# 1. learn how to use another scraping tool
# 2. or you can find a work around
# an example would be pagination (scrapy can do it, but beautifulsoup and selenium will need a work around)

# while-break
# while <expression>:
#     <statement>

n = 4
while n > 0:
    print(n)
    n -= 1

print('message')

z = 4
while z > 0:
    print(z)
    z -= 1
    if z == 2:
        break

print('loop ended')
