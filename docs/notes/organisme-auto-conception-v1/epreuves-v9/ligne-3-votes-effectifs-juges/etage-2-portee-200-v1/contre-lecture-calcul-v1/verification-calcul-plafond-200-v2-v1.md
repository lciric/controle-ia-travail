# Vérification de la correction du calcul du plafond à 200 (ligne 3), version 2 — v1

Contre-lecteur, modèle S (le même que pour la contre-lecture `contre-lecture-calcul-plafond-200-v1.md`, 9adbe32d…), mêmes interdits, aucun appel payant, aucune écriture dans le dépôt.

## Verdict : Conforme

## Ce que j'ai vérifié

- Empreintes des pièces versées, égales à celles annoncées : programme v2 `86440df6…`, sortie v2 `fe58be3a…`, essais v2 `10672098…`, rapport v2 `a893f3fa…` ; le différentiel `b8be019c…` est le seul fichier dont l'empreinte n'était pas annoncée.
- Programme v2 rejoué deux fois (`python3 -I -B`, depuis la racine du dépôt) : deux sorties d'empreinte `fe58be3a790ee28db3fadb6370251a69c4378dc887e977a19ab77fd9093eb3e2`, égales entre elles et à la sortie versée, à l'octet.
- Essais v2 rejoués sur une copie (programme et essais copiés dans mon dossier, devis lu au chemin du dépôt) : 20 passés.
- Différentiel rejoué : sortie d'empreinte `6dc90ba69b5b5928a55a0b398cc0b20c33f07647a318f158499fce0e822cbaea`, égale à celle annoncée ; 2 feuilles différentes, `regle_du_compteur.texte` et `version`. Je l'ai recoupé par un `diff` de texte entre les deux sorties : deux lignes seulement (711 et 713). Le `diff` des deux programmes ne montre que la docstring, la constante `VERSION`, la constante `TEXTE_REFUS`, la concaténation du texte de la règle et le message d'usage : aucune ligne de calcul n'a bougé.
- Texte, mot pour mot : le texte de la sortie contient « un envoi refusé (refusé, coupé par un délai, en erreur) est compté 0,60 USD puis rejoué une fois, avec succès, à son coût ; un envoi revenu sans coût lisible est compté 0,60 USD et n'est pas rejoué (texte l. 193) ; le modèle des refus ne joue que la première forme », identique à celui que j'ai proposé. La docstring le porte de même, avec des retours à la ligne seulement.

## Version qui suit le nom (R12)

J'accepte. La clé `version` suit le nom du fichier, comme en version 1 ; le nom est neuf, la version 1 est gardée sans modification. Elle est l'une des deux seules feuilles qui diffèrent, et rien d'autre ne bouge dans la sortie.

## Remarque

Les essais v2 lisent le devis v7 au chemin du dépôt, comme demandé, et tournent sans le bloc-notes du développeur ; ma remarque de la v1 sur leur dépendance est donc levée. Le différentiel, lui, lit ses deux sorties dans le bloc-notes du développeur (chemin fixé en tête de fichier) ; je l'ai rejoué tel quel, la copie existe encore. À noter si on le scelle.

Contre-lecteur, modèle S.
