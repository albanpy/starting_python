male=int(input("Enter number of males registered in a class:"))
female=int(input("Enter number of females registered in a class:"))
total=male+female
#ml=(male/total)*100
#fm=(female/total)*100
print(f"The percentage of males student in a class are {male/total:%}\n"
      f"The percentage of females student in a class are {female/total:%}")
#print(f"The percentage of males student in a class are {ml:.2f}%\n"
      #f"The percentage of females student in a class are {fm:.2f}%")

