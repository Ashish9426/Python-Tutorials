# 1st method -> simple calculator

def calculator(p1, p2):
    addition = p1 + p2
    print(f"Addition of two no. = {addition}")
    print("-*-" * 10)
    substration = p1 - p2
    print(f"Substraction  of two no. = {substration}")
    print("-*-" * 10)
    multiplication = p1 * p2
    print(f"Multiplication of two no. = {multiplication}")
    print("-*-" * 10)
    division = p1/p2
    print(f"Division of two no. = {division}")
    print("-*-" * 10)

# calculator(20, 10)


# 2nd method -> simple calculator

def calculator1(p1, p2):

    addition = p1 + p2
    print(f"Addition of two no. = {addition}")
    print("-*-" * 10)
    substration = p1 - p2
    print(f"Substraction  of two no. = {substration}")
    print("-*-" * 10)
    multiplication = p1 * p2
    print(f"Multiplication of two no. = {multiplication}")
    print("-*-" * 10)
    division = p1/p2
    print(f"Division of two no. = {division}")
    print("-*-" * 10)


#print("-----Enter two number for calculation-----")
#print("Enter first number:")
#value1 = int(input())
#print("Enter second number:")
#value2 = int(input())

# calculator1(value1, value2)
# calculator1(p1=value1, p2=value2)


# 3rd method -> simple calculator
def math_operations(p1, p2):
    addition = p1 + p2
    subtraction = p1 - p2
    division = p1 / p2
    multiplication = p1 * p2
    return addition, subtraction, division, multiplication


answers = math_operations(40, 20)
print(f"answers = {answers}, type = {type(answers)}")
print(f"addition = {answers[0]}")
print(f"subtraction = {answers[1]}")
print(f"division = {answers[2]}")
print(f"multiplication = {answers[3]}")