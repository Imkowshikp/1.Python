class pythonCalculator():
    
    def init(self):
        pass

    def calculating(self):

        firstOperand = int(input("Enter the First Operand :"));

        operators = input("\nEnter the Operator(+, -, *, /, %, //, %, **) :");

        secondOperand = int(input("\nEnter the Second Operand :"));

        if(operators == "+"):
            calculateAnswer = firstOperand + secondOperand;

        elif(operators == "-"):
            calculateAnswer = firstOperand - secondOperand;

        elif(operators == "*"):
            calculateAnswer = firstOperand * secondOperand;

        elif(operators == "/"):
            calculateAnswer = firstOperand / secondOperand;

        elif(operators == "%"):
            calculateAnswer = firstOperand % secondOperand;

        elif(operators == "//"):
            calculateAnswer = firstOperand // secondOperand;

        elif(operators == "**"): 
            calculateAnswer = firstOperand ** secondOperand;

        print("\nAnswer :", calculateAnswer);
