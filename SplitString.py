# Coding Is Easy

# Manipulate Strings and Input and other things with strings

# Strings:
# * Trimming
# * Splitting
# * Joining
# * Replacements
# * Conversion to and from numbers etc

# City name, temperature, in words, country
weather_data = "London,16,cold,uk"
weather_data = "Dubai,49,extremely hot boiling even,UAE"

str_data = weather_data.split(",")
# print(str_data)

format = f"{str_data[0]}, today is {str_data[1]} degrees celcius. It's a bit {str_data[2]}"

print(format)