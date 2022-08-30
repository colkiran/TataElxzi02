
class Manager:

    def doJob(self):
        print("Manager's Job.....")

class Developer:

    def doJob(self):
        print("Developers Job......")


def BankJobs(emps):
    print("Bank Job Started.......")
    for emp in emps:
        emp.doJob()
    print("Bank job Completed........")

Mike = Manager()
David = Developer()

BankJobs([Mike, David])