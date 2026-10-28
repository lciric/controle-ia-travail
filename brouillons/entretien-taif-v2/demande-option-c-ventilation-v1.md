# La demande à l'entretien — option (c) ventilée — v1

Lignée conv-audit, instance du 28 octobre 2026 (modèle servant déclaré par l'environnement : Fable 5.1 ; auteur désigné du
travail principal : Opus 4.6, décision de Lazar). Écrit à partir du relevé `date -u` de **10:31:47 UTC le 28 octobre 2026**.

**Décision de Lazar** (28 octobre, 11:28 heure de Paris) : **option (c), « go »** — la demande reste celle qui a été envoyée, et
l'on **nomme et chiffre une extension** que l'agenda mérite si le fonds veut aller là. Il a joint la version envoyée. Cette
ventilation est **soumise avant envoi** ; rien ne part sans son mot.

**Ce que la version envoyée dit** (proposition v2 du 7 octobre, `737c482c…` ; formulaire `76cdbb3b…` ; budget v3
`037765b0…`) : demande **58 630 USD** pour sept mois (1er décembre 2026 → 30 juin 2027), fourchette **28 160** (quatre mois,
papier C seul) à **138 600** (douze mois, ajoute le papier B). Corrige mes versions antérieures, qui citaient les scénarios du
dépôt (41 800 / 91 740 / 146 300) et supposaient 60 000 : **le chiffre qui compte est 58 630**, et la fourchette envoyée monte
déjà à 138 600, ce qui laisse la place à une extension sans contredire l'échange.

---

## 1. Principe

- **La base ne bouge pas** : 58 630 USD, lignes inchangées (allocation 35 000 ; carte graphique 4 000 ; outillage des agents
  7 000 ; validation humaine 4 000 ; déplacement 2 500 ; divers 800 ; réserve 10 % 5 330). Elle finance les fronts A (théorie),
  B (mesures à coût nul), D (papiers C et A) et la porte G0 — exactement ce que la proposition envoyée promet.
- **L'extension est nommée, chiffrée, séparable** : elle finance ce qui s'est ajouté depuis le 7 octobre (le front C gouverné et
  la théorie des moniteurs) et ne vit que si le fonds le veut. Elle reste **sous le scénario ambitieux déjà envoyé** (138 600),
  qu'elle ne remplace pas : le papier B reste dans ce scénario-là.
- **Chaque ligne porte son hypothèse de calcul**, pour que Lazar la corrige d'un chiffre.

## 2. L'extension « sécurité et théorie des moniteurs » (USD, sept mois, mêmes dates)

| ligne | montant | hypothèse de calcul |
|---|---|---|
| E1 — Revue de sécurité externe des sorties adversariales | **7 500** | deux revues (avant toute exécution de l'adversaire scellé ; avant publication des sorties au niveau méthode) ; ≈ 5 jours d'un évaluateur indépendant à ≈ 1 500 USD/jour ; fourchette 5 000–12 000, **taux à fixer par Lazar** |
| E2 — Adversaire scellé, exécution sous revue | **4 000** | carte graphique ≈ 1 500 (organismes de l'étage 3 et leur évaluation, réserve de détecteurs jamais déployés) ; appels de modèles ≈ 2 500 (le collisionneur multi-modèles a coûté ≈ 180 USD en quatre jours en octobre) |
| E3 — Matrice « statistique × classe d'écart » complète et vérification formelle | **6 000** | consultant en statistique ≈ 40 heures (ligne déjà chiffrée 4 000 dans le scénario ambitieux envoyé) + outillage des agents pour la formalisation (Lean) 2 000 |
| E4 — Réplication : seconde famille de modèles et organismes de 70 milliards de paramètres | **6 000** | carte graphique vers la ligne ambitieuse envoyée (12 000) ; ici la moitié de l'écart, pour la réplication seule, sans le papier B |
| E5 — Validation humaine supplémentaire (vérité terrain des modes, mode tenu à l'écart compris) | **1 500** | ≈ 30 heures à 50 USD |
| Sous-total | **25 000** | |
| Réserve 10 %, déclarée | **2 500** | même règle que la base |
| **Extension** | **27 500** | |
| **Base + extension** | **86 130** | sous les 138 600 envoyés |

**Variante avec du temps** : l'extension ajoute du travail dans les mêmes sept mois. Si le fonds préfère, **E6 — deux mois
d'allocation supplémentaires** (10 000 + réserve 1 000) portent le total à **97 130** et le terme au 31 août 2027. À proposer
seulement si l'interlocuteur demande « et le temps ? ».

## 3. Comment le dire (anglais, une fois)

> The request stands at 58,630 dollars for seven months, as submitted. Since then the programme has grown a part it did not
> have on the seventh of October: a theory of what monitors cannot see, and a governed adversarial track with an external
> security review. If the fund wants that part, it is a named extension of about 27,500 dollars — external review, the sealed
> adversary run under that review, the full statistic-by-deviation-class matrix with formal verification, and a replication on a
> second model family — which keeps the total under the ambitious scenario already on file. It is separable: the base delivers
> what the proposal promises without it.

## 4. Ce que cela change ailleurs

- **Programme d'entretien** : la section « demande » et le point 3 de « ce qui reste à Lazar » se réécrivent avec 58 630 /
  28 160 / 138 600 (v4, en cours).
- **Chiffre de calcul** : la proposition envoyée dit « about $20 » de calcul au 7 octobre et 602 tests ; au 28 octobre, ≈ 450 USD
  connus (carte graphique sous GO ≈ 95, dont phase 0 stricte ≈ 70 ; appels de modèles ≈ 353, surtout pilotes de l'organisme
  ≈ 156 et collisionneur ≈ 180) et ≈ 900 tests. À dire ainsi : *the preregistered instrument work ran under about a hundred
  dollars of GPU; the whole programme, idea-collider rounds and organism pilots included, is a few hundred dollars to date.*
  Note de réconciliation de session-depot : `docs/notes/depenses-cumul-2026-10-28-v1.md` (`93969946…`, sur `main`).
- **Calendrier** : la proposition envoyée place **GC fin du mois 2 et G1 fin du mois 4** ; le programme v2 interne dit « G1 et
  GC en fin de M2 ». C'est la version envoyée qui fait foi devant le fonds ; l'écart interne est signalé à Lazar (modifier le
  programme est son geste).

## 5. Réserves

1. Les montants E1 à E5 sont **mes ordres de grandeur**, pas des devis ; E1 dépend d'un taux que Lazar fixe.
2. Le fonds peut financer la base seule : l'extension est écrite pour que cela ne coûte rien à la cohérence.
3. La variante E6 n'est pas recommandée d'emblée (elle touche l'allocation, le poste le plus visible).
4. Rien n'est envoyé par moi.

## 6. Ce que Lazar tranche

1. Le taux et le nombre de jours de la revue externe (E1).
2. Garder ou retirer E4 (réplication) de l'extension — c'est la ligne la plus proche du scénario ambitieux déjà envoyé.
3. Proposer ou non la variante E6.
