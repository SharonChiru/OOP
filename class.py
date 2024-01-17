class Person:
  def __init__(self, name, age, profession):
    self.name = name
    self.age = age
    self.profession = profession

p1 = Person("Sharon", 40, "teacher")

print(p1.name)
print(p1.age)
print(p1.profession)


class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def display_info(self):
        return f"My name is {self.name}. I am {self.age} years old, and I am a {self.profession}."

# Create an instance of the Person class
p1 = Person("Sharon", 40, "teacher")

# Call the display_info method to print the desired information
print(p1.display_info())

