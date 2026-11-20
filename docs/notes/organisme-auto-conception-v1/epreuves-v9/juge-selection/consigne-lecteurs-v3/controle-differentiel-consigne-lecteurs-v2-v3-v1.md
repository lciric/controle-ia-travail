# Contrôle du différentiel v2 → v3 de la consigne des lecteurs du rejeu — v1

- **Contre-lecteur, modèle O** : le même que pour `d9f5ff4c…` et `e5c21791…`. Écrit le 2026-11-20 (`date -u` : 2026-11-20T05:48:31Z). Processeur seul, aucune dépense, aucun appel de modèle. Rien n'est écrit dans le dépôt.
- **Pièces**, dossier `consigne-lecteurs-v3/`, toutes égales à leur compagnon : la consigne v3 (`85efbd70fc7b1e78d897218711ab834b680b6500ce939436d103e7eaf25fa011`), `remplacements-consigne-lecteurs-v2-v3-v1.json`, le journal, le différentiel et le rapport.
- **Mandat** : `consigne-lecteurs-v2/mandat-redacteur-consigne-lecteurs-rejeu-v3-v1.md` (`1607797a…`), égal à son compagnon.

## Verdict

**Conforme.** La condition de remise est remplie : la garde nommée existe sur `main`, avec l'empreinte citée.

## 1. Rejeu de l'outil

J'ai rejoué `remplacer_texte_exact_v1.py` (`391db990…`, recalculé) sur une copie de la v2 (`1e5479be…`) avec une copie du fichier de remplacements. Il fait 4 remplacements et rend **`85efbd70…`**, égale à l'octet à la v3 versée. Le différentiel ne porte que ces quatre changements : le titre, la ligne « Version 3 » et les deux retouches du § 4.

## 2. Les retouches du § 4

- « le programme d'assemblage ne voit pas » : c'est ma retouche facultative, mot pour mot.
- **La garde nommée existe.** J'ai lu `origin/main:docs/notes/organisme-auto-conception-v9-mere/juge-selection-manifeste-v1/garde_lignee_reconnue_v2.py` après `fetch`, redirigé vers mon dossier.
  - Son empreinte est **`635e9160e0bf03cd70a25cd0532e638203c8bc621c502313e5f2491b4ba76585`**, égale à son compagnon sur `main` et à la consigne.
  - Son en-tête et sa constante `AUCUNE` disent ce que la phrase annonce : elle refuse une `lignee_reconnue` qui n'est ni une clé de `familles` ni « aucune ». Elle le fait dans les cartes comme dans le veto. Elle ne lit que le manifeste et la lecture.

## 3. Les deux points du rédacteur

- **Le chemin de la garde est donné au lecteur.** Pas de correction. Le § 8 lui interdit déjà d'ouvrir autre chose que les cartes servies, les critères et la consigne. La garde ne porte d'ailleurs aucune information sur une carte. Le chemin et l'empreinte disent seulement qu'elle existe.
- **Les deux autres « le programme » du § 4** (« Le programme ne compare que la famille » ; « Le programme compte, après coup… ») disent vrai du programme d'assemblage, commande `gardes`, l. 1071 et 1067-1081. Pas de correction.

## 4. Lu, et incidents

- Lus : le différentiel, le journal, et l'en-tête de la garde, par une recherche bornée sur ma copie.
- Mes copies sont dans `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-juge-v4/controle-consigne-v3/`.
- Aucune carte, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`, une commande simple par appel.
- **Aucun refus** de permission, de classifieur ni de garde.

*contre-lecteur, modèle O*
