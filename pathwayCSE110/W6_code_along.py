# read the file - check
#skip the first line - check
#divide the line and save in variables - check
#print our report, line by line - check

with open("hr_system.txt") as file:
   next(file)

   for line in file:
      clean_line = line.strip()
      fields=clean_line.split(" ")
      paycheck_amount = (float(fields[3])/12)/2
      if fields[2].lower() == "engineer":
        paycheck_amount += 1000
         
      print(f"{fields[0]} (ID: {fields[1]}), {fields[2]} - ${paycheck_amount:.2f}")
      
print("file is closed")
    