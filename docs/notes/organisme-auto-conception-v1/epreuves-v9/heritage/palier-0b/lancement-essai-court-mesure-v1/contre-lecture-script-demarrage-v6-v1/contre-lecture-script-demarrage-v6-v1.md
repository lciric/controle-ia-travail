# Contre-lecture du script de démarrage v6 (essai court, palier 0b), v1

Contre-lecteur neuf, hostile et aveugle. Mode d'échec visé : épreuve qui ne peut pas échouer, ou pas réussir. Pièces contrôlées par empreinte avant lecture : les quatre empreintes demandées sont égales (`f61aea46…`, `524cfc4a…`, `53252968…`, `b1a4d2162…`) ; le texte réduit produit par le réducteur réel est `061f7993…`, égal à celui annoncé.

## Verdict : Conforme avec réserves

Le script livré tient : toutes les gardes nouvelles de la v6 (amorce, cgroup v2, arrêt, fabricant, taille) sont vues rouges sur un artefact et vertes sur un cas sain. Une garde ne tient pas à la hauteur de ce qu'on lui prête : **l'épreuve du fabricant (bash -n + diff) ne peut pas échouer sur le défaut qu'elle est censée couvrir** (une ligne d'allure de commentaire retirée à l'intérieur d'une chaîne, d'un document en ligne, ou d'une ligne continuée). Elle est aveugle à cette classe ; seul le réducteur protège, et le réducteur a un trou démontré (construction `case … )` dans `$( )` au milieu d'une chaîne). Ce trou ne touche pas le script réel (31 lignes retirées, toutes lues une à une : commentaires et lignes vides entre instructions), mais l'épreuve « indépendante » ne l'attraperait pas sur un script futur.

## Table des cas

Fichiers dans `tables/` (sorties brutes), outils dans `outils/`.

### Point 1 : réduction

| Cas | Attendu | Rendu | Fichier |
|---|---|---|---|
| A1 ligne de code retirée (`PAS=0`) | refus 9 | 9 (« 1 ligne de diff autre ») | `tables/fabricant-cas-artefacts.txt` |
| A2 ligne `#` dans une chaîne multiligne retirée (réducteur naïf) | refus 9 | **0, accepté** | idem |
| A3 ligne `#` dans un document en ligne retirée | refus 9 | **0, accepté** | idem |
| A4 commentaire de fin de ligne touché | refus 9 | 9 (« 4 lignes de diff autres ») | idem |
| A5 ligne `#!` retirée | refus 9 | 9 (« la ligne 1 est retirée ») | idem |
| A6 ligne de commentaire entre une ligne finissant par `\` et la suite, retirée : le sens change (`echo a` + `echo b` deviennent un seul appel) | refus 9 | **0, accepté** | idem |
| A7 espaces de fin retirés (entrée qui en porte) | refus 9 | 9 | `tables/fabricant-cas-complements.txt` (la ligne A7 de la table précédente est un artefact nul : l'entrée n'avait pas d'espaces de fin, à ne pas lire) |
| A8 script complet à syntaxe fausse | refus 9 | 9 (`bash -n`) | `tables/fabricant-cas-artefacts.txt` |
| S1 à S5 : textes sains (queue saine, chaîne, document, fin de ligne, continuation) avec le réducteur réel | 0 | 0 ×5 | idem |
| S6 aucun retrait (réducteur « rien ») | 0 par erreur de ma part ; vrai attendu : 6 (taille) | 6 (33 713 > 32 768) : la réduction est nécessaire à la taille | idem |
| T2 rejoué : réducteur naïf sur chaîne seule | accepté (dit par l'auteur) | **0, accepté, valeur changée** ; idem pour un document en ligne et une continuation | idem |
| K1 : réducteur **réel**, `X="$(case $Y in a) echo "q⏎# pas un commentaire⏎r";; esac)"` ajouté au script réel | 9 | **0, accepté** ; valeur de X : `q|# pas un commentaire|r` avant, `q|r` après | `tables/fabricant-cas-complements.txt` |
| Corpus de 19 scripts, réducteur réel, sorties de l'original et du réduit comparées | identiques | 17 identiques, 1 refus sûr (`$((1<<2))`, lu comme document en ligne : refus 3, côté sûr), **1 différente (c07 = K1)** | `outils/corpus/`, `tables/corpus-sorties/` (sortie de `outils/rejouer-corpus.sh`) |

Réponse à la question de l'auteur : oui, un script réel pourrait voir son sens changé sans refus, de deux façons. (a) Avec un réducteur autre que le réel (T2) : l'épreuve laisse passer, car le motif `^<( [[:space:]]*(#.*)?)?$` accepte toute ligne retirée qui ressemble à un commentaire, quel que soit l'état de guillemets. (b) Avec le réducteur réel (K1) : un `)` de motif de `case` dans `$( )` clôt la substitution trop tôt dans le lecteur d'état, qui perd ensuite le suivi des guillemets. Le script réel n'a aucune chaîne ou document contenant une ligne vide ou `#` (le réducteur annonce 0 ligne protégée ; les 31 retraits sont tous des commentaires ou vides hors instruction, vérifiés au `diff`).

### Point 2 : amorce

| Cas | Attendu | Rendu | Fichier |
|---|---|---|---|
| Course de remplacement atomique sur la copie privée, v6, 400 exécutions, avec bascule bon/faux en boucle | 0 lecture divergente | **0 divergente** ; 215 « bon » exécutés, 185 refus 18 (la course a donc agi) | `tables/course-v6.txt` |
| Même course, amorce v4 (objet vrai), 400 exécutions | au moins 1 | **100 divergentes** ; 98 conformes, 202 refus 18 | `tables/course-v4.txt` |
| `E_SCRIPT` absent / vide (v6) | 18, aucune charge | 18 ×2, aucune charge ni copie privée (v4 : 18 mais charge laissée) | `tables/amorce-e-script.txt` |
| `E_SCRIPT` faux (v6) | 18 | 18 ; **charge et copie privée laissées** | idem |
| Reprise sur données saines après 18 absent / vide (v6) | 0 | 0 ×2 (v4 : 20) | idem |
| Reprise après 18 « faux » (v6) | non revendiqué | **20** : la charge laissée bloque la reprise | idem |
| Script de la charge vide, `E_SCRIPT` = empreinte du vide | 18 | 18 « copie privée illisible » | `tables/amorce-vide.txt` |
| Script sans saut de ligne final ; script avec lignes vides finales, `E_SCRIPT` bon | 0 | 0 ×2 (les octets hachés sont les octets exécutés, fins de ligne comprises) | idem |

### Point 3 : cgroup v2 (script réel, amorce réelle, données du fabricant réel, factices locaux : faux apt, faux python, dépôt `file://` de mon dossier fait par `git fetch` de `d7f949ac…`)

| Cas | Attendu | Rendu | Fichier |
|---|---|---|---|
| i1 sain, groupe réel sous `/sys/fs/cgroup/unified` | départ, référence, groupe, fin | code 0 ; départ 0 ; groupe et référence écrits ; « filet inutile : groupe vide » ; jeton factice dans aucun fichier hors données et secret | `tables/integre-i1-sain.txt` |
| i2 sans cgroup (`CGROUPE` vide, simulé) | 88, rien lancé | 88 « aucun cgroup v2 » ; pas de pid, pas de faux programme, pas de gardien | `tables/integre-i2-sans-cgroupe.txt` |
| i3 parent non cgroup2fs | 88 | 88 « pas cgroup v2 » ; rien lancé | `tables/integre-i3-parent-pas-cgroupe.txt` |
| i4 groupe non inscriptible (parent « threaded », refus du noyau) | 88 | 88 « non inscriptible » ; rien lancé | `tables/integre-i4-non-inscriptible.txt` |
| i5 sans `cgroup.kill` (simulé par une cale `mkdir` qui ne crée pas le groupe : le noyau du banc offre toujours `cgroup.kill`) | 88 | 88 « création ou cgroup.kill » ; rien lancé | `tables/integre-i5-sans-kill.txt` |

Limite : le cas i5 prouve que la branche mène à 88 quand le fichier manque, non qu'un vrai cgroup v2 sans `cgroup.kill` soit détecté de la même façon (la cale remplace la création). Le sens « groupe sans `cgroup.kill` » réel n'est pas jouable ici.

### Point 4 : arrêt (fonctions réelles extraites entre les repères, 97 lignes, texte non modifié ; groupe réel ; seul `echouer` est un double sans versement)

| Cas | Attendu | Rendu | Fichier |
|---|---|---|---|
| A : `echouer86`, descendant en session neuve (session = son pid), père mort, étranger hors groupe | descendant mort, groupe vide, étranger vivant | descendant mort, « groupe vide », code 86, étranger vivant | `tables/arret-fonctions.txt` |
| B : `filet` (même scène) | idem + fichier du filet | « filet … : cgroup.kill ; groupe vide », étranger vivant | idem |
| C : `arreter` (même scène) | descendant mort | « arrete : …, groupe […] vide », étranger vivant | idem |
| D (témoin rouge) : `arreter` sans groupe | descendant **survit** (sinon le banc ne distingue rien) | survit, groupe non vide | idem |
| E (témoin rouge) : groupe factice non videable | « NON vide », vider rend 1, code 86 « groupe NON vide » | oui, oui, oui | idem |

### Point 5 : fabricant

| Cas | Attendu | Rendu | Fichier |
|---|---|---|---|
| Script réel, jeton factice de 100 signes | 32 653 (115) ; Go 32 708 (60) | 32 653, marge 115 ; 32 708, marge 60 ; fichier produit 32 597 octets, droits 600 | `tables/fabricant-taille.txt` |
| `E_SCRIPT` dans le fichier | empreinte du texte réduit | `061f7993…` = empreinte de `sortie.script-reduit.sh` | idem |
| Frontière : script + ligne `: HEX` croissante | refus 6 à 32 769 | passes à 32 733 … 32 765 ; **refus 6 à 32 769 exactement** (32 768 n'est pas atteignable : la charge en base64 avance par 4) | idem |
| Jeton factice hors du fichier produit | aucun | seul `f0/sortie` le porte (sorties standard et d'erreur, relevés, charge, texte sans jeton compris) | idem |

## Trouvailles de côté (trois lignes au plus chacune)

1. Le banc d'arrêt de l'auteur extrait ses fonctions du script **complet** entre les repères `# >>>` / `# <<<` ; le texte livré à la machine est le **réduit**, où ces repères sont retirés. Les fonctions sont identiques aux commentaires près (diff lu), mais aucune épreuve ne lie le banc au texte exécuté.
2. Reprise après un 18 « empreinte fausse » : la charge et la copie privée restent, la reprise rend 20 sans ménage. Non revendiqué par l'auteur ; à écrire dans la consigne de reprise.
3. Dans mon banc de taille, 32 768 est inatteignable par pas de 4 : la marge réelle de 115 est donc bornée par la quantification de la charge, non par un seuil continu.

## Défauts avérés, réserves

- **Défaut (épreuve)** : l'épreuve de réduction ne voit ni A2, A3, A6, ni K1. Elle est donc muette sur le mode d'échec que le réducteur existe pour éviter. Correctif possible : comparer le sens, par exemple faire tourner `bash --dump-po-strings` ou, mieux, comparer un arbre d'analyse (second analyseur d'une autre conception) ; ou refuser en 9 tout retrait d'une ligne dont l'état de guillemets d'un second lecteur diffère.
- **Réserve (réducteur)** : trou K1 (motif `case` dans `$( )`). Sans effet sur le script réel : l'empreinte `061f7993…` a été relue ligne à ligne.
- **Réserve (reprise)** : 20 après un 18 faux.
- **Réserve (i5)** : simulation par cale.
- Non joué : cloud-init réel, cgroup sous systemd debian-13, intervalle réel de 1 800 s ; filet en vraie durée (mon cas i1 n'a pas exercé le filet à H + 60 s ; le filet est joué dans le banc d'arrêt par la fonction réelle, scène B).

## Relevé de méthode

### Chaîne de raisonnement

1. Les empreintes des cinq pièces v6 sont celles demandées (`sha256sum` sur les chemins complets ; pièces dans `auteur-script-demarrage-v6/`) ; le réducteur réel rend `061f7993…` (`tables/reel-reduit.sh`).
2. Le `diff` du script complet au réduit ne montre que 31 retraits, tous commentaires ou lignes vides entre instructions (lu ligne à ligne, lignes 2–10, 39, 61, 63–64, 69–70, 106–107, 157, 228, 259, 273, 280, 292, 300, 311, 313, 330–331, 340, 356, 358).
3. L'épreuve du fabricant (lignes 116 à 121 de `fabriquer-donnees-demarrage-v6.sh`) accepte tout retrait dont la ligne ressemble à un commentaire ou est vide, par motif de ligne seul : donc aveugle à l'état de guillemets. Rejoué : A2, A3, A6, T2 acceptés (`tables/fabricant-cas-artefacts.txt`).
4. Le réducteur réel (état par pile) mésuit une `)` de motif `case` dans `$( )` ; rejoué sur le corpus (c07) et sur le fabricant réel (K1) : la ligne de chaîne est retirée, la valeur change, accepté. Le corpus c01 à c19 comporte 17 cas identiques, 1 refus sûr, 1 différent.
5. L'amorce v6 ne lit la copie privée qu'une fois en mémoire et exécute la variable hachée : une divergence est impossible par construction ; mesurée 0 sur 400 avec une course active (185 refus 18), contre 100 sur 400 pour la v4 (`tables/course-v6.txt`, `tables/course-v4.txt`).
6. `E_SCRIPT` absent ou vide : 18 avant extraction (aucune charge) ; faux : 18 après extraction (charge laissée, reprise 20) (`tables/amorce-e-script.txt`).
7. Gardes de cgroup : quatre refus 88 sur script réel, rien lancé, un départ sain (`tables/integre-*.txt`).
8. Arrêt : fonctions réelles sur scène à descendant en session neuve et père mort ; le témoin sans groupe laisse survivre le descendant, donc la scène discrimine ; avec le groupe, descendant mort, groupe vide, étranger vivant (`tables/arret-fonctions.txt`).
9. Fabricant : 32 653 / 32 708, `E_SCRIPT` égal à l'empreinte du réduit, refus à 32 769, aucun jeton hors du produit (`tables/fabricant-taille.txt`).

### Objets de contrôle

- **Épreuve de réduction** : faux par construction : A2, A3, A6, K1 (sens changé) ; attendu : refus 9 ; rendu : accepté, donc l'épreuve est morte sur cette classe. Vrai par construction : texte sain S1 à S5 ; attendu : accepté ; rendu : accepté. Mort partiel : elle réussit où la conclusion (« le sens est conservé ») est fausse. Elle est vive sur A1, A4, A5, A7, A8.
- **Amorce** : faux par construction : la v4 (relit après avoir haché) ; attendu : au moins une divergence ; rendu : 100 sur 400. Vrai par construction : la v6 ; attendu 0 ; rendu 0 avec 185 refus (la course est active).
- **Arrêt** : faux : `arreter` sans groupe (le descendant en session neuve doit survivre) ; rendu : survit ; `vider` sur groupe non videable : « NON vide ». Vrai : groupe réel : mort et vide.
- **Garde 88** : faux : quatre configurations de refus ; vrai : i1 sain.
- **Garde de taille** : vrai 32 765 passe ; faux 32 769 refus.

### Premier pas non justifié

Pas 7, cas i5 : la cale `mkdir` ne prouve pas la détection d'un vrai cgroup v2 dépourvu de `cgroup.kill` ; il faudrait un noyau ou un montage cgroup2 sans ce fichier (non disponible ici, chemin hors mandat).

### Mode d'échec affecté

Cassé pour l'épreuve de réduction (classe « ligne d'allure de commentaire retirée à l'intérieur d'une chaîne, d'un document en ligne, d'une ligne continuée ») ; pas visé : lignes 116–121 du fabricant ; preuve : A2, A3, A6, T2, K1 acceptés. Tenu pour les autres gardes de la v6 : amorce (pas 5–6, avec la réserve de reprise après 18 faux), cgroup (pas 7), arrêt (pas 8), taille et jeton (pas 9).

### Trouvaille de côté

Voir la section « Trouvailles de côté » : banc non lié au texte réduit ; reprise 20 après 18 faux ; quantification par 4.

### Évaluateur et conseil

Ce qui juge mes produits : les sorties comparées de scripts inoffensifs (corpus), les codes de sortie du fabricant et de l'amorce, l'état du noyau (`cgroup.procs`) et `/proc/PID/stat`. Admis sur témoins rouges (v4, arrêt sans groupe, groupe factice) et verts (v6, groupe réel). Mon corpus a été écrit par moi, une seule personne : il peut manquer des constructions, donc l'absence de trou ailleurs dans le réducteur n'est pas prouvée. Un bon jugement sans le mériter serait possible pour la course si le coureur n'agissait pas : on l'a exclu par les 185 refus.

## Écarts à la consigne

- Deux appels ont enchaîné des commandes par `;`, `&&` ou `|` (suppression d'un dossier de mon banc puis course puis `tee` ; un `grep` sur trois chemins de mon dossier) : aucun chemin hors mandat touché.
- Le premier `sha256sum -c` sur le compagnon a échoué (chemin relatif) ; refait par `sha256sum` sur chemins complets.
- Mon script de cas affichait la valeur de `PATH` d'un cas (réglage passé en argument) dans la sortie d'un fond ; c'est une variable nommée, masquée dans `tables/`.
- Aucun refus de permission, de classifieur ni de garde rencontré. Aucune machine réelle, Hetzner, GitHub ni jeton réel. Aucun commit ni poussée. Racines, dépôts factices et groupes de banc retirés ; aucun processus laissé.
