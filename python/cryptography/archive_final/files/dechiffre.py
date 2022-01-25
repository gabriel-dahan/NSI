 # -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 08:56:52 2022

@author: scohen
"""

message="MVVYKG M TYE RGCO QGCVGB XG BHYV"
permu_v1="".join(chr(dec) for dec in range(65, 91))
permu_v2=["m","z","x","t","g","o","j","q","y","n","w","d","p","r","h","s","u","v","b","a","c","k","f","e","l","i"]
decryptage=""
k=0
for text in message:
    if text==" ":
        decryptage+=" "
    else:
        while ord(text)!=ord(permu_v2[k])-32:
            k+=1
        decryptage+=permu_v1[k]
        k=0
print(decryptage)
