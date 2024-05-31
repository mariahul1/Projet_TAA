import os
from nltk.stem import WordNetLemmatizer
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer

# Initialisation du lemmatiseur pour la langue anglaise
lemmatizer_en = WordNetLemmatizer()

# Initialisation du lemmatiseur pour la langue française
lemmatizer_fr = FrenchLefffLemmatizer()

# Fonction pour lemmatiser une phrase selon la langue spécifiée
def lemmatize_sentence(sentence, lang='en'):
    if lang == 'en':
        return [lemmatizer_en.lemmatize(word) for word in sentence]
    elif lang == 'fr':
        return [lemmatizer_fr.lemmatize(word) for word in sentence]
    else:
        raise ValueError("Langue non supportée")

# Chemin vers le dossier avec les fichiers à lemmatiser
input_folder = '/content/drive/MyDrive/données_du_corpus'  # Chemin vers le dossier avec les fichiers

# Chemin vers le dossier où seront enregistrés les lemmes
output_folder = '/content/drive/MyDrive/lemmatisés_non_tokenisés'  # Chemin vers le dossier de sortie

# Vérifier si le dossier de sortie existe, sinon le créer
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Traitement de tous les fichiers dans le dossier d'entrée
for file_name in os.listdir(input_folder):
    input_file_path = os.path.join(input_folder, file_name)

    # Vérifier si le fichier d'entrée est un fichier texte
    if os.path.isfile(input_file_path):
        lang = 'en' if file_name.endswith('.en') else 'fr'

        with open(input_file_path, 'r', encoding='utf-8') as infile:
            # Créer le nom de fichier de sortie
            output_file_name = file_name.replace('.en', '_lemmatised.en').replace('.fr', '_lemmatised.fr')
            output_file_path = os.path.join(output_folder, output_file_name)

            with open(output_file_path, 'w', encoding='utf-8') as outfile:
                # Traitement de chaque ligne dans le fichier d'entrée
                for line in infile:
                    tokens = line.strip().split()  # Diviser la ligne en tokens
                    lemmatized_tokens = lemmatize_sentence(tokens, lang)  # Lématiser les tokens
                    outfile.write(' '.join(lemmatized_tokens) + '\n')  # Enregistrer les lemmes dans le fichier de sortie
