# Vérification — préenregistrement court v6 de la course « nouvelles attaques » — v1

- Contre-lecteur neuf, modèle O. Je suis le même contre-lecteur que pour la contre-lecture de la v4 (`539c4854…`) et la vérification de la v5 (`508ebfde…`). Je n'ai écrit ni la v6 ni son jeu de remplacements. Règle R2. Écrit le 2026-11-20 ; relevé de `date -u` : 10:46:30Z, avant l'écriture.
- Demande : message de la session de l'organisme, sur le versement du commit `bda24906`. Mêmes interdits que mon mandat (`01f9e057…`).
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit. **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

**Conforme, à sceller.** C1 à C3 sont portées mot pour mot. C4 porte la lettre de la mère, mot pour mot. Les deux blancs ont disparu. Le reste n'est que de la tenue, et elle est juste. Aucun total, seuil, arrêt ni décision ne change.

## 1. Empreintes (égales au compagnon)

Dossier P6 = `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v6/`.

| pièce | empreinte |
|---|---|
| P6/`preenregistrement-court-course-nouvelles-attaques-v6.md` | `7e240c8c9b059171e06b416d5cf8b14c6822978f84219ad2d9770a32f90f11c5` |
| P6/`remplacements-preenregistrement-court-v5-v6-v1.json` | `1656f3b9fd0dcd00208f76b5d067ae7ba028de50ed5187d1f024082ad030a77b` |
| P6/ journal de l'outil | OK |
| P6/`differentiel-preenregistrement-court-v5-v6-v1.diff` | `529e084c88fbd4db25a46041f90575299c04be1e6b68030a031afbb6579440f3` |
| P6/`sortie-validateur-preenregistrement-court-v6-v1.txt` | `97feea71db866b617ccb545a923012e1320c55d3b823af205fd5badec678376c` |
| P6/`rapport-redacteur-preenregistrement-court-v6-v1.md` | `3ae121f78aab38dee045e1b422b2a419e0cfe9901a4ab69e58b2dbc44f574756` |
| pièces citées par la v6 : ma vérification de la v5, au chemin `preenregistrement-court-v5/verification-v1/` ; le mandat du rédacteur de la v6 | `508ebfde…` ; `9409a47a…` |

J'ai tiré du journal et du rapport du rédacteur les noms des pièces versées, sans commande de liste.

## 2. Rejeu et comparaisons

- Outil (`391db990…`) sur la v5 (`b2bb980a…`) avec le jeu versé : « FAIT : 8 remplacement(s) », sortie `7e240c8c…`. `cmp` avec la v6 versée : égal.
- Le différentiel refait ne diffère du différentiel versé que par la ligne 2 (chemin et heure).
- Le programme `comparer_jeux_v6_v1.py`, à côté de ce rapport, n'écrit rien. Il rend :
  - mes C1, C2 et C3 (`corrections-preenregistrement-court-v5-v1.json`, `5a02055a…`) figurent à l'identique dans le jeu versé ;
  - la lettre de la mère pour C4, recopiée de la demande dans `verification-v6/c4-lettre-de-la-mere.txt`, y figure comme « neuf », mot pour mot ;
  - cinq objets s'y ajoutent : C4 et quatre remplacements de tenue (titre, deux pour le statut, phrase de version).
- `grep -c -F -e "(à écrire par la mère)"` et `grep -c -F -e "(empreinte du rapport)"` sur la v6 rendent **0** et **0**.
- Le validateur, rejoué sur la v6, rend « problemes : aucun », comme la sortie versée. Les deux comptes à 0 montrent que ce « aucun » vaut ici « complet ».

## 3. La tenue

- **La phrase ajoutée à la phrase de version** : « Par C1, « devis v3 » dans ce texte, hors la citation de GO-2026-11-20-34, renvoie au devis v4 (`620de369…`) ; la phrase de version de la v5 qui dit ces renvois non récrits vaut pour la v5 seule. » Elle est **juste et utile**. Sans elle, la phrase de version de la v5, gardée telle quelle, dirait de la v6 que les renvois ne sont pas récrits, ce qui est devenu faux par C1. Elle ne tranche rien et redit C1. Sans suite.
- **La ligne de date non retouchée** : acceptable. L'usage n'est pas constant : la v3 n'avait pas ajouté de relevé « Version 3 ». La phrase de version de la v6 le déclare. Sans suite.
- **Le statut** dit que la v6 « reste à vérifier par le même contre-lecteur ». Une fois scellé, ce membre de phrase sera dépassé, comme « non scellée ». C'est l'usage déjà suivi au scellement de la v3, où R-4125 cite le contrôle qui manquait au texte. Je ne demande pas de correction. **À la mère** : citer cette vérification à la ligne de scellement du registre.
- Le titre (« v6 ») et « tant que la v6 ne l'est pas » sont justes.

## 4. Ce qui reste, hors de ce texte

Les points renvoyés à la mère par la contre-lecture restent entiers :
- la manière de relire le solde de Rigaud et les lots de R-4170 (valeur ouverte écrite par K3) ;
- l'ordre de course v3, qui dit encore cinq espèces ;
- R-4179 ;
- l'option d'un plafond de 0,05 USD pour la sonde de l'espèce 6, à porter à Lazar avec le devis v4.

## 5. Écarts

1. J'ai tiré du journal de l'outil et du rapport du rédacteur les noms des pièces versées.
2. J'ai écrit la lettre de la mère pour C4 dans un fichier de travail, pour la comparer par programme : `verification-v6/c4-lettre-de-la-mere.txt`. Mes essais restent dans le sous-dossier `verification-v6/`.

— contre-lecteur neuf, modèle O
