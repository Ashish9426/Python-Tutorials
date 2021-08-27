# logical operators

# and => &&

# true and true     => true
# true and false    => false
# false and true    => false
# false and false   => false

age = 70
# age > 20 and age<60
# if() {
#      code
#      }

if (age > 25) and (age < 60):
    print(f"inside if block")
    print(f"Valid age for an Employee")
else:
    print(f"inside else block")
    print(f"Invalid aage for an Employee")
print(f"This is the out of if and else Block")

print("-*-" * 20)
# or  => ||
if (age > 25) or (age < 60):
    print(f"inside if block")
    print(f"valid age for an Employee")
else:
    print(f"inside else block")
    print(f"invalid age for an Employee")
