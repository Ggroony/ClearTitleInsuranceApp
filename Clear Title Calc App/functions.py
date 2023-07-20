from pywebio.input import * 
from pywebio.output import *


class Property_Calc:
  

  
  def begin(): #headertext
    logo = open('images\Logo.jpg', 'rb').read()
    put_image(logo, width = '100px', height= '100px').style('margin-top: 10px; margin-right: 50%; margin-bottom: 20px')
    put_text("Welcome to Clear Title's Title Insurance Calculator!\n").style('color:#000080; font-size:30px; text-decoration:underline')
    put_text("Please enter the information below to retrieve your title insurance quote \n")
    
    #createing variables to store similtaneos policy rates (need 2 for the owners policy and the lenders policy)
    global insurance_rate_loan1 #variable 1 to store the loan amount
    insurance_rate_loan1 = 0.003875
    
    global insurance_rate_loan2 #variable 1 to store the loan sales price amount
    insurance_rate_loan2 = 200 #this amount is always $200 according to OR's calculator
    
    global insurance_rate_cash #variable to store general title insurance rate
    insurance_rate_cash = 0.003875 #Old Republic Cash Rate (Kentucky as of 7/13/2023)
      
  def property_data(): #function recieving user input for loan, then outputing their results
    
    choice = select("Please select your transaction type", ['Cash', 'Financing/Loan']) #Drop down selection for property type
   
    value_cash = 0.00 #creating a variable to store the input for propertycash[sales] so I can multiply it with the underwriter's insurance rate
    value_loan = 0.00 #variable to store propertyloan[loan]
    value_loan_sales = 0.00 #variable to store loan sales price
    default_Cash = "$200"
      
    if choice == 'Financing/Loan': #if choice is for a loan, then it asks user to input loan amount
      global propertyloan
      propertyloan = input_group("Title Insurance Calculator:",[
        input('Input your Address', name = 'address'),
        input("Input your Loan Amount", name = 'loan', type = NUMBER),
        input("Input the Sales Price", name = 'sales', type = NUMBER),
        ]
                      )
      
      value_loan = propertyloan['loan']
      
      
      preloanquote = value_loan * insurance_rate_loan1 #multiplying the global loan rate times the inputed loan amount by the user (still need to add 200 for the owners policy)
      loanquote = preloanquote + insurance_rate_loan2 #Adding 200 to include the simultaneos owners policy rate of $200
      
      put_table([ #visually returning the insurance quote
        [('Lenders & Owners Title Insurance Estimate (In Dollars)')], [loanquote]
        
      ])
      
      #disclaimer
      
      put_text("Please note, that this rate does not include local tax rates, lender endorsements or premiums that may need to be included for your specific property, be sure to advise with your lender or processor about your transaction for a more up to date estimate.")

      put_text("Want to find out more about what Title Insurance covers? Call us today at (859)-523-8485, or email us at orders@kycleartitle.com").style('margin-top: 200px; color: blue; font-size: 30px;') 
      
      
    if choice == 'Cash': #if choice is cash, then asks user to input only sales info
      global propertycash
      propertycash = input_group("Title Insurance Calculator:",[
        input('Input your Address', name = 'address', required=True),
        input("Input the Sales Price", type = NUMBER, name ='sales', required=True),
        ]
                            )
      
      value_cash = propertycash['sales']
      quote = value_cash * insurance_rate_cash #multiply the user's input for price and multiply it by the global rate to get the rate quote
      
      if quote <= 200:
        put_table([ #visually returning the insurance quote if quote is less than 200 (minimum owners insurance policy is $200)
        [('Title Insurance Estimate (In Dollars)')], [default_Cash]
        
      ])
             
      else:
        put_table([ #visually returning the insurance quote
        [('Title Insurance Estimate (In Dollars)')], [quote]
        
      ])
      
      #disclaimer
      
      put_text("Please note, that this rate does not include local tax rates, or premiums that may be included in the same of your specific property, be sure to advise with your processor about your transaction for a more up to date estimate.")

      put_text("Want to find out more about what Title Insurance covers? Call us today at (859)-523-8485").style('margin-top: 200px; color: blue; font-size: 30px;') 
 
 
  def insurance_output(): #potential function to create a pdf of the quote for the user to print/keep - or I could make a function to simply print the page
    

    '''  
  def check_loan(property): # Function to error handle incorrect loan input
    if property['loan'] <= 0:
      return ('loan', "Cannot be equal to or lower than 0")
