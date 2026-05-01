x_int = 7
x_float = 7.0
print(x_int)
print(x_float)
print(float(x_int))

x_string = 'test1'
x_string2 = "test2"
print(x_string)
print(x_string2)

x = 1
y = 2
z = x + y
print(z)

x_string = "Hello"
y_string = "World"
z_string = x_string + " " + y_string
print(z_string)

x1, x2 = 1, 2
print(x1, x2)

# change this code
sol_string = "hello"
sol_float = 10.0
sol_int = 20

# testing code
if sol_string == "hello":
    print("String: %s" % sol_string)
if isinstance(sol_float, float) and sol_float == 10.0:
    print("Float: %f" % sol_float)
if isinstance(sol_int, int) and sol_int == 20:
    print("Integer: %d" % sol_int)

# change this code 2
sol2_string = "hello2"
sol2_float = 20.0
sol2_int = 40

# testing code
if sol2_string == "hello2":
    print(f"string: {sol2_string}")
if isinstance(sol2_float, float) and sol2_float == 20.0:
    print(f"Float: {sol2_float}")
if isinstance(sol2_int, int) and sol2_int == 40:
    print(f"Integer: {sol2_int}")
