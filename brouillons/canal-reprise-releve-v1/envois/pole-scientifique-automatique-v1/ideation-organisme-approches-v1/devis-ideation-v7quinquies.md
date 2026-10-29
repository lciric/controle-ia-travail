# Course d'idéation de l'organisme — devis v7 quinquies (Argon 11,6 ; relecture CL6 ; tentatives de contrôle)

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` **02:11 UTC**. **Remplace le devis
v7 quater** (gardé, R12) ; le reste des v2 à v7 quater vaut. Code : **v40** (363 essais ; relecture ciblée v39 → v40 chez
session-depot avant tout lancement).

1. **Plafonds** (décisions de Lazar : « ok 49 » puis « Argon à 11,6 ») : Claude **40** (0,4 de contrôles + 2 × (5 + 9,3) + 4 + 7
   = 40,0) ; Argon **11,6** (contrôle à taille réelle ≤ 2,5 + 2 × 2,5 + juge 3,5 + contrôle du bras 0,2 = 11,2, marge 0,4) ;
   **total 51,6**. Le cœur refuse au départ toute somme de plafonds au-dessus des totaux (CL37-03, CL39-01) ; le lanceur
   refuse si le relais (plafond − réserve − dépense déjà faite) ne peut pas servir la dernière session (CL39-03).
2. **Tentatives de contrôle** (CL39-02) : un contrôle refusé (Claude ou Argon) est scellé dans `SORTIE-controle/tentative-N.json`
   avec son coût (plafond compté si le coût est inconnu) ; la relance dans la même SORTIE impute ce coût aux totaux ;
   **trois tentatives au plus**, puis un mot de Lazar. Le contrôle d'Argon se fait sur la **plus grosse consigne** qu'il
   recevra (pièces + matériau attesté + marge de fiches, ≈ 1,1 million de caractères avec la liste v4 en seconde passe) :
   son plafond de 2,5 est à confirmer au barème d'Argon par session-depot.
3. **Interruption** (CL39-04, 05) : SIGINT, SIGTERM, SIGHUP arrêtent proprement (Argon et son groupe tués, session comptée au
   plafond, manifeste de fin) ; un bras interrompu **après envoi** est verrouillé : pas de relance sans un mot de Lazar.
4. **Ordre de lancement** inchangé (v7 quater, point 4) avec, avant la course : `sha256sum -c EMPREINTES-…-v40.txt`, relais
   `--plafond-usd 40 --reserve-par-appel 4` relancé à neuf (dépense 0) à chaque tentative, `--budget-externe-usd 11.6`
   (défaut), `--delai-session-s 3600 --delai-commande-s 1800` (défauts), liste v4 et `--taille-max-pieces 750000` (défaut).
