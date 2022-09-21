# Approach: Match the patients with the more strict requirements first and then match any remaining blood to less strict patients after
# Order: O-, A-/B-, AB-, O+, A+/B+, AB+

total = 0

blood = input().split(" ")
blood = [int(x) for x in blood]

patients = input().split(" ")
patients = [int(x) for x in patients]

# For O-

if blood[0] >= patients[0]:
    total += patients[0]
    blood[0] -= patients[0]
    patients[0] = 0
    
else:
    total += blood[0]
    patients[0] -= blood[0]
    blood[0] = 0
    

# For A-

if blood[2] >= patients[2]:
    total += patients[2]
    blood[2] -= patients[2]
    patients[2] = 0
    
else:
    total += blood[2]
    patients[2] -= blood[2]
    blood[2] = 0
    

# For B-

if blood[4] >= patients[4]:
    total += patients[4]
    blood[4] -= patients[4]
    patients[4] = 0

    
else:
    total += blood[4]
    patients[4] -= blood[4]
    blood[4] = 0
    

# Redistrbute remaining O-
# To A-
if blood[0] > 0:
    if patients[2] > 0:
        if blood[0] >= patients[2]:
            total += patients[2]
            blood[0] -= patients[2]
            patients[2] = 0
            
        else:
            total += blood[0]
            patients[2] -= blood[0]
            blood[0] = 0

# To B-
if blood[0] > 0:
    if patients[4] > 0:
        if blood[0] >= patients[4]:
            total += patients[4]
            blood[0] -= patients[4]
            patients[4] = 0
            
        else:
            total += blood[0]
            patients[4] -= blood[0]
            blood[0] = 0
            
            
# For AB-

if blood[6] >= patients[6]:
    total += patients[6]
    blood[6] -= patients[6]
    patients[6] = 0
    
else:
    total += blood[6]
    patients[6] -= blood[6]
    blood[6] = 0
    




# For O+

if blood[1] >= patients[1]:
    total += patients[1]
    blood[1] -= patients[1]
    patients[1] = 0
    
    
else:
    total += blood[1]
    patients[1] -= blood[1]
    blood[1] = 0
    
    

# For A+

if blood[3] >= patients[3]:
    total += patients[3]
    blood[3] -= patients[3]
    patients[3] = 0
    
    
else:
    total += blood[3]
    patients[3] -= blood[3]
    blood[3] = 0
    
    

# For B+

if blood[5] >= patients[5]:
    total += patients[5]
    blood[5] -= patients[5]
    patients[5] = 0
    
    
else:
    total += blood[5]
    patients[5] -= blood[5]
    blood[5] = 0
    


# Redistrbute remaining O+
# To A+
if blood[1] > 0:
    if patients[3] > 0:
        if blood[1] >= patients[3]:
            total += patients[3]
            blood[1] -= patients[3]
            patients[3] = 0
            
        else:
            total += blood[1]
            patients[3] -= blood[1]
            blood[1] = 0

# To B+
if blood[1] > 0:
    if patients[5] > 0:
        if blood[1] >= patients[5]:
            total += patients[5]
            blood[1] -= patients[5]
            patients[5] = 0
            
        else:
            total += blood[1]
            patients[5] -= blood[1]
            blood[1] = 0


# For AB+

if blood[7] >= patients[7]:
    total += patients[7]
    blood[7] -= patients[7]
    patients[7] = 0
    
else:
    total += blood[7]
    patients[7] -= blood[7]
    blood[7] = 0


# Distribute remaining - to +
# O
if blood[0] > 0 and patients [1] > 0:
    if blood[0] >= patients[1]:
        total += patients[1]
        blood[0] -= patients[1]
        patients[1] = 0
    
    else:
        total += blood[0]
        patients[1] -= blood[0]
        blood[0] = 0

# A
if blood[0] > 0 and patients [3] > 0:
    if blood[0] >= patients[3]:
        total += patients[3]
        blood[0] -= patients[3]
        patients[3] = 0
    
    else:
        total += blood[0]
        patients[3] -= blood[0]
        blood[0] = 0

if blood[2] > 0 and patients [3] > 0:
    if blood[2] >= patients[3]:
        total += patients[3]
        blood[2] -= patients[3]
        patients[3] = 0
    
    else:
        total += blood[2]
        patients[3] -= blood[2]
        blood[2] = 0

# B
if blood[0] > 0 and patients [5] > 0:
    if blood[0] >= patients[5]:
        total += patients[5]
        blood[0] -= patients[5]
        patients[5] = 0
    
    else:
        total += blood[0]
        patients[5] -= blood[0]
        blood[0] = 0

if blood[4] > 0 and patients [5] > 0:
    if blood[4] >= patients[5]:
        total += patients[5]
        blood[4] -= patients[5]
        patients[5] = 0
    
    else:
        total += blood[4]
        patients[5] -= blood[4]
        blood[4] = 0

# Send all remaining bloods to AB- and AB+
# AB- 
if blood[0] > 0 and patients [6] > 0:
    if blood[0] >= patients[6]:
        total += patients[6]
        blood[0] -= patients[6]
        patients[6] = 0
    
    else:
        total += blood[0]
        patients[6] -= blood[0]
        blood[0] = 0
        
if blood[2] > 0 and patients [6] > 0:
    if blood[2] >= patients[6]:
        total += patients[6]
        blood[2] -= patients[6]
        patients[6] = 0
    
    else:
        total += blood[2]
        patients[6] -= blood[2]
        blood[2] = 0

if blood[4] > 0 and patients [6] > 0:
    if blood[4] >= patients[6]:
        total += patients[6]
        blood[4] -= patients[6]
        patients[6] = 0
    
    else:
        total += blood[0]
        patients[6] -= blood[0]
        blood[4] = 0

#AB+

if blood[1] > 0 and patients [7] > 0:
    if blood[1] >= patients[7]:
        total += patients[7]
        blood[1] -= patients[7]
        patients[7] = 0
    
    else:
        total += blood[1]
        patients[7] -= blood[1]
        blood[1] = 0
        
if blood[3] > 0 and patients [7] > 0:
    if blood[3] >= patients[7]:
        total += patients[7]
        blood[3] -= patients[7]
        patients[7] = 0
    
    else:
        total += blood[3]
        patients[7] -= blood[3]
        blood[3] = 0

if blood[5] > 0 and patients [7] > 0:
    if blood[5] >= patients[7]:
        total += patients[7]
        blood[5] -= patients[7]
        patients[7] = 0
    
    else:
        total += blood[0]
        patients[7] -= blood[0]
        blood[5] = 0
        
if blood[0] > 0 and patients [7] > 0:
    if blood[0] >= patients[7]:
        total += patients[7]
        blood[0] -= patients[7]
        patients[7] = 0
    
    else:
        total += blood[0]
        patients[7] -= blood[0]
        blood[0] = 0
        
if blood[2] > 0 and patients [7] > 0:
    if blood[2] >= patients[7]:
        total += patients[7]
        blood[2] -= patients[7]
        patients[7] = 0
    
    else:
        total += blood[2]
        patients[7] -= blood[2]
        blood[2] = 0

if blood[4] > 0 and patients [7] > 0:
    if blood[4] >= patients[7]:
        total += patients[7]
        blood[4] -= patients[7]
        patients[7] = 0
    
    else:
        total += blood[0]
        patients[7] -= blood[0]
        blood[4] = 0
    
print(total)
