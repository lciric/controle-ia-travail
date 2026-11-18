# Vérification courte de « Lecture sur PDF des pistes de priorité haute contre O4 » v2

**Verdict : conforme avec réserves.**

- **auteur : modèle C ; vérificateur : modèle D ; C ≠ D.** Le vérificateur est l'auteur de la contre-lecture de la v1 ; il n'a écrit aucune des trois pièces de la v2.
- **Heures (`date -u`)** : début 2026-11-14T09:43:26Z ; rejeu des citations 2026-11-14T09:43:36Z ; contrôles page par page 2026-11-14T09:44:14Z et 2026-11-14T09:44:30Z ; écriture de ce fichier 2026-11-14T09:45:25Z.
- **Pièces jugées** (empreinte recalculée = compagnon `.sha256`) : `lecture-pdf-priorite-haute-o4-v2.md` `fc7c09f4…` ; `citations-priorite-haute-o4-v2.json` `186de41c…` ; `resultat-citations-priorite-haute-o4-v2.json` `76443bac…`. Les v1 sont intactes : note `1e841edd…`, liste `7c339ba5…`, programme de l'auteur `2daf5daa…`, mêmes empreintes que dans ma contre-lecture de la v1 (le programme de l'auteur est donc bien inchangé).
- **Fait** : contre-lecture v1 et v2 lues en entier ; 69 citations rejouées par mon programme ; couverture note ↔ liste contrôlée ; affirmations hors guillemets contrôlées sur la page dite. Aucune écriture git, aucun accès réseau, aucune dépense, aucun chemin interdit ouvert, aucune recherche récursive, aucun refus de permission ou de classifieur rencontré.
- **Borne (R8)** : je n'ai relu que les pages nommées ci-dessous, par lignes filtrées ; aucun PDF lu en entier ; code d'EvoSCM, de BEYOND et de WAHL non lu. « Conforme » veut dire : conforme aux pièces à cette profondeur.

## 1. Rejeu des citations

Commande : `python3 -I docs/notes/lecture-o4-suite-v1/rejouer_citations_priorite_haute_o4_v2.py /home/user/controle-ia-travail docs/notes/lecture-o4-suite-v1/citations-priorite-haute-o4-v2.json <sortie hors dépôt>` (mon programme, inchangé ; la forme d'entrée de la liste v2 lui convient ; 15 secondes).

| mesure | résultat |
|---|---|
| citations de la liste v2 retrouvées sur la page dite, empreinte du PDF conforme | **69 sur 69** |
| au niveau strict (casse et ponctuation gardées) | 69 sur 69 |
| citation trouvée aussi sur une autre page | 0 |
| accord avec le résultat de l'auteur (mêmes 69 lignes, même ordre) | 69 sur 69 des deux côtés |
| passages en anglais entre guillemets dans la note, absents de la liste | 0 |
| citations de la liste absentes de la note | 4 (BEYOND p. 16, 26, 34 ; EVOSCM p. 1) |

## 2. Constats de la contre-lecture : traités ou non

Les 14 constats (le 6 en deux parties) ont chacun une ligne dans la section 5 de la v2, avec décision et citation ; 15 lignes sur 15. Fondements revérifiés sur la page :

- **1 (EvoSCM)** : p. 27 « uniform evidence weights », « precommitted predictions » ; p. 29 lignes 9-12 (seuil 0,20, « withheld from the planner ») ; p. 18 « Posterior odds: finite / vanishing », « 5.98 × 10^18 : 1 » ; p. 28 « before accepting the submission » ; p. 30 « stored before its outcome is observed » : tous présents. La nuance de C tient : la p. 29 dit que le seuil retire des arêtes au planificateur, non qu'il promeut une loi. « likelihood » : zéro occurrence dans les 34 pages.
- **2 (WAHL)** : P = voisin, accepté. Refus de « facteur de Bayes de substitution » **fondé** : p. 3, la phrase est sous « Probabilistic model inference » (travaux antérieurs) ; p. 8, section 4.5 « Posterior Analysis », aucune occurrence de « ratio » ni de « Bayes ». Je retire cette glose.
- **3, 4, 5 (BEYOND)** : p. 12, 16, 34, 35 conformes. La mise en garde de C sur 4 tient : p. 34 ne nomme pas τsig ; p. 13 et 16 nomment τsig et τecon sans valeur.
- **6a, 6b (NMV)** : p. 9 (« 5% level », six facteurs, 183 signaux), p. 10 conformes.
- **7 (ATLAS)** : « LLM » zéro ; « language model » une fois, p. 10. Conforme.
- **8 à 14** : traités ; 11 accepté et **non fait**, ce que la v2 dit (section 5 et résumé).
- Termes cherchés sur le texte entier des six PDF : résultat de C confirmé (ACES : « pre-processed » et « pre-processing » seulement).

## 3. Réserves (aucune ne change un statut de la table)

1. **Contrôle strict « 69 sur 69 » dit sans appui de l'auteur.** La v2 (en-tête et section 5, ligne 9) écrit que son contrôle strict hors dépôt donne 69 sur 69 ; le résumé de l'auteur dit 68 sur 68 avant l'ajout de la 69e citation (WAHL p. 2), contrôle non relancé. Le chiffre est vrai (mon rejeu : 69 strict), mais la v2 ne l'a pas mesuré. De même, l'heure du rejeu final (09:42:58Z selon le résumé) n'est pas dans la note, qui donne 09:40:58Z.
2. **« 69 passages entre guillemets »** : la note en cite 65 ; 4 citations de la liste n'y figurent pas (section 1).
3. **Demande du constat 1 remplie en partie.** Je demandais la lecture entière des p. 17-19 et 26-31 d'EvoSCM. Lues en entier : 18, 27, 28, 29 ; par lignes filtrées : 17, 30 ; non lues : 19, 26, 31. La section 2 de la v2 le montre, la section 5 ne le dit pas.
4. **Trois mots de plus que les pages, section 3.5 et table (iv-a), EvoSCM** : « par l'agent, dans un journal » (p. 5 « recorded », p. 30 « stored » : ni le support ni qui consigne ne sont dits ; p. 27 : le modèle de langue propose les prédictions, le programme choisit l'essai) ; « données simulées » (« simulator » p. 27 et 30, non vérifié pour les trois bancs) ; « avec baisse notable » sans chiffre (p. 17, table 11 : 75,09 % contre 63,47 %).
5. **NMV p. 10, « la page ne dit pas qui examine »** : un peu fort. La phrase a « we » pour sujet (« After reviewing these results […] we are left with ») ; ce que la page ne dit pas, c'est si l'examen est fait à la main ou par programme. Le retrait de « filtre humain » reste prudent et juste.
6. **Refus de « le plus proche »** (constats 1 et 2) : refus sans citation contraire, par abstention ; le classement est renvoyé à Lazar. Acceptable ; je note que ce n'est pas un refus « avec citation ».
7. **« EvoSCM et WAHL ajoutent des voisins que la note d'englobement n'a pas »** (section 6) : repris de ma contre-lecture, borné par ce que j'avais lu de cette note (sections 0 et 5) ; non revérifié ici.

## 4. Nœuds

Quatre nœuds (BEYOND, EvoSCM, WAHL, SSRN), chacun écrit comme une décision pour Lazar, sans conclusion. Le verdict « occupée en partie » n'est pas modifié ; rien n'est déclaré libre ; la ligne « conjonction » dit « non trouvée dans les six pièces lues », bornée par la section 2 et par le code non lu. Aucun identifiant de modèle dans les trois fichiers (recherche sur les trois fichiers nommés : zéro).

## 5. Ce que je n'ai pas fait

Pas de relecture entière d'une page au-delà des lignes filtrées ; la note d'englobement n'est pas rouverte ; les provenances (constat 11) ne sont pas recontrôlées ; SSRN 6569258, SSRN 6474601 et la version de la revue de Novy-Marx et Velikov restent non lus.
