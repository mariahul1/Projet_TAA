# Code écrit par Maria Hul

import os

##Définition des fonctions de vérification d'existence des dossiers, d'extraction des phrases et de sauvegarde
def verifier_si_le_dossier_existe(chemin_dossier):
    """
    La fonction vérifie si le dossier spécifié existe et s'il n'existe pas, la fonction le crée.
    """
    if not os.path.exists(chemin_dossier):
        os.makedirs(chemin_dossier)

def extraire_phrases(chemin_fichier, debut, fin):
    """
    La fonction extrait des phrases d'un fichier de point 'debut' jusqu'au point 'fin'.
    """
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()
    return lignes[debut:fin]

def sauvegarder_phrases(phrases, chemin_fichier):
    """
    La fonction sauvegarde une liste de phrases dans un fichier.
    """
    verifier_si_le_dossier_existe(os.path.dirname(chemin_fichier))
    with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
        fichier.writelines(phrases)

##Définitions des dossiers contenant les fichiers traités pour faciliter l'écriture de la fonction suivante
repertoire_data = 'données_du_corpus'
repertoire_europarl = 'EUROPARL-corpus'
repertoire_emea = 'EMEA-corpus'

# Extraction des lignes souhaitées et sauvegarde des données essentielles pour Run 1 et Run 2
traitement_des_données = [
    # corpus de train
    (f'{repertoire_europarl}/Europarl.en-fr.en', 0, 100000, f'{repertoire_data}/Europarl_train_100k.en'),
    (f'{repertoire_europarl}/Europarl.en-fr.fr', 0, 100000, f'{repertoire_data}/Europarl_train_100k.fr'),
    (f'{repertoire_emea}/EMEA.en-fr.en', 0, 10000, f'{repertoire_data}/Emea_train_10k.en'),
    (f'{repertoire_emea}/EMEA.en-fr.fr', 0, 10000, f'{repertoire_data}/Emea_train_10k.fr'),
    # corpus de dev
    (f'{repertoire_europarl}/Europarl.en-fr.en', 100001, 103751, f'{repertoire_data}/Europarl_dev_3750.en'),
    (f'{repertoire_europarl}/Europarl.en-fr.fr', 100001, 103751, f'{repertoire_data}/Europarl_dev_3750.fr'),
    # corpus de test
    (f'{repertoire_europarl}/Europarl.en-fr.en', 103751, 104251, f'{repertoire_data}/Europarl_test_500.en'),
    (f'{repertoire_europarl}/Europarl.en-fr.fr', 103751, 104251, f'{repertoire_data}/Europarl_test_500.fr'),
    (f'{repertoire_emea}/EMEA.en-fr.en', 10001, 10501, f'{repertoire_data}/Emea_test_500.en'),
    (f'{repertoire_emea}/EMEA.en-fr.fr', 10001, 10501, f'{repertoire_data}/Emea_test_500.fr')
]

##Traitement de données en respectant les points de 'début' et 'fin'
for fichier_input, debut, fin, fichier_output in traitement_des_données:
    phrases = extraire_phrases(fichier_input, debut, fin)
    sauvegarder_phrases(phrases, fichier_output)

