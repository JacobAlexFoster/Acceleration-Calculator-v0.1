print("Which two parts of the equation do you know?")
print("Acceleration = A")
print("Initial Velocity = Vi")
print("Final Velocity = Vf")
print("Time = t")

x = input("First known variable (A/Vi/Vf/t): ").strip().upper()
y = input("Second known variable (A/Vi/Vf/t): ").strip().upper()

if x == "VI" and y == "VF":
    Vi = float(input("Initial Velocity (m/s): "))
    Vf = float(input("Final Velocity (m/s): "))
    t = float(input("Time (s): "))
    A = (Vf - Vi) / t
    print(f"Acceleration (A): {A:.2f} m/s²")

elif x == "A" and y == "T":
    A = float(input("Acceleration (m/s²): "))
    t = float(input("Time (s): "))
    Vi = float(input("Initial Velocity (m/s): "))
    Vf = Vi + (A * t)
    print(f"Final Velocity (Vf): {Vf:.2f} m/s")

elif x == "A" and y == "VI":
    A = float(input("Acceleration (m/s²): "))
    Vi = float(input("Initial Velocity (m/s): "))
    t = float(input("Time (s): "))
    Vf = Vi + (A * t)
    print(f"Final Velocity (Vf): {Vf:.2f} m/s")

elif x == "A" and y == "VF":
    A = float(input("Acceleration (m/s²): "))
    Vf = float(input("Final Velocity (m/s): "))
    t = float(input("Time (s): "))
    Vi = Vf - (A * t)
    print(f"Initial Velocity (Vi): {Vi:.2f} m/s")

elif x == "VF" and y == "T":
    Vf = float(input("Final Velocity (m/s): "))
    t = float(input("Time (s): "))
    Vi = float(input("Initial Velocity (m/s): "))
    A = (Vf - Vi) / t
    print(f"Acceleration (A): {A:.2f} m/s²")

elif x == "VI" and y == "T":
    Vi = float(input("Initial Velocity (m/s): "))
    t = float(input("Time (s): "))
    Vf = float(input("Final Velocity (m/s): "))
    A = (Vf - Vi) / t
    print(f"Acceleration (A): {A:.2f} m/s²")

else:
    print("Invalid input. Please enter A, Vi, Vf, or t.")