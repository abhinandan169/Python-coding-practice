# Create a class Company with a class variable company_name = "TechCorp". Add a class method rename(new_name) that changes company_name. Create two Company objects, call rename once, and show that both objects see the new name.


class Company:
    company_name = "TechCorp"

    @classmethod
    def rename(cls, new_name):
        cls.company_name = new_name

c1 = Company()
c2 = Company()

Company.rename("InnovateX")

print(c1.company_name)
print(c2.company_name)   