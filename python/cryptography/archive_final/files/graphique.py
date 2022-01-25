#cryptanalyse
import matplotlib.pyplot as plt

lettre = list(range(26))
lcrypte = [x+0.3 for x in lettre]
alpha="abcdefghijklmnopqrstuvwxyz"
# F est la liste des fréquences des lettres de la langue française
F = [8.15,0.97,3.15,3.73,17.39,1.12,0.97,0.85,7.31,0.45,0.02,5.69,2.87,7.12,5.28,2.80,1.21,6.64,8.14,7.22,6.38,1.64,0.03,0.41,0.28,0.15]
plt.xticks(lettre,list(alpha))
#freq est la liste des fréquences obtenues
#plt.bar(lettre,freq,color = 'red')
plt.bar(lcrypte,F, color = 'green')
plt.grid(True)
plt.show()
