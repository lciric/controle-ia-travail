# Prix de `gpt-6-astra` (Astra, OpenAI) — relevé v1 : **page officielle inaccessible, aucun prix lu**

Développeur neuf, sous-agent de la session mère, 14 novembre 2026 (heures relevées par `date -u`). Demande : lire le prix
d'entrée et de sortie de `gpt-6-astra` sur la page officielle d'OpenAI, avec l'adresse et la date ; si la page est
inaccessible, le dire et n'inventer aucun chiffre.

## Ce qui a été tenté

| Adresse | Outil | Quand | Résultat |
|---|---|---|---|
| `https://openai.com/api/pricing/` | WebFetch | 14 novembre 2026, peu avant 07:43:41 UTC | **échec** : `getaddrinfo ENOTFOUND openai.com` (hôte hors des domaines permis de la session) |
| `https://platform.openai.com/docs/pricing` | WebFetch | même moment | **échec** : `getaddrinfo ENOTFOUND platform.openai.com` (même cause) |

Les deux hôtes ne se résolvent pas depuis la session : ils sont hors des domaines réseau qu'elle autorise. Comme le dit
l'outil, je n'ai pas essayé d'autres sites, ni de moteur de recherche : un extrait de moteur n'est pas la page officielle,
et la règle R7 ne le rend pas opposable. **Aucun prix n'est donc lu.** Le dépôt l'avait déjà noté en octobre : les pages
d'OpenAI renvoient une page anti-robot de Cloudflare (`LISEZMOI-relais-kimi-v4.md`, § 5, point 2).

Pour mémoire, l'hôte de l'interface de programmation, `api.openai.com`, est joignable : une requête sans clé et sans
corps vers `GET https://api.openai.com/v1/models` a rendu `401` (14 novembre 2026, peu avant 07:43:41 UTC). Ce n'est pas un
appel payant, et cette route ne donne aucun prix.

## Ce que le dépôt contient déjà (non opposable, pour situer seulement)

- **Barème prudent 10 / 50 USD par million de jetons** (entrée / sortie) pour `gpt-6-astra`, marqué **« SUPPOSÉ »** :
  rapporté, jamais lu sur la page des tarifs. Sources : `docs/notes/ideation-organisme-v1/course-2/collisionneur-v8/collisionneur_v8.py`,
  table `MODELES["E"]` ; R-1049 (« Astra 10/50 supposé ») ; configuration du pilote v70, « barème prudent du collisionneur
  v8 (cout_pire_cas, « SUPPOSÉ ») ». **Ce n'est pas un prix** : `devis-lecture-astra-v1.md` ne l'emploie qu'à titre
  d'illustration, en le nommant ainsi.
- Un seul appel réel d'Astra relevé : R-1454 (4 novembre 2026), 9 949 jetons d'entrée, 3 199 de sortie, 0,25978 USD
  comptés **au barème du script** (10 / 50). Ce chiffre ne mesure pas le prix : le script appliquait son propre barème.
- Prix du cache (jetons d'entrée en cache) : rien dans le dépôt. Par défaut, l'outil v3 compte les jetons en cache **au
  prix d'entrée** (borne haute).

## Ce qu'il faut pour clore ce relevé (nœud)

L'une des deux voies, au choix de Lazar :

1. **Lazar lit lui-même** le tarif de `gpt-6-astra` (entrée, entrée en cache, sortie, en USD par million de jetons) sur
   la console ou sur la page des tarifs d'OpenAI, et le donne par écrit, avec la date ; la mère le consigne au registre et
   dans une version 2 de ce relevé ;
2. ou **ouvrir `openai.com` et `platform.openai.com`** dans les réglages réseau de la session (environnement), puis
   relire la page par WebFetch, en citant les passages exacts et en gardant une copie empreintée (R6, R7).

Tant que le prix n'est pas lu, l'outil v3 ne peut pas être préparé pour de bon : `preparer` exige `--prix-entree`,
`--prix-sortie` et `--source-prix`, sans valeur par défaut.
