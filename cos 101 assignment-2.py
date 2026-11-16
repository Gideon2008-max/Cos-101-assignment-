def kinetic_energy():
    m = float(input("Enter mass (kg): "))
    v = float(input("Enter velocity (m/s): "))
    ke = 0.5 * m * v**2
    print(f"Kinetic Energy = {ke} Joules")


def potential_energy():
    m = float(input("Enter mass (kg): "))
    h = float(input("Enter height (m): "))
    g = 9.8
    pe = m * g * h
    print(f"Potential Energy = {pe} Joules")


def force():
    m = float(input("Enter mass (kg): "))
    a = float(input("Enter acceleration (m/s^2): "))
    f = m * a
    print(f"Force = {f} Newtons")


def pressure():
    f = float(input("Enter force (N): "))
    a = float(input("Enter area (m^2): "))
    p = f / a
    print(f"Pressure = {p} Pascals")


def power():
    w = float(input("Enter work done (J): "))
    t = float(input("Enter time (s): "))
    p = w / t
    print(f"Power = {p} Watts")


# Infinite while loop
while True:
    print("\n--- Physics Calculator ---")
    print("1. Kinetic Energy")
    print("2. Potential Energy")
    print("3. Force")
    print("4. Pressure")
    print("5. Power")

    choice = input("Choose (1-5): ")

    if choice == "1":
        kinetic_energy()
    elif choice == "2":
        potential_energy()
    elif choice == "3":
        force()
    elif choice == "4":
        pressure()
    elif choice == "5":
        power()
    else:
        print("Invalid choice, try again")

    again = input("Do you still want to run another operation? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
