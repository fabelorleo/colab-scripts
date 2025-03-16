import os
from google.colab import drive

# Montiamo Google Drive
drive.mount('/content/drive')

# Definiamo il percorso della cartella principale di Google Drive
drive_path = "/content/drive/MyDrive/"

# Lista di tutti i file nella cartella Drive e sottocartelle
all_files = []
for root, dirs, files in os.walk(drive_path):
    for file in files:
        full_path = os.path.join(root, file)
        all_files.append(full_path)

# Mostriamo tutti i file trovati
print("\n📂 **Tutti i file trovati in Google Drive:**\n")
for file in all_files:
    print(file)
