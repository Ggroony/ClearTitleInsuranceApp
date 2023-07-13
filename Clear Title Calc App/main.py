from functions import *

from pywebio import *

def main():  # PyWebIO application function
  
  Property_Calc.begin()
  Property_Calc.property_data()

start_server(main, port=8080, debug=True)