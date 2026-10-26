# def add (a,b):
#     return a+b
# print(add(10,20))


class employee:
    def __init__(self,name):
        self.name =name

    def login(self):
        return f"{self.name} has logged in."

    def view_task(self):
        return f"{self.name} can view assigned task."

class team_member(employee):
    def submit_task(self):
        return f"{self.name} has submitted the task."

class manager(employee):
    def assign_task(self):
        return f"{self.name} has assigned the task."

arun= team_member("Arun")
mani= manager("Mani")

print(arun.login())
print(arun.submit_task())
print(mani.login())
print(mani.assign_task())