from rich.console import Console
from rich.table import Table

flights = {}
 
num_entries = int(input("Enter the number of flights you would like to add: "))
 
x = 1
for i in range(num_entries):
    key1 = "startingPoint" + str(x)
    value1 = input("Enter number for starting point: ")
    flights[key1] = value1

    key2 = "stoppingPoint" + str(x)
    value2 = input("Enter number for stopping point: ")

    if (value1 == value2):
        z = True
        while (z):
            value2 = input("Please input a different stopping than starting point: ")
            if (value1 == value2):
                z = True
            else:
                z = False
        

    flights[key2] = value2

    key3 = "price" + str(x)
    value3 = input("Enter the cost of the flight: ")
    flights[key3] = value3

    x += 1
 
print("Flight list after adding user input:", flights)

console = Console()

table = Table(title="Flights")
table.add_column("Starting point", style="yellow", justify="center")
table.add_column("Ending point", style="magenta", justify="center")
table.add_column("Price(USD)", style="green", justify="right")


y = 1
while (y) <= num_entries:
    table.add_row(
        str(flights["startingPoint" + str(y)]),
        str(flights["stoppingPoint" + str(y)]),
        str(flights["price" + str(y)]) + " USD"
    )
    y += 1


console.print(table)
