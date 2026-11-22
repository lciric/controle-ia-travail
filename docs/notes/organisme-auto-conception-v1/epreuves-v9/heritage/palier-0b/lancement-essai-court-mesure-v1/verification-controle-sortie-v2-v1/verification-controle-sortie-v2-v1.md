# Vérification du contrôle de sortie v2 (v2 = 73046b31…, v1 = 8d88b263…, empreintes recalculées : conformes)

**Verdict : Conforme avec réserves.** Les trois corrections sont vues rouges sur artefact et vertes sur le cas sain ; aucun contournement trouvé dans le périmètre annoncé. Une réserve (R3, trou au banc) et une réserve de méthode.

## Table des cas
| # | Cas | Attendu | Rendu (v1 / v2) | Fichier |
|---|---|---|---|---|
| 1 | diff v1→v2 | seules R1, R2, R3, code 22, import zlib, ligne d'usage | conforme ; `grep build_opener|urlopen|Redirect|install_opener` sur v2 : aucune occurrence ; `ProxyHandler({})` gardé hors adresse officielle | sortie du diff (session) |
| 2 | 301, 302, 303 | v2 : 22, 1 requête | v1 : 0, **2 requêtes, jeton envoyé aussi à la cible** ; v2 : 22, 1 requête | tables/r1-cas.txt, journal-serveur.txt |
| 2 | 307, 308 | v2 : 22, 1 requête | v1 : 21 ; v2 : 22, 1 requête, jeton seulement sur la route d'origine | idem |
| 3 | gzip + 1 octet nul / 4 octets / seconde trame (vide, « x », zéros) / gzip tronqué | 14 | v1 : 0 ; v2 : 14 | tables/r2-cas.txt |
| 3 | tar + octet non nul ; octet non nul dans le remplissage (même longueur, juste après le dernier membre, dernier octet) | 14 | v1 : 0 ; v2 : 14 | idem |
| 3 | remplissage tronqué (1 bloc, jusqu'à fin+1024, sans remplissage, −1 octet), allongé (+1 octet, +1 bloc, +10 240) | 14 | v1 : 0 ; v2 : 14 | idem |
| 3 | sain identique ; sain recompressé autrement | 0 | 0 / 0 | idem |
| 4 | `--nom-jeton` sans `--adresse`, banc (à blanc et `--envoyer`) | 2, aucune requête | v1 : 0 et 20 ; v2 : 2 | tables/r3-cas.txt |
| 4 | `--nom-jeton` hors banc, avec ou sans adresse, avec `--envoyer`, avec HCLOUD_TOKEN | 2 | 2 / 2 | idem |
| 4 | banc, `--adresse` = URL officielle + `--nom-jeton` | (non annoncé) | v2 : 0 en à blanc ; admis | idem |
| 5 | corps v1 contre v2 (POST /ok, même données) | égaux | sha 0c2c85d3…fedbb des deux côtés | r1-cas.txt |
| 5 | jeton factice dans ps (envoi lent 2 s), stdout, stderr, relevé | absent | absent ; mot de passe et user_data factices expurgés | r1-cas.txt |

## Défauts et réserves
- **Réserve R3** : au banc, `--adresse https://api.hetzner.cloud/v1/servers --nom-jeton NOM` passe le contrôle R3 (l'adresse est « donnée »). Avec `--envoyer` et la variable posée, un jeton factice partirait vers l'API réelle. Jouée seulement à blanc (code 0), l'envoi n'a pas été joué (réseau interdit). Peu grave (banc, option explicite) ; correction : exiger que `--adresse` soit l'adresse locale quand `--nom-jeton` est donné.
- Les contrôles de taille (13) précèdent la charge (14) : la marge de taille des données saines est faible (~100 octets) ; mes variantes l'ont respectée. Un ajout plus gros donnerait 13 et non 14 (refus quand même).
- Corps sain testé sur un seul jeu de données de banc (fabricant v8, dépôt git factice local).

## Relevé de méthode
**Chaîne de raisonnement.**
1. Empreintes v1 et v2 recalculées (sha256sum) : celles annoncées.
2. Diff v1→v2 lu : seuls les changements annoncés ; `grep` : aucun `build_opener`/`urlopen`/gestionnaire de redirection résiduel (pas 1).
3. Données saines produites par le fabricant v8 (FABRICANT_BANC=oui, dépôt git local vide, jeton factice 33 signes) : code 0 (outils/00-preparer.sh).
4. Variantes de charge construites en décompressant le tar sain (81 920 octets, fin du dernier membre 78 336) puis en le modifiant (outils/cas_r2_r3.py) ; chaque variante jouée sur v1 et v2 : tables/r2-cas.txt.
5. Serveur factice local propre (outils/serveur.py), 5 codes de redirection, v1 et v2 : tables/r1-cas.txt, journal des requêtes avec empreinte du jeton, jamais le jeton.
6. R3 : 8 combinaisons d'options : tables/r3-cas.txt.
7. Égalité des corps : empreinte du corps reçu par le serveur, v1 et v2.

**Objets de contrôle.** Faux par construction : v1 sur chaque artefact (suit 301/302/303, accepte gzip+octets, accepte `--nom-jeton` seul) : attendu 0 ou succès, rendu comme attendu ; donc les artefacts sont bien « acceptables » pour v1 et les rejets de v2 sont dus aux corrections. Vrai par construction : données saines et recompressées : v2 rend 0, corps identique.

**Premier pas non justifié.** Pas 7 pour la généralité : un seul jeu de données saines ; le justifierait un second jeu (autre taille de remplissage de tar). Sinon aucun.

**Mode d'échec affecté.** Tenu pour R1, R2 ; tenu avec réserve pour R3 (voir ci-dessus). Preuves : tables/.

**Trouvaille de côté.** Aucune autre.

**Évaluateur et conseil.** Le juge est le code de sortie et le journal du serveur, écrits par moi, admis par v1 (rouge/vert croisé). Un bon résultat non mérité serait possible si mes variantes ne couvraient pas un ajout qui préserve l'égalité de longueur et la nullité du remplissage : non trouvé (la condition exige longueur exacte et zéros jusqu'à la fin).
