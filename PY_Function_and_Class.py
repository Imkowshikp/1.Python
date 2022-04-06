sideValue = 12;

def squareOfArea():
        
    areaOfSquare = sideValue * sideValue;
    
    print("Side =", sideValue, "\nArea formula : Side * Side", "\nArea of square:", areaOfSquare);
        
    
def squareOfPerimeter():  
      
    perimeterOfSquare = 4*sideValue;

    print("\nPerimeter formula : 4 * Side", "\nPerimeter of Square :", perimeterOfSquare);   
       

    
def linearCalculate():

    weightMeasure = 15;

    inputValue = 5;

    biasValue = 1;

    linearValue = weightMeasure * inputValue + biasValue;

    print("Weight :", weightMeasure, "\nInput :", inputValue, "\nBias Value :", biasValue, "\nFormula: Output = Weight * Input + Bias Value", "\nSimple Linear :", linearValue);

    
def ageCalculate():

    birthYear = 2000;

    presentYear = 2022;

    yearOfDateOfBirth = presentYear - birthYear;

    print("Birth Year :",birthYear, "\nPresent Year :",presentYear,"\nFormula : Present Year - Birth Year", "\nPresent Age :", yearOfDateOfBirth);


class artificialIntelligenceCourseList():
    
    def init(self):
        pass

    def aiCourse(self):

        courseHead = "Course List:";

        courseList = ["Python", "Machine Learning", "Data Science", "Deep Learning", "NLP", "Time Series Analysis"];

        print(courseHead);

        for courseAI in courseList:
            print(courseAI);
        
        
class rectangleOfAreaAndPerimeter():
    
    def init(self):
        pass

    def areaRectangle(self):

        areaLength = 12;

        areaBreadth = 18;

        areaOfRectangle = areaLength * areaBreadth;

        print("Length :", areaLength, "\nBreadth :", areaBreadth, "\nArea formula : Length * Breadth", "\nArea of rectangle :", areaOfRectangle);

    

    def perimeterRectangle(self):

        perimeterLength = 9;

        perimeterBreadth = 15;

        perimeterOfRectangle = 2 * (perimeterLength + perimeterBreadth);

        print("\nLength :", perimeterLength, "\nBreadth :", perimeterBreadth, "\nPerimeter formula : 2*(Length + Breadth)", "\nPerimeter of rectangle", perimeterOfRectangle);

   

class swapValue():
    
    def init(self):
        pass

    def valueSwapping(self):

        valueOfA = 67;

        valueOFB = 45;

        print("a=", valueOfA, "\nb=", valueOFB);

        valueOfA, valueOFB = valueOFB, valueOfA;

        print("After swapping", "\na=", valueOfA, "\nb=", valueOFB);
        
        
        
class simpleInterest():
    
    def init(self):
        pass
    

    def calculatingSimpleInterest(self):

        principleAmount = 5000;

        rateOfInterest = 5;

        timePeriod = 12;

        simpleInterest = (principleAmount * rateOfInterest * timePeriod) / 100;

        print("Principle Amount :", principleAmount, "\nRate of Interest :", rateOfInterest, "\nTime Period :", timePeriod, "\nSimple Interest formula = (P*R*T)/100", "\nSimple Interest :",simpleInterest);

        
        
class studentAverageMark():
    
    def init(self):
        pass

    def averageCalculating(self):

        import math;

        markList = [78, 89, 90]

        totalMark = sum(markList);

        averageMark = totalMark/len(markList);

        #print(round(avg,1));

        print("Mark1 =", markList[0], "\nMark2 =", markList[1], "\nMark3 =", markList[2], "\nTotal :", totalMark, "\nAverage :", math.trunc(averageMark));
        
        
        
    
class carModels():
    
    def init(self):
        pass

    def carVariant(self):

        listHead = "Car Model Names:";

        listOfCarModels = ["Maruti Alto", "Maruti Dzire", "Hyundai Creta", "Maruti Swift"];

        print(listHead);

        for carModels in listOfCarModels:
            print(carModels);
    
        
        
class primeNumber():
    
    def init(self):
        pass

    def primeNumberCalculating(self):

        getValue = int(input("Enter any number: "));

        if(getValue > 1):

            for primeValue in range(2, getValue//2): #range(2, int(getValue/2)+1):
                

                if(getValue % primeValue) == 0:

                    print(getValue, "is not prime number");
                    break;

                else:
                    print(getValue, "is a prime number");
                    break;

            else:
                print(getValue, "is not prime number");

        
        
        
        
        
        
        
        
        
        
        
        
        
        
