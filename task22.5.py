class Student:
    pass

st1.name = "Alex"
st1.age = 20
st1.mark = 10

st2.name = "Alisa"
st2.age = 18
st2.mark = 9

def view(student):
    return (f"{student.name}: age = {student.age}, "
            f"mark = {student.mark}")

print(view(st1))
print(view(st2))