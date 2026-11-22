# Mandat du releveur neuf — relevés de la plateforme de modèles avant le réajustement (devis v9, § 5, points 4 et 9) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-22, sur le mot de Lazar ed47f2e3…. Français.

## Ce que tu relèves, sur pages publiques seulement (documentation, conditions, code source public de `huggingface_hub`)
1. **Clé restreinte** (point 4) : la plateforme permet-elle une clé à grain fin qui lise un modèle à accès contrôlé
   (`meta-llama/Llama-3.1-8B-Instruct`) **et** n'écrive que sur un seul dépôt privé ? Quelles cases exactes Lazar doit cocher ?
2. **Stockage privé** (point 9) : coût et quota du stockage privé de modèles pour un compte personnel (≈ 31 Go : ≈ 17 Go de fichiers
   d'ajustement, ≈ 13 Gio d'exports), coût mensuel en chiffre ; taille maximale par fichier ; limites d'envoi.
3. **Empreinte rendue pour un gros fichier** : pour un fichier stocké en grand fichier (LFS ou Xet), l'empreinte SHA-256 que
   l'interface rend est-elle recalculée ou vérifiée par la plateforme à la réception, ou déclarée par l'envoyeur ? Appuie-toi sur la
   documentation et le code public (protocole LFS, stockage Xet) ; dis ce qui est établi et ce qui ne l'est pas.
4. **Débit en écriture** : ce que la documentation en dit (rien de mesuré par toi).
5. **Licence** : la licence de Llama 3.1 permet-elle de ranger en privé des poids dérivés (lentilles ajustées sur ses activations) ?
   Citation exacte, paragraphe nommé.
Chaque réponse : source (adresse), date du relevé, citation courte exacte, et « établi », « probable » ou « non établi ».

## Ce que tu ne fais pas
**Aucune requête vers l'interface de la plateforme avec une clé** ; aucune clé lue, testée ni citée autrement que par son nom ; aucun
compte créé ; rien loué ni dépensé ; aucune donnée du projet dans les requêtes. Rien du dépôt hors de ce mandat, du devis v9
(`docs/notes/neuron-lens-v1/devis-reajustement/devis-reajustement-lentilles-b-beta-v9.md`) et de `CLAUDE.md`.

## Rendu
`docs/notes/neuron-lens-v1/devis-reajustement/releves-plateforme-reajustement-v1.md`, scellé (`PYTHONPATH=src python -m
controle_ia.scellement sceller <chemin>`), non committé (la session des lentilles committe). Dernier message : les cinq réponses en une
ligne chacune, empreinte du fichier.
