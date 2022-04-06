
class t20_Indian_Premere_Leaque():
    
    def init(self):
        pass

    def groupTeam_A(self):

        teamList_A = ["CSK", "RCB", "MI"]

        teamList_B = [1, 2, 3]




        userName = int(input("User Name :"))

        if(userName == teamList_B[0]):
            print(teamList_A[0]);

        elif(userName == teamList_B[1]):
            print(teamList_A[1]);

        elif(userName == teamList_B[2]):
            print(teamList_A[2]);

        else:
            print("Enter the Correct Value");


    #for listValue in teamList_A:
     #   print(listValue);

     



    def groupTeam_B(self):    

        getTeam = int(input("Enter the Group :"))    

        teamGroup = [1, 2]    



        teamGroup_1 = ["\nChennai Super Kings", "Royal Challengers Bangalure", "Mumbai Indians", "Kolkata Knight Riders", "Delhi Capitals"]

        teamGroup_2 = ["\nLucknow Super Giant", "Gujarat Titans", "Punjab Kings", "Sun Risers Hyderabad", "Rajastan Royals"]


        if(getTeam == teamGroup[0]):


            for teamAlpha in teamGroup_1:
                print(teamAlpha);

        elif(getTeam == teamGroup[1]):

            for teamBeta in teamGroup_2:
                print(teamBeta);
        else:
            print("Enter the Correct Value");

  


    
    