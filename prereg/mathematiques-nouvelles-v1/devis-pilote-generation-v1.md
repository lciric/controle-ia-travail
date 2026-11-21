# Devis — pilote « oracles plantés » du pilier des mathématiques nouvelles — v1

- **Statut** : devis par phase, **aucun GO demandé par ce texte** ; il accompagne le brouillon 1 du préenregistrement (`preenregistrement-pilote-generation-v1-brouillon.md`, même dossier) et le plan d'avancée (`docs/notes/mathematiques-nouvelles-v1/plan-d-avancee-mathematiques-nouvelles-v1.md`). Il deviendra un devis v2, contre-lu, quand les prix auront été relevés sur les pages publiques et les identifiants confirmés ; le GO se prend sur la v2.
- **Écrit par** : le concepteur du mandat de la mère (R-4388, agent 2 ; modèle servi `claude-fable-5-1`, mandat Fable 5.2, écart signalé), le 2026-11-21, 07:20 à 07:40 UTC (`date -u`). Aucun appel de modèle, aucun réseau, aucune dépense.
- **Source unique des chiffres** : `prereg/mathematiques-nouvelles-v1/calculs-v1/calculs_devis_pilote_generation_v1.py` (`ad1c85d3e45a6f10ace7529d4beef3dda38e053143118cfecdeaaeb823f2156d`), sortie `sortie-calculs-devis-pilote-generation-v1.txt` (`5d6175ddb25da9285b7eb2add8eec77612628baeaf48c7bf18245f6bccc92613`), lancée par `.venv/bin/python -I` ; les blocs cités sont ceux de la sortie. Tous les montants en USD.

## 1. Prix employés (par million de jetons, entrée / sortie) — **aucun vérifié sur une page publique à ce jour**

| modèle (rôle) | prix | source | statut |
|---|---|---|---|
| Opus 5.5 (proposeur, témoin, bras S et N) | 4 / 20 | référence locale `claude-api`, table « Current Models » cachée le 2026-11-03 | **non vérifié** |
| Gemini 4 Argon (proposeur ; reformulateur de repli) | 10 / 50 au devis (prudent) ; 2 / 10 jusqu'au 30 novembre et 4 / 20 dès le 1er décembre sur la page archivée `docs/sources/prix/page-prix-gemini-api-20261108T054611Z.html` (`ad2140dd…`) | `collisionneur_v8.py` l. 69-71 ; page archivée | lu sur page archivée ; le devis garde 10 / 50 ; sensibilité au § 5 |
| Kimi K3.1 Pro (relecteur de S, reformulateur des connus, juge de repli) | 2 / 10 | `collisionneur_v8.py` l. 73-74, « vérifiés le 30 octobre » | rapporté |
| GPT-6 Astra (juge de nouveauté) | 10 / 50 | `collisionneur_v8.py` l. 76-82, « SUPPOSÉS, barème volontairement haut » | supposé ; identifiant et accès à confirmer (nœud de compte) |
| machine à processeur (Hetzner ccx33) | 0,28 l'heure (0,22692 EUR) | `registres/depenses.md` l. 422 (observé le 12 novembre) | observé ; borne haute du programme 1,30 l'heure (brouillon 3 de l'essai Lean, § 4.3) |

Cache non compté (prudent) ; le raisonnement des modèles est facturé comme sortie et compté comme tel ; profils de jetons SUPPOSÉS (script, bloc 2 et constantes), à remplacer par la mesure du pilote.

## 2. Devis par phase (bloc 2 ; bas / attendu / pire)

| phase | contenu | bas | attendu | pire |
|---|---|---|---|---|
| **P0 construction** (sans appel) | générateur de mondes, grammaire, bac à sable, tests de mort exacts, normaliseur, clés scellées, essais R5, rejeu complet de la batterie sur la banque plantée ; harnais d'appels ; script d'analyse | 0 | 0 | 0 |
| **P1 banque de connus plantés** | 40 reformulations par Kimi (6 k / 3 k attendu) ; 60 jugements (8 k / 4 k attendu) : juge Kimi au bas, Astra à l'attendu et au pire | 3,04 | 18,48 | 47,04 |
| **P2 proposeurs** | 12 mondes × 24 propositions × 2 configurations = 576 propositions ; profil attendu 10 k / 3 k par proposition (S-02 de la note du pilier) ; bas : appel groupé 3 k / 1,5 k, Argon à 2 / 10 ; pire 20 k / 12 k | 21,17 | 79,20 | 253,44 |
| **P3 bras « suite bon marché » (S)** | 150 énoncés ; agent Opus 5.5 à outil Python en bac isolé (40 k / 6 k attendu, plafond 1,50 par énoncé) + relecteur Kimi | 23,40 | 46,20 | 190,80 |
| **P3 bras « lecture nue » (N)** | 150 énoncés ; un appel Opus 5.5 sans outil (4 k / 6 k attendu) | 7,80 | 20,40 | 74,40 |
| **total des appels** | | **55,41** | **164,28** | **565,68** |
| **P4 machine** | processeur seul : génération, bac, tests de mort, analyse ; 12 / 24 / 48 heures ; 0,28 l'heure, pire à 1,30 | 3,36 | 6,72 | 62,40 |
| **total appels + machine** | | **58,77** | **171,00** | **628,08** |

Lignes conditionnelles (bloc 3, à l'attendu) : banque de connus refaite une fois (reformulations reconnaissables à leur forme, audit de symétrie) 18,48 ; un monde régénéré et rejoué (générateur défaillant sur un monde) 12,15 ; **attendu avec lignes conditionnelles 194,91**.

## 3. Plafonds proposés et règles de coupure (bloc 3)

- **Plafond d'appels proposé : 300 USD** = arrondi à la dizaine de (attendu avec lignes conditionnelles × 1,5 + réserve des appels en vol 7,04). La coupure A6 du préenregistrement joue dès que la dépense dépasse le plafond moins la réserve ; le pire cas sous plafonds par item (565,68) ne peut donc pas être atteint : la course s'arrête tronquée, par blocs de mondes complets (les deux configurations sur chaque monde), et se lit en description si moins de 8 mondes sont complets.
- **Plafond machine proposé : 65 USD** = 48 heures à la borne haute de 1,30 ; minuterie de destruction par identifiant à 48 heures (R10, A9) ; à 0,28 l'heure, 48 heures coûtent 13,44.
- **Somme des plafonds : 365 USD.** Ce n'est pas un attendu : l'attendu est 171 ; le bas 59.

## 4. Machine et environnement

Une machine à processeur, louée (Hetzner ccx33 observée à 0,28 USD l'heure) ou conteneur sans accès au dépôt ni aux clés : le bac exécute du code écrit par un modèle (outil Python de S) et le code du générateur ; cloison du brouillon 3, § 4.5 (sans clé, sans dépôt, réseau sortant coupé avant tout code de modèle, dossier neuf par item, chaîne en lecture seule) ; le harnais qui porte les clés tourne hors du bac. Aucune carte graphique. Disque : les mondes et les clés tiennent en quelques dizaines de mégaoctets (ordre de grandeur, non mesuré).

## 5. Sensibilité (bloc 4, total des appels à l'attendu)

| prix d'Argon | juge Kimi | juge Astra |
|---|---|---|
| 2 / 10 (page archivée, jusqu'au 30 novembre) | 122,04 | 135,48 |
| 4 / 20 (page archivée, dès le 1er décembre) | 129,24 | 142,68 |
| 10 / 50 (prudent, retenu) | 150,84 | 164,28 |

Le poste qui pèse le plus est le profil des proposeurs (P2 : 79 attendu, 253 au pire) ; le second est le plafond par énoncé du bras S.

## 6. Relecture humaine et temps des agents (bloc 8)

- **Lazar** : 1,5 à 6 heures (attendu 3) : tirage de 20 propositions vivantes, étiquettes du juge, lecture du verdict.
- **Agents** (hors devis d'interface ; la question « le temps des sous-agents est-il une dépense ? » reste ouverte, brouillon 3, § 8, point 6) : code et vérification 23 à 37 heures ; préenregistrement et contre-lecture 6 à 10 ; harnais 6 à 10 ; course 24 à 36 heures murales ; lecture et verdict 4 à 8.

## 7. Hors devis

L'outillage Lean (GO-2026-11-10-13, 65 USD, 0,56 dépensés, échéance 30 novembre) ; le pilote « preuve formelle contre suite bon marché » (D-1b : plafond 578 + 35 proposé au brouillon 3, ligne de GO neuve à part) ; le pilote 2 (attaque B4, bras Lean) ; toute lecture d'antériorité ; un mathématicien extérieur (contact externe, nœud).

## 8. À vérifier avant tout GO (devis v2)

1. Prix d'Opus 5.5, de Kimi K3.1 Pro, de Gemini 4 Argon et de GPT-6 Astra sur les pages publiques, avec la date du relevé (« À REMPLIR : PRIX-VÉRIFIÉS » du préenregistrement) ; identifiant et accès d'Astra, ou repli R1 fixé avant le scellement.
2. Profils de jetons des proposeurs et du bras S : un essai à blanc sur un monde témoin (dans le plafond, après GO) ou une mesure sur les journaux des courses passées de l'organisme (sans lecture de contenu).
3. Prix et disponibilité de la machine ; cloison éprouvée (R5).
4. Que le harnais compte les jetons par appel et vérifie l'identifiant servi (A2).
5. Le plafond d'appels retenu par Lazar (300 proposé ; 200 si la course est réduite à 8 mondes ; 400 si Lazar veut les deux configurations à 36 propositions par monde) : « À REMPLIR : PLAFOND-GO ».
