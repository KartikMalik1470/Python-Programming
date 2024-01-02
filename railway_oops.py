import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        print(f"age is {self.age}")

kartiksApplication = RailwayForm()
kartiksApplication.name = "Kartik"
kartiksApplication.train = "Rajdhani Express"
kartiksApplication.age = "23"
kartiksApplication.printData()