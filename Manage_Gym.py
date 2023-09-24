import textwrap
class Gym:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.payments = []

    def add_members(self, member):
        self.members.append(member)

    def add_payments(self, payment):
        self.payments.append(payment)
    
    def remove_members(self, member):
        self.members.remove(member)

class Member:
    def __init__(self, id_member, name ,cpf):
        self._id = id_member
        self.name = name
        self.cpf = cpf
        self.payment = False
        self.academic_plan = None
    
    @classmethod
    def new_member(cls,id_member, name ,cpf):
        return cls(id_member, name ,cpf)
    



def menu():
    menu = """
========== MENU ==========
[1] -> Add Member
[2] -> Add Payment
[3] -> List Members
[4] -> Status Member
[5] -> Remove Member
[s] -> Stop 
:
"""
    print(menu)


def verify_members(cpf, Gym):
    for i in Gym.members:
        if cpf in i.cpf :
            return True

def recovery_members(cpf, Gym):
    for i in Gym.members:
        if cpf in i.cpf :
            return i
       


def check_cpf():
    while True:
        cpf = input("Enter CPF the member: ")
        if cpf.isdigit():
            return cpf
        else:
            print("@@ Enter a valid value @@")

def add_plan(cpf, Gym):
    Member = recovery_members(cpf, Gym)
    while True:
        plan = input("Enter plan the member [1 -> Basic] [2 -> Premium]: ")
        if plan == "1":
            Member.academic_plan = "BASIC"
            return
        elif plan == "2":
            Member.academic_plan = "PREMIUM"
            return
        else:
            print("@@ Enter a valid value @@")


def is_alpha_space(str):
    return all(char.isalpha() or char.isspace() for char in str)

def check_name():
    while True:
        name=input('Enter name the member: ')
        if is_alpha_space(name) and len(name) >= 3:
            return name
        else:
            print("@@ Enter a valid value @@")

def add_member(id_member, Gym):
    name = check_name()
    cpf = check_cpf()
    verification = verify_members( cpf , Gym)
    if verification :
        print("@@ The member is already part of the gym @@")
    else:
        confirmation_member = input(f"## Do you want to add member {name.upper()} / CPF: {cpf}? [y/n] ")
        if confirmation_member == "y":   
            newMember = Member.new_member(id_member=id_member,name=name.upper(), cpf=cpf)
            Gym.add_members(newMember)
            plan = add_plan(cpf,Gym)
            print("## The member was added successfully ##")
        else: 
            print("@@ operation canceled @@")
        


def check_float(value):
    
    if value.isdigit():
        value = float(value)
        if value > 0:
            return False
        else:
            return True
    else:
        return True


def add_payment(id_payment, Gym):
    cpf = input("Enter CPF the member: ")
    verification = verify_members( cpf , Gym)
    if verification:
        Member = recovery_members(cpf, Gym)
        confirmation_member = input(f"## Should the payment be added to member {Member.name} / CPF: {Member.cpf} account? [y/n] ")
        if confirmation_member == "y":
            while True:
                value = input("Enter the payment amount: ")
                if check_float(value):
                    print("@@ Enter a valid value @@")
                else:
                    break

            Member.payment = True
            Gym.add_payments([id_payment, Member.name, Member.cpf, value])
            print("## The payment was added successfully ##")
        else:
            print("@@ operation canceled @@")
    else:
        print("@@ This member does not exist. @@")


def status_member(Gym):
    cpf = input("Enter CPF the member: ")
    verification = verify_members( cpf , Gym)
    if verification:
        Member = recovery_members(cpf , Gym)
        text = "is up to date with payment" if Member.payment else "is late in payment"
        print(f"## The member {Member.name} {text} ##")
    else:
        print("@@ This member does not exist. @@")

def remove_member(Gym):
    cpf = input('Enter CPF the member:')
    verification = verify_members( cpf , Gym)
    if verification:
        Member = recovery_members(cpf , Gym)
        confirmation_member = input(f"## Do you want to removed member {Member.name} / CPF: {Member.cpf}? [y/n] ")
        if confirmation_member == "y":    
            Gym.remove_members(Member)
            print("## The member removed successfully ##")
        else:
            print("@@ operation canceled @@")
    else:
        print("@@ This member does not exist. @@")

        



def main():
    Name_Gym = Gym(input("Enter name the Gym: "))
    id_member = 0
    id_payment = 0
    while True:
        menu()
        options = input()

        if options == "1":
            id_member += 1
            add_member(id_member, Name_Gym)
        
        elif options == "2":
            id_payment += 1
            add_payment(id_payment,Name_Gym)
        
        elif options == "3":
            cont = 0
            if Name_Gym.members:
                print(f"############ Members the Gym {Name_Gym.name} ############")
                for i in Name_Gym.members:
                    cont+=1
                    print(f"{cont}° {i.name} / CPF: {i.cpf} / Payment: {i.payment} / Plan: {i.academic_plan}")
            else:
                print("@ There are no members @")
        
        elif options == "4":
            status_member(Name_Gym)
        
        elif options == "5":
            remove_member(Name_Gym)
        
        elif options == "s":
            break
main()
