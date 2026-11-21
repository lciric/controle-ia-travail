VERSION DE PYTHON : `python3 --version` (3.13) ; essais sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider` ; AUCUN `-c`.

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`.

# Mandat du développeur — véhicule NA-1, lots 1 et 2 (tirage ; garde de motifs) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21. **Ne part qu'au « Conforme » du contrôle de la conception v4 et au mot de la mère** (08:00Z : « Les mandats de code peuvent se préparer dans l'ordre du chemin critique, à lancer dès le « conforme » »). Code écrit par un développeur O, vérifié ensuite par un vérificateur S. **Aucun appel à un fournisseur, aucune dépense, aucune clé ; essais sur données factices seules.**

## Qui

Un développeur neuf (modèle O), qui n'a écrit ni la conception, ni le relevé du lot 0, ni aucun orchestrateur. Tu signes « développeur des lots 1 et 2 du véhicule NA-1, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- **La conception v4** : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/conception-vehicule-v4/conception-vehicule-course-nouvelles-attaques-v4.md` (empreinte à son compagnon), en particulier § 0 bis (décisions de la mère), § 2.1 (tirage), § 5.2 (identifiants, règle d'encodage en cinq points, épreuve dans les deux sens), § 6.1 et § 6.2 (épreuves), § 7 (lots 1 et 2 : contenu, dépendances, arrêts éprouvés). **Le texte de la conception, avec ses décisions et son contrôle, fait foi ; ce mandat ne le remplace pas.**
- **Le contrôle de la v4** (dossier `conception-vehicule-v4/controle-v1/`, quand il est versé) : ce qu'il demande de plus pour les lots 1 et 2.
- **La v9 scellée** (`prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v9.md` sur `origin/main`), son additif 1 v5 et le complément de valeurs v3 avec son additif : règle des graines (R9, `numpy.random.SeedSequence`, clés gelées), tirage des cases, clés n° 30 et n° 40, arrêt n° 10 (premier temps), arrêt n° 16 (motif interdit), ligne de case.
- **Le relevé du lot 0** (`docs/notes/ideation-nouvelles-attaques-v1/lot-0-vehicule-na-v1/releve-lot-0-vehicule-na-v1.md`, `10ac79ec…`) pour ce qui touche le tirage et les identifiants du noyau (identifiant de fiche du noyau, Q6).
- **La base** : le paquet v68 et sa manière (paquet, manifeste, programme d'application ; `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/`, sur `origin/main` au commit de versement), et l'orchestrateur en lecture seule (`/home/user/lciric/ideation-organism`, `a41b7b50…`).

## Ce que tu écris (fichiers neufs seulement)

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lots-1-2/`.

1. **Lot 1, module `tirage`** (nom de la série NA-1, suffixe `_na_v1`) : cases ; clés 0, 1, 2, 3, 30 et 40, les deux dernières tirées au même geste et consignées ; identifiants de case ; réserve ; C1 ; ligne de case et son contrôle ; **identifiants neutres réencodés sans suite hexadécimale** selon la règle du § 5.2 (alphabet, ordre des octets, base 60 à longueur fixe, 18 et 14 lettres, décodage qui refuse), même tirage. Essais : arrêt n° 10 (premier temps), ligne de case, tirage rejoué deux fois égal à l'octet, clés n° 30 (aucune case de sabotage : rien n'est tiré) et n° 40 (mot refusé), encodage aller et retour sur toutes les valeurs d'un échantillon tiré, refus d'une chaîne hors alphabet, absence de toute suite de huit chiffres hexadécimaux dans un identifiant encodé.
2. **Lot 2, module `garde_motifs`** : programme, format de la liste des motifs, témoins positifs. **La liste réelle des motifs n'est pas à toi** (rédaction du modèle F, en parallèle) : tu écris contre une **liste d'essai** factice de deux familles, au format que tu fixes et que la conception permet. Essais : arrêt n° 16 par famille sur la liste d'essai, cas sain et artefact (R5) ; une requête assemblée qui passe ; une qui porte un motif refusée au dernier point avant l'envoi ; aucun octet changé après la garde (l'empreinte journalisée est celle de ce que la garde a lu).
3. Pour chaque lot : **mutations** (pour chaque garde, la garde retirée fait échouer son essai), à la manière de la v68.
4. **`rapport-developpeur-lots-1-et-2-na-v1.md`** : ce que la conception exige (citation, paragraphe), comment le code le fait (fichier:ligne), les essais et leur nombre, les mutations, ce que la lettre ne fixe pas (en remarque, jamais tranché), et l'interface que les lots 3 et 5 recevront.
5. Une table d'empreintes du dossier ; un compagnon pour chaque fichier (`env -C DOSSIER sha256sum F`, redirigé par `>` vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ni de matière première ouverte. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle dans tes sorties. Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
