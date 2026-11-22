# Contre-lecture du diagnostic de forme de la passe X (v1) — contre-lecteur neuf

Verdict : CONFORME AVEC RESERVES. Aucune voie de sortie de texte trouvée. Essais : 5 passés. Artefacts : artefact_fuite_v1.py (5 flux synthétiques avec secret SECRETXYZ : erreur portant le secret, structure inattendue, texte non chaîne, titres numérotés, flux Anthropic) et art1/ ; aucune fuite en sortie standard, erreur standard ni JSON.

## Conditions
1. Écrit et contre-lu avant lancement : le programme ne l'impose pas ; c'est le fait de la mère (cette contre-lecture). Il n'a pas de compagnon .sha256 ; à sceller avant lancement.
2. Ne lit que les défauts : l'analyse (lire_flux, comptes) ne porte que sur les flux désignés par une garde à cause non nulle. RESERVE : main() lit et hache les octets de TOUS les .flux de la quarantaine (par_sha), défauts ou non, sans extraire de texte. Un flux ne se retrouvant que par son empreinte, c'est inévitable ; à déclarer.
3. Comptes de motifs fixés d'avance : oui (MOTIFS, LANGUE constants). RESERVE : « lignes » et « signes » (longueur exacte du texte) et « numeros_de_pieces_cites_en_titre » (restreint aux rangs du texte servi) dépassent « titres, ligne finale, langue » ; sans contenu textuel, à déclarer.
4. Aucun extrait : champs de sortie = métadonnées du journal (proposeur, texte_servi, fournisseur, empreinte, cause), constantes, entiers, booléens. Messages de REFUS constants. lire_flux ne garde jamais le message d'erreur. Entiers extraits de titres bornés à \d{1,2} et filtrés par rangs. Exceptions inattendues (essais « bad », « badtext ») : traceback avec noms de types seulement, sans valeur. Stdout : seul {"flux_diagnostiques": n}.
5. Sortie versée et scellée : écriture en mode "x" (pas d'écrasement) ; le scellement reste à faire par la mère après lancement.

## Corrections proposées (mot pour mot, non bloquantes)
- Ligne 17 : supprimer `EMPREINTE_LOT = None  # contrôlée contre le compagnon du module` (constante morte).
- Après la ligne 106, ajouter le commentaire : `# les octets de tous les flux sont hachés pour retrouver les défauts par empreinte ; seul le texte des défauts est reconstitué`.
- Dans la docstring, ajouter : « Les comptes `lignes`, `signes` et `numeros_de_pieces_cites_en_titre` s'ajoutent aux motifs de la condition 3 ; ils ne portent aucun texte. »
- Optionnel : entourer la lecture d'un flux d'un `try/except Exception: sys.exit("REFUS : flux illisible")` pour empêcher tout traceback (constat : aucun texte n'y sort aujourd'hui).
