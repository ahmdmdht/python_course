from car import Car
from employee import Employee
from office import Office


samy_car = Car(name="Fiat 128", fuelRate=70, velocity=100)

# Create Samy the employee
samy = Employee(
    name="Samy",
    money=5000,
    healthRate=80,
    mood="happy",
    id=1,
    car=samy_car,
    salary=7000,
    distanceToWork=30,
    email="samy@iti.org"
)

# Create ITI office and hire Samy
iti_office = Office("ITI Smart Village")
iti_office.hire(samy)
iti_office.calculate_lateness(arrival_time=10)
# Simulate a week
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days:
    print(f"\n** {day} ***")
    if day in ["Saturday", "Sunday"]:
        print("It's the weekend. Samy stays at home.")
    else:
        print("Samy is going to work.")
        samy.drive(samy.distanceToWork)
        samy.work(8)
lateness=iti_office.calculate_lateness(arrival_time=10)
print(f"Sami arrived   {lateness} hour late   ")