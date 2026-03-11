# Programme de chiffrement César avec message et clé fixes

message = "coucou"  # message à chiffrer
cle = 3             # clé de décalage

resultat = ""

# parcourir chaque lettre du message
for lettre in message:
    if lettre.isalpha():
        if lettre.isupper():
            resultat += chr((ord(lettre) - 65 + cle) % 26 + 65)
        else:
            resultat += chr((ord(lettre) - 97 + cle) % 26 + 97)
    else:
        resultat += lettre

# afficher le résultat
print("Message chiffré :", resultat)
import hashlib

text1 = "cybersecurity"
text2 = "cybersecurity!"

hash1 = hashlib.sha256(text1.encode()).hexdigest()
hash2 = hashlib.sha256(text2.encode()).hexdigest()

print("Hash 1:", hash1)
print("Hash 2:", hash2)
import hashlib

# 1️⃣ Créer un fichier texte
with open("admin_config.txt", "w") as f:
    f.write("Configuration admin serveur")

# 2️⃣ Calculer le hash SHA-256 du fichier original
with open("admin_config.txt", "rb") as f:
    data = f.read()
hash_original = hashlib.sha256(data).hexdigest()
print("Hash original :", hash_original)

# 3️⃣ Modifier une lettre dans le fichier
with open("admin_config.txt", "w") as f:
    f.write("Configuration admin server")  # changement d'une lettre

# 4️⃣ Recalculer le hash SHA-256
with open("admin_config.txt", "rb") as f:
    data_modifie = f.read()
hash_modifie = hashlib.sha256(data_modifie).hexdigest()
print("Hash après modification :", hash_modifie)

# 5️⃣ Vérifier si le fichier a été modifié
if hash_original == hash_modifie:
    print("Le fichier n'a pas été modifié.")
else:
    print("Attention : le fichier a été modifié !")
    