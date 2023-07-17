import re
import urllib.request

# Open the URL
url = "http://py4e-data.dr-chuck.net/regex_sum_1777571.txt"
file = urllib.request.urlopen(url)

# Initialize the sum
sum = 0

# Loop through the lines of the file
for line in file:
    # Decode the line from bytes to string
    line = line.decode().rstrip()
    # Find all the numbers in the line using regular expression
    numbers = re.findall('[0-9]+', line)
    # Loop through the numbers and add them to the sum
    for number in numbers:
        sum += int(number)

# Close the file
file.close()

# Print the sum
print("Sum of all numbers in the file:", sum)
