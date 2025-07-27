import numpy as np
import matplotlib.pyplot as plt
# input (charge(coulombs), x position, y position)
epsilon = 1e-10  # small value to avoid division by zero

def process_charge_inputs():
    
    charges_list = []

    print("please give the values for the charge (charge(coulombs), x position, y position)")
    
    def create_charge():
        vals = []
        for label in ['Charges (C)', 'x', 'y']:
            try:
                value = float(input(f"{label}:    "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                return create_charge()
            
            vals.append(value)
        charge = tuple(vals)
            
        return charge
    charges_list.append(create_charge())
    
    
    
    response = input("Do you have more charges? y/n")
    
    while response == 'y': 
        charges_list.append(create_charge())
        response = input("Do you have more charges? y/n: ")
        if response.lower() == 'n':
            break
        elif response.lower() not in ['y', 'n']:
            print("Invalid input, please enter 'y' or 'n'.")
            response = input("Do you have more charges? y/n: ")
    return charges_list
        
        
def create_field_lines(charges_list): # input [(charge, x, y), ...]
    k = 1/(4*np.pi*8.85418782*(10**-12)) # constant

    charges = charges_list

    x = np.linspace(-8, 8, 150)
    y = np.linspace(-8, 8, 150)

    X, Y = np.meshgrid(x, y)

    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)

    for q, x0, y0 in charges:
        c_x = X - x0
        c_y = Y - y0

        r_squared = c_x**2 + c_y**2
        r = np.sqrt(r_squared)

        r_squared[r_squared == 0] = 1e-10
        r[r == 0] = epsilon

        Ex += q*(c_x)/(r_squared**1.5)
        Ey += q*(c_y)/(r_squared**1.5)

    E_mag = np.sqrt(Ex**2 + Ey**2)
    if np.any(E_mag == 0):
        E_mag[E_mag == 0] = epsilon
    Ex_hat = Ex/E_mag
    Ey_hat = Ey/E_mag



    plt.figure(figsize=(10, 10))
    plt.streamplot(X, Y, Ex, Ey, color=E_mag, cmap='cool', linewidth=1)
    plt.quiver(X, Y, Ex_hat, Ey_hat, color='gray', alpha=0.3)

    for q, x0, y0 in charges:
        if q>0: plt.plot(x0, y0, 'ro')
        else: plt.plot(x0, y0, 'bo')


    plt.title("Electric Fields of Charges")
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.axis('equal')
    plt.grid(True)
    plt.show()


charges = process_charge_inputs()
create_field_lines(charges)


