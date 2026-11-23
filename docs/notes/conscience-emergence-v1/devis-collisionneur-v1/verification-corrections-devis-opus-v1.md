# Vérification des corrections du devis « conscience et émergence » (v1)

- Même vérificateur que `verification-devis-opus-v1.md` (`91d5d1a6…`) : Claude Opus 5.5, 2026-11-23. Aucun appel à un modèle externe ; seul le calcul du devis, qui ne touche pas au réseau, a été relancé.
- Pièce vérifiée : `devis-collisionneur-conscience-emergence-v2.md`, SHA-256 `93db3c537b4d6ceb…`. Son compagnon est conforme et c'est le même contenu qu'au commit `7f54f613`.
- **Objet servi : la v2 de la question**, `../test-neutralite-v1/texte-servi-question-neutre-v2.txt` (`db54b152…`, compagnon conforme, 1 107 mots). Une comparaison mot à mot avec la v1 ne montre que trois retouches, et rien d'autre :
  - le titre « Acquis d'un travail antérieur… » devient « Explications ordinaires déjà identifiées… » ;
  - « tiendra » devient « pourrait tenir » ;
  - la dernière phrase est rendue symétrique : « Toute conclusion, … ou non, … recevable ».

## Verdict

**À corriger**, pour deux retouches de pure forme :
- deux cases du tableau sont permutées ;
- la phrase attribuée à Lazar sur Opus est mal citée.

Le reste est juste. Les six défauts sont corrigés sur le fond et les chiffres v2 sont confirmés. La commande donne bien le devis annoncé, et la voie admet l'effort `max`. Une fois les deux retouches faites, le devis est bon à soumettre ; il n'y a pas besoin d'une nouvelle passe de calcul.

## Les chiffres v2

- **Relance du calcul sur la v2.** J'ai relancé `devis --fable --opus --argon --astra --carbon --neon --faits Q2 --question Q2`. Le code de sortie est 0, et la sortie est identique octet pour octet à `devis-moteur-v8m-six-especes-question-neutre-v2-v1.txt` (`12396988…`, compagnon conforme). Par rapport à la v1, une seule cellule bouge : Neon au tour 3 passe de 1,67 à 1,68 USD.
- **Total payant sans relance : 20,05 USD.** Le calcul exact donne 20,0467 USD. **Juste.** Le premier tour de Carbon et Neon fait 3,83 USD : **juste.**
- **Avec toutes les relances : 61,30 USD.** Je l'ai recalculé avec les fonctions du moteur (`cout_pire_cas` et `nombre_relances`).
  - Le calcul exact donne 61,29 USD (61,2894), et la somme des cases arrondies donne 61,30. **Juste.**
  - Les relances d'Astra, comptées à son plafond de relance de 32 000 jetons, valent 1,68, 2,10 et 2,27 USD au calcul exact (1,6809, 2,1009 et 2,2689). **Juste.**
- **Défaut neuf A : deux cases du tableau sont permutées.** Le tableau du devis met Argon à 1,92 et Neon à 1,67 au tour 3. La sortie brute donne Argon à 1,91 et Neon à 1,68. Le total du tour, 7,22, reste juste. La phrase entre parenthèses (« l'écart d'un centime … au tour 3 d'Argon ») doit dire « de Neon ».

## Les six défauts de la première vérification

1. **Pire cas avec toutes les relances : corrigé.** Le devis donne 61,30 USD avec la bonne règle.
2. **Commande de course : corrigée.**
   - La commande `vague_abonnement_v2.sh v8m DOSSIER Q2 GO-2026-11-23-19 max 40 --fable --opus --argon --astra --carbon --neon` correspond aux arguments du script, dans l'ordre moteur, dossier, question, accord, effort, plafond, puis les espèces.
   - Le script passe les mêmes espèces, avec `--faits Q2 --question Q2`, et sans `--sortie-max` ni `--effort-max`. C'est la composition du devis relancé, donc la commande donne bien le devis annoncé.
   - Elle donne aussi `--plafond-usd 40 --ligne-usd 40` et `GO_ID=GO-2026-11-23-19`.
   - La voie v6 admet bien `max` : `EFFORTS_SESSION = ("max", "xhigh", "high")`, et toute autre valeur est refusée.
3. **Espèces et effort : corrigé sur le fond, mais la citation est fausse (défaut neuf B).**
   - L'ajout d'Opus sans dépense est maintenant déclaré, et l'effort `max` est fixé pour Fable et Opus.
   - Mais le devis prête à Lazar les mots « demande à opus max aussi » et dit qu'il a demandé « opus max ». L'événement `e4fb2d53…`, que j'ai relu, porte en réalité « d'autre spropositons a eprouver opus ? demande a fable max aussi ». Lazar s'y adresse à Opus, la session elle-même, et demande Fable en effort maximal.
   - Les mots « opus 5.5 max aussi » se trouvent dans la ligne GO-2026-11-23-21, mais celle-ci porte sur une autre question : la demande reformulée des idées intéressantes, `230585b9…`.
   - Il faut citer exactement, ou citer GO-2026-11-23-21 comme analogue. L'ajout d'Opus reste à soumettre au mot de Lazar.
4. **Confirmation du plafond : corrigée dans la pièce.** L'événement, son heure et ses mots sont exacts. L'inscription au registre est bien demandée à la mère. Cela reste une condition de départ.
5. **Consultation de Carbon et Neon fondue dans le premier tour : corrigé.** C'est déclaré dans le texte et dans la ligne d'engagement.
6. **Compagnon du script et « 3,7 fois » : corrigé.**
   - Le compagnon `vague_abonnement_v2.sh.sha256` est écrit et conforme (`2f7c2ecb…`).
   - Note de forme : la v2 de la question compte 1 107 mots, pas « environ 1 090 ». Le rapport à la question précédente est donc de 3,8. Sans conséquence.

## La phrase « cellule de Fable refusée au-delà d'environ 37 USD dépensés avant le tour 3 »

Le sens est juste : la cellule de Fable serait refusée sans rien coûter, et rien ne serait dépensé au-delà du plafond. Mais le seuil et le moment sont imprécis, parce que les cellules Claude passent **deux** contrôles :

- **Quand la voie écrit le kit** (`garder_avant_kit`), le contrôle porte sur le plus grand des deux plafonds de Fable, soit 64 000 jetons. Le pire cas compté est alors de 3,87 USD au tour 3 (3,28 au tour 1, 3,70 au tour 2). Le kit est refusé si la dépense dépasse environ **36,1 USD**.
- **Quand le moteur lit la réponse recueillie**, à la vague suivante, il refait la garde dans `executer_cellule`, au premier plafond de 49 000 jetons, soit 3,12 USD. La réponse est alors refusée si la dépense dépasse environ **36,9 USD**. Or cette dépense comprend déjà les cellules payantes du même tour, parties à la première vague. Ce n'est donc pas « avant le tour 3 ».
- Opus est contrôlé de la même façon, à 1,55 USD au tour 3.

Je propose de remplacer la phrase par celle-ci : « refusée si la dépense dépasse environ 36 USD à l'écriture du kit, ou environ 37 USD à la lecture de la réponse, cellules payantes du même tour comprises ». Ce point ne bloque pas.

## Effort réellement servi aux cellules Claude

Je contrôle ici la note du vérificateur de l'autre dossier.

- L'effort servi à Fable et à Opus est l'argument d'effort du script. Il est écrit dans la fiche de chaque kit, et c'est à partir de cette fiche que la mère crée la session.
- Le moteur, lui, affiche « effort high » : c'est son réglage pour l'interface, qui ne sert pas sur la voie abonnement.
- **Réserve** : aucun programme ne contrôle que la session a vraiment tourné à cet effort.
  - `recueil_session_v6.py` contrôle le modèle servi, la fin de session et le texte servi, mais pas l'effort.
  - `recueillir` recopie l'effort de la fiche, et non celui de la session.
- La mère doit donc créer chaque session avec l'effort `max` et le vérifier dans les détails de la session, par l'effort qu'elle déclare. Elle consigne ce qu'elle a lu.
