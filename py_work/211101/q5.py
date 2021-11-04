gcm=42
while gcm >=0:
    gcm = gcm - 1
    if 120 % gcm == 0 and 42 % gcm ==0:
        break
print(gcm)