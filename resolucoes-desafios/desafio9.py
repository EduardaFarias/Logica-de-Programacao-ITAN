matricula_antiga = "20511035"

matricula_nova = "1"
for i in range(1, (len(matricula_antiga)-3)):
    matricula_nova += matricula_antiga[i]
matricula_nova += "0"

for i in range(5, len(matricula_antiga)):
    matricula_nova += matricula_antiga[i]

print(matricula_nova)

    
