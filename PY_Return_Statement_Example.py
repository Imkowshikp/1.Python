
class totalNumberOfStudents():
    
    def init(self):
        pass

    def overallBoysCounting(self):

        boysFirstLanguageOverallStudents = 500;

        boysMathsOverallStudents = 750;

        boysPhysicsOverallStudents = 650;

        boysChemistryOverallStudents = 770;

        boysBiologyOverallStudents = 550;

        totalNumberOfBoysStudents = boysFirstLanguageOverallStudents + boysMathsOverallStudents + boysPhysicsOverallStudents + boysChemistryOverallStudents +boysBiologyOverallStudents;

        return totalNumberOfBoysStudents;

     


    def overallGirlsCounting(self):

        girlsFirstLanguageOverallStudents = 370;

        girlsMathsOverallStudents = 500;

        girlsPhysicsOverallStudents = 600;

        girlsChemistryOverallStudents = 750;

        girlsBiologyOverallStudents = 570;

        totalNumberOfGirlsStudents = girlsFirstLanguageOverallStudents + girlsMathsOverallStudents + girlsPhysicsOverallStudents + girlsChemistryOverallStudents + girlsBiologyOverallStudents;

        return totalNumberOfGirlsStudents;

   


    def totalStudents(self):
        
        totalNumberOfBoys = totalNumberOfStudents.overallBoysCounting(self);
        
        totalNumberOFGirls = totalNumberOfStudents.overallGirlsCounting(self);
        
        overallStudents = totalNumberOfBoys + totalNumberOFGirls;
                
        print("Total Number of Students of the Year :", overallStudents);
        
        return overallStudents;
    
    
    
 
    
      