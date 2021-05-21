from alg import *
from os import system, name

clearConsole = lambda: system('cls' if name in ('nt', 'dos') else 'clear')

if __name__ == "__main__":
    while (True):
        # inputs
        n= int(input("Please enter number of processes (n): "))
        m= int(input("Please enter number of resources (m): "))
        print("")

        s="   "
        alloc=[]
        maxm=[]
        aval=""
        for i in range(m):
            s+= "R"+ str(i)+" "

        print("Please fill the Allocation matrix separated by spaces")
        print(s)
        for i in range(n):
            alloc.append(input("P"+str(i)+" "))
        print("")

        print("Please fill the Max matrix separated by spaces")
        print(s)
        for i in range(n):
            maxm.append(input("P"+str(i)+" "))
        print("")

        print("Please fill the Available vector separated by spaces")
        print(s[3:])
        aval=input("")
        print("")

        # Data
        aval = aval.split()
        map_object = map(int, aval)
        Aval = list(map_object)

        Maxm = []
        for i in range(n):
            temp = maxm[i].split()
            map_object = map(int, temp)
            Maxm.append(list(map_object))

        Alloc = []
        for i in range(n):
            temp = alloc[i].split()
            map_object = map(int, temp)
            Alloc.append(list(map_object))

        Need = []
        temp = []
        for i in range(m):
            temp.append(0)
        for i in range(n):
            Need.append(temp.copy())
        for i in range(n):
            for j in range(m):
                Need[i][j] = Maxm[i][j] - Alloc[i][j]

        # Output
        print("The Need matrix")
        print(s)
        for i in range(n):
            print("P" + str(i), Need[i])
        print("")

        # Input
        print("Enter 0 for Safety check or enter 1 for immediate request check")
        decision = int(input())
        if decision == 1:
            index = int (input("Enter the requesting process index (Hint: index starts from 0): P"))
            print("Enter the requesting resources")
            print(s)
            req = input("P"+ str(index)+" ")
        print("")



        if decision == 1:
            req = req.split()
            map_object = map(int, req)
            Req = list(map_object)
        # Processing
        if decision == 0:
            safe,seq = safety(n, m, Aval.copy(), Alloc.copy(), Need.copy())
            sequence = ""
            if safe==1:
                for i in range(n):
                    sequence += ("P" + str(seq[i]) + ",")
                sequence = sequence[:len(sequence) - 1]

        elif decision == 1:
            result,safe,seq = request(n, m, Aval.copy(), Alloc.copy(), Need.copy(),index,Req)
            if result==1 and safe==1:
                sequence = ""
                for i in range(n):
                    sequence += ("P" + str(seq[i]) + ",")
                sequence=sequence[:len(sequence)-1]

        # Output
        if decision==0:
            if safe == 1:
                print("Yes, Safe state <" + sequence + ">")
            else :
                print("No, Not in safe state ")

        if decision == 1:
            if result==-1:
                print("Error the process exceeded the maximum claim of the resources")
            elif result==0:
                print("Request cannot be performed the process must wait")
            elif result==1:
                if safe ==1:
                    print ("Yes request can be granted with safe state, Safe state <P"+str(index)+"req,"+sequence+">")
                elif safe==0:
                    print("No request cannot be granted with safe state")

        print("")

        restart= input("If you want to restart the whole program enter Y or anything else for termination: ")
        clearConsole()
        if restart !="Y":
            break