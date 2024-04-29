# popular-man-names
Generate a popularity report of names in HTML form

It is a program in Python that will analyze data from a CSV file containing the most popular
male surnames in Poland as of 2024. The program on input receives the variable top, top_min:
top - x most popular names along with the number of occurrences
top_min - x least popular names along with the number of occurrences

The program is to generate a report in the form of an HTML file, which will contain:
1. a table with the top most popular names
2. a table with the top_min least popular names
3. a pie chart with the percentage of the top most popular names

* Extra:
The program saves the report as an HTML file to the results folder.
When calling the program from the command line, the user can specify the top and top_min values.
If the report has already been generated before for the given input data, the program 
should return the appropriate message and not generate the report again.

** Extra 
The force_calc parameter to the script, which will take two values False (default) and True.
If force_calc=True then the program always generates a report, if force_calc=False then the program
checks if the report has already been generated and prints an appropriate message.
