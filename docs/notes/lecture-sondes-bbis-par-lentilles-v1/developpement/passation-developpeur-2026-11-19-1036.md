# Passation du développeur neuf — lecture des sondes de l'étape B bis par la lentille publique

Session `session_013QMayj4Cr6sUZxiFq3rA8W`, branche `claude/lentilles-bbis-developpeur-v1`. Rangée ici, et non sous `registres/passations/`,
pour ne pas se glisser parmi les passations de la session mère (les registres ne me sont pas ouverts).

## Fait
- Code de la section « Code neuf » du texte scellé (`ca5066d7…`) : paquet `src/controle_ia/lentilles_sondes_bbis/` (version 1), essais
  ciblés (258 verts, `sortie-essais-v1.txt`), table des essais, notes, empreintes, outils (banc à taille réelle sur matrices aléatoires,
  essai des essais), renvois des chiffres ; tout scellé, commits `59ceab1e` et `128810af`, poussés.
- Rendu à la mère, reçu et consigné par elle (R-3731, selon son message du 2026-11-19 vers 10:36 UTC ; donnée d'une autre session).

## Reste
- Attendre le rapport du contre-lecteur d'un autre modèle, transmis en un lot par la mère ; traiter chaque remarque par écrit (faite, ou
  refusée avec sa raison) dans `traitement-contre-lecture-v1.md` ; puis vérification des corrections par le même contre-lecteur.
- Réponses de la mère à mes quatre points, à appliquer dans la version 2 seulement :
  1. biais de calibration : texte appliqué tel quel, rien ne change ; la décision (garder et déclarer, ou addendum scellé) revient à Lazar ;
  2. pôles « intermédiaires » : aucune phrase, valeurs en table (inchangé) ;
  3. corrections sous des noms neufs (`_v2`) pour les seuls modules qui changent, fichier d'empreintes v2 ; rien en place ;
  4. le code comparera ses propres empreintes à la fiche citée par `CODE-LENTILLES-BBIS` et refusera au moindre écart (cas sain et
     artefact) ; forme de la fiche : celle des fiches déjà au registre (la mère cite `registres/code-mots-et-cout-bras-a/CODE-MOTS-ET-COUT-BRAS-A-v2.json` ;
     je n'en lirai que les noms des champs, par programme, au moment d'écrire la version 2).

## Réserves
Celles des notes, § 4 : réseau réel non éprouvé ; lecture du tokeniseur par les scripts du voisin depuis le cache posé, sans clé, non
éprouvée ; pointe de mémoire 6,0 Go. Le code ne doit servir à rien avant la contre-lecture et la ligne `CODE-LENTILLES-BBIS`.

## Prochaine action
À la réception du lot de remarques : écrire la version 2 des modules touchés (dont la comparaison à la fiche du code), rejouer les essais
ciblés, sceller, pousser, rendre à la mère. D'ici là, ne pas toucher au code.

## Instances actives
Aucune machine, aucune dépense. Environnement d'essais dans le bloc-notes du conteneur (torch pour processeur, transformers, safetensors) :
à refaire si le conteneur est repris (`requirements-cpu.txt`, plus l'index de torch pour processeur).
