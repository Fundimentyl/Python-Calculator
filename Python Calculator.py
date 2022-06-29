import math
def calculator():
    inp_types = "Input types:"
    types_math_set = "A: Sin\nB: Cos\nC: Tan\nD: Addition\nE: Subtraction\nF: Division\nG: Multiplication\nH: Exponentation\nI: Area of Square/Rectangle\nJ: Area of Triangle\nK: Area of Cylinder\nL: Area of Cube\nM: Area of Circle\nN: Pythagoras Hypotenuse (c)\nO: Pythagoreas Leg (a)\nP: Pythagoras Leg (b)"
    math_set_choice = "Enter the indexed input method you prefer from the set above\n"

    pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

    num_inp = "Enter your number\n"
    num_inp2 = "Enter another number\n"
    exp_inp = "Enter the number\n"
    exp_pwr_inp = "Enter the power\n"
    geo_side1 = "Enter the length of the side(s)\n"
    geo_side2 = "Enter the length of the other side\n"
    geo_base1 = "Enter the base\n"
    geo_height1 = "Enter the height\n"
    geo_rad = "Enter the radius\n"
    geo_edge = "Enter the edge\n"
    pythag_a = "Enter the value of a\n"
    pythag_b = "Enter the value of b\n"
    pythag_c = "Enter the value of c\n"

    print(inp_types)
    print(types_math_set)

    math_set_type_choice = input(math_set_choice)
    #End of variables
    try: # Tries all the code below for any errors
         # example: "so we can check for errors, we could TRY the code for any, and make exceptions to prevent the error from showing up."
        if math_set_type_choice == "A": # Trigonometry: Sin
            print("sin()")
            sin_calc = int(input(num_inp))
            print(f"sin({sin_calc}) = {math.sin(sin_calc)}")
        if math_set_type_choice == "B": # Trigonometry: Cos
            print("cos()")
            cos_calc = int(input(num_inp))
            print(f"cos({cos_calc}) = {math.cos(cos_calc)}")
        if math_set_type_choice == "C": # Trigonometry: Tan
            print("tan()")
            tan_calc = int(input(num_inp))
            print(f"tan({tan_calc}) = {math.tan(tan_calc)}")
        if math_set_type_choice == "D": # Addition
            print("# + #")
            add_num = int(input(num_inp))
            add_num2 = int(input(num_inp2))
            add_calc = f"{add_num} + {add_num2} = {add_num + add_num2}"
            print(add_calc)
        if math_set_type_choice == "E": # Subtraction
            print('# - #')
            sub_num = int(input(num_inp))
            sub_num2 = int(input(num_inp2))
            sub_calc = f"{sub_num} - {sub_num2} = {sub_num - sub_num2}"
            print(sub_calc)
        try:
            if math_set_type_choice == "F": # Division
                print("# / #")
                div_num = int(input(num_inp))
                div_num2 = int(input(num_inp2))
                div_calc = f"{div_num} / {div_num2} = {div_num / div_num2}"
                print(div_calc)
        except ZeroDivisionError:
            print("Cannot divide any number by zero. Please re-run code and enter correct values.")
        if math_set_type_choice == "G": # Multiplication
            print("# * #")
            mul_num = int(input(num_inp))
            mul_num2 = int(input(num_inp2))
            mul_calc = f"{mul_num} * {mul_num2} = {mul_num * mul_num2}"
            print(mul_calc)
        if math_set_type_choice == "H": # Exponentation
            print("#^#")
            exp_num = int(input(exp_inp))
            exp_pwr = int(input(exp_pwr_inp))
            exp_calc = f"{exp_num}^{exp_pwr} = {exp_num ** exp_pwr}"
            print(exp_calc)
        if math_set_type_choice == "I": # Area of Square
            print("Area of Square")
            sidelen = int(input(geo_side1))
            sidelen2 = int(input(geo_side2))
            print(f"The area of the square is {sidelen * sidelen2}")
        if math_set_type_choice == "J": # Area of Triangle
            print("Area of Triangle")
            heighttri = int(input(geo_height1))
            basetri = int(input(geo_base1))
            print(f"The area of the triangle is {(heighttri * basetri) / 2}")
        if math_set_type_choice == "K": # Area of Cylinder
            print("Area of Cylinder")
            radiuscyl = int(input(geo_rad))
            heightcyl = int(input(geo_height1))
            print(f"The area of the cylinder is ≈{2 * pi * radiuscyl * heightcyl + 2 * pi * radiuscyl**2}")
        if math_set_type_choice == "L": # Area of Cube
            print("Area of Cube")
            edgecube = int(input(geo_edge))
            print(f"The area of the cube is ≈{6 * edgecube**2}")
        if math_set_type_choice == "M": # Area of Circle
            print("Area of Circle")
            radcir = int(input(geo_rad))
            print(f"The area of the circle is ≈{pi * radcir**2}")
        if math_set_type_choice == "N": # Pythagoras Hypotenuse c = a + b
            print("Pythagoreas Hypotenuse")
            ac = int(input(pythag_a))
            bc = int(input(pythag_b))
            print(f"The hypotenuse is ≈{math.sqrt(ac**2 + bc**2)}")
        if math_set_type_choice == "O": # Pythagoras Leg (a)
            print("Pythagoras Leg (a)")
            ba = int(input(pythag_b))
            ca = int(input(pythag_c))
            print(f"The leg is ≈{math.sqrt(ca**2 - ba**2)}")
        if math_set_type_choice == "P": # Pythagoras Leg (b)
            print("Pythagoras Leg (b)")
            ab = int(input(pythag_a))
            cb = int(input(pythag_c))
            print(f"The leg is ≈{math.sqrt(cb**2 - ab**2)}")
    except ValueError:
        print("Value Error: Input value must be an integer. Please re-run code and enter correct values.")
calculator()