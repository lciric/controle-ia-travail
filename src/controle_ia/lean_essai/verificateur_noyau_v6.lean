/-
Vérificateur du noyau du harnais — essai Lean, D-1a, v6 (R-2464, sous le mandat « réparer d'abord » de R-2439).

Copie de la v5 (`verificateur_noyau_v5.lean`, inchangée, R12) ; un seul changement : les options d'impression posent
`pp.mathlib.binderPredicates` à faux (option de Mathlib, `Mathlib/Util/PPOptions.lean` l. 24, Mathlib `56a00585…`). Avec
elle à vrai (défaut), Mathlib imprime `∀ x < 0, 0 < x → …` sans le type de `x` (`Mathlib/Util/Delaborators.lean`) ;
réélaboré, ce texte se relit sur `ℕ` et l'aller-retour refusait l'artefact de vacuité (attendu « accepté »). À faux,
l'énoncé s'imprime `∀ (x : ℝ), x < 0 → 0 < x → x ^ 2 < 0`, hypothèses visibles pour le relecteur (G-L5).
Usage (par le harnais seulement) : `lean --run verificateur_noyau_v6.lean ITEM.olean M NONCE`.

Texte de la v5 : Vérificateur du noyau du harnais — essai Lean, D-1a, v5 (réparation R-2439 : la v4 ne compile pas sous Lean 4.35.0, R-2438).

Même conception et même sortie que la v4 (`verificateur_noyau_v4.lean`, inchangée, R12) ; texte de la v4 ci-dessous. La v5 ne
change que ce qu'exige la chaîne épinglée (Lean 4.35.0, commit `eb6cafb7…` ; Mathlib `56a00585…`) pour compiler sans message
et rendre sur l'item sain les mêmes faits que la v4 était censée rendre. Chaque changement renvoie aux sources de la chaîne
(`src/lean/` de la chaîne `leanprover/lean4:v4.35.0`, chemin et ligne) :
1. `axiomesDe` : `CollectAxioms.collect` est privé et prend un argument de plus (`Lean/Util/CollectAxioms.lean` l. 37-39) ;
   l'interface publique est `Lean.collectAxioms` (même fichier, l. 149), appelée dans une monade d'état sur l'environnement.
2. `Options.setNat` n'existe plus ; `Options.set` (`Lean/Data/Options.lean` l. 68) avec l'instance `KVMap.Value Nat`
   (`Lean/Data/KVMap.lean` l. 244).
3. `enableInitializersExecution` est `unsafe` (`Lean/ImportingFlag.lean` l. 31) : appelé par le terme `unsafe`, comme le fait
   Lean lui-même (`Lean/Elab/Frontend.lean` l. 333).
4. `importModules … (loadExts := true)` : sous 4.35.0 les extensions des modules importés (notations, délaborateurs,
   instances de Mathlib) ne sont chargées que sur demande (`Lean/Environment.lean` l. 2426-2440) ; sans elles, l'énoncé
   imprimé perd ses notations et l'aller-retour échoue sur l'item sain. C'était le comportement de `importModules` que la
   v4 supposait (note 1 : « le code de ses délaborateurs y est »).
5. Rejeu : `Environment.replay` est déprécié (`Lean/Replay.lean` l. 194-197 ; l'avertissement sortirait sur la sortie standard
   et ferait échouer G-L7) ; le rejeu par le noyau est `Kernel.Environment.replay` (l. 176), appelé tel quel, et décide seul
   de la ligne `rejeu` (G-L8). L'ancien `Environment.replay` rendait `Environment.ofKernelEnv` du résultat, environnement
   **sans contexte de réalisation des imports** (`Lean/Environment.lean` l. 643-644) où toute élaboration échoue
   (`realizeConst`, l. 2649-2652) : l'environnement d'impression et d'aller-retour est donc celui des imports, augmenté des
   constantes du module **acceptées par ce rejeu** (mêmes `ConstantInfo`, dans l'ordre de leurs dépendances, par
   `Environment.addDeclCore` l. 699, sans second contrôle ; non sûres et partielles exclues comme au rejeu, `Lean/Replay.lean`
   l. 179-182). Les axiomes se lisent sur cet environnement.
6. Imports (CLC3-03) : sous 4.35.0 tout en-tête sans `prelude` déclare `Init` deux fois, ordinaire et `meta`
   (`Lean/Elab/Import.lean` l. 33-35). `permis` exige l'en-tête **exact** que produit `import Mathlib` (trois imports, drapeaux
   compris) ; `modules` rend les noms distincts (`Init`, `Mathlib` pour l'item sain), comparés par `gardes_lean_v4.py`.
Le nom de l'espace `VerificateurNoyauV4` et le message d'usage sont gardés (aucun changement hors de ces six points).
Usage (par le harnais seulement) : `lean --run verificateur_noyau_v5.lean ITEM.olean M NONCE`.

Texte de la v4 :
Vérificateur du noyau du harnais — essai Lean, D-1a, v4 (contre-lecture courte de la v3 `b6ca886d…`, décision R-2307).

Même conception que la v3 (`verificateur_noyau_v3.lean`, inchangée, R12) : lancé par le harnais après la compilation, dans un
processus distinct, sans jamais importer le module de l'agent ; lecture de `Item.olean` comme des données ; rejeu de chaque
déclaration par le noyau ; axiomes ; énoncés imprimés par le harnais sans extension de l'agent ; aller-retour.

v4 :
- note 1 : plus d'`import Mathlib` dans le vérificateur (l'environnement de rejeu importe Mathlib à l'exécution ; le code de ses
  délaborateurs y est) ;
- CLC3-03 : imports du module **exactement** `Init` et `Mathlib` (un module `prelude` sans import est refusé) ;
- CLC3-02 : impression avec `pp.maxSteps` levé, `pp.deepTerms` et `pp.proofs` vrais ; sont rapportés et refusés par le harnais :
  `⋯` dans le texte (troncature), métavariable dans le terme réélaboré (trou), tout message émis par l'élaboration ; erreurs
  levées au lieu d'être remplacées par `sorry` (`withoutErrToSorry`) ;
- CLC3-06 : pour chaque énoncé attendu, liste des constantes **du module de l'agent** qu'il cite.
Sortie : lignes JSON, dernière `{"type":"fin","nonce":…}`. **Non compilé ici** : premier pas de l'épreuve sur la machine.
Usage (par le harnais seulement) : `lean --run verificateur_noyau_v4.lean ITEM.olean M NONCE`.
-/
import Lean
import Lean.Replay

open Lean Meta Elab

namespace VerificateurNoyauV4

def emettre (paires : List (String × Json)) : IO Unit :=
  IO.println (Json.mkObj paires).compress

def genre : ConstantInfo → String
  | .thmInfo _ => "theoreme"
  | .defnInfo _ => "definition"
  | .axiomInfo _ => "axiome"
  | .opaqueInfo _ => "opaque"
  | .inductInfo _ => "inductif"
  | .ctorInfo _ => "constructeur"
  | .recInfo _ => "recurseur"
  | .quotInfo _ => "quotient"

def surete : ConstantInfo → String
  | .defnInfo v =>
    match v.safety with
    | .safe => "sure"
    | .unsafe => "non-sure"
    | .partial => "partielle"
  | ci => if ci.isUnsafe then "non-sure" else "sure"

def axiomesDe (env : Environment) (n : Name) : Array Name :=
  let _ : MonadEnv (StateM Environment) := { getEnv := get, modifyEnv := modify }
  Id.run ((collectAxioms n : StateM Environment (Array Name)).run' env)

def contexte : Core.Context := { fileName := "<harnais>", fileMap := default }

/-- Options d'impression fixées (CLC3-02) : aucune troncature volontaire. -/
def optionsImpression (o : Options) : Options :=
  (((o.set `pp.maxSteps (100000000 : Nat)).setBool `pp.deepTerms true).setBool `pp.proofs true).setBool `pp.oneline false |>.setBool `pp.mathlib.binderPredicates false

structure Rendu where
  texte : String
  explicite : String
  egal : Bool
  tronque : Bool
  metavariables : Bool
  messages : Nat
  raison : String

def enonceEtAllerRetour (ty : Expr) : MetaM Rendu := do
  let texte := toString (← withOptions optionsImpression (ppExpr ty))
  let explicite := toString (← withOptions (fun o => (optionsImpression o).setBool `pp.all true) (ppExpr ty))
  let tronque := texte.contains '⋯' || explicite.contains '⋯'
  let avant := (← getThe Core.State).messages.toList.length
  match Parser.runParserCategory (← getEnv) `term texte with
  | .error e => return ⟨texte, explicite, false, tronque, false, 0, "analyse du texte imprimé : " ++ e⟩
  | .ok stx =>
    try
      let e ← Term.TermElabM.run' do
        let e ← Term.withoutErrToSorry (Term.elabTerm stx none)
        Term.synthesizeSyntheticMVarsNoPostponing
        instantiateMVars e
      let apres := (← getThe Core.State).messages.toList.length
      let trous := e.hasMVar || e.hasLevelMVar
      let egal ← if trous then pure false else withReducible (isDefEq e ty)
      let raison := if egal then "" else "le texte imprimé, réélaboré, ne redonne pas le type vérifié"
      return ⟨texte, explicite, egal, tronque, trous, apres - avant, raison⟩
    catch ex =>
      return ⟨texte, explicite, false, tronque, false, 0, "élaboration du texte imprimé : " ++ (← ex.toMessageData.toString)⟩

/-- v5, point 5 : ajoute à l'environnement `(env, vus)` la constante `n` du module (et d'abord ses dépendances du module),
telle que le rejeu du noyau l'a acceptée ; un bloc inductif entier à la fois ; constructeurs et récurseurs viennent avec lui. -/
partial def ajouterAcceptee (nouvelles : Std.HashMap Name ConstantInfo) (n : Name) :
    StateT (Environment × NameSet) (Except Kernel.Exception) Unit := do
  let some ci := nouvelles.get? n | return
  if (← get).2.contains n || (← get).1.contains n || ci.isUnsafe || ci.isPartial then return
  let ajouterDecl (d : Declaration) : StateT (Environment × NameSet) (Except Kernel.Exception) Unit := do
    let (e, vus) ← get
    set ((← (e.addDeclCore 0 0 d none (doCheck := false) : Except Kernel.Exception Environment)), vus)
  match ci with
  | .ctorInfo v => ajouterAcceptee nouvelles v.induct
  | .recInfo v => for i in v.all do ajouterAcceptee nouvelles i
  | .quotInfo _ => pure ()
  | .inductInfo v =>
    let membres := v.all.filterMap nouvelles.get?
    let ctors := membres.map fun m => m.inductiveVal!.ctors.filterMap nouvelles.get?
    modify fun (e, vus) => (e, (v.all ++ (ctors.flatten.map (·.name))).foldl NameSet.insert vus)
    for c in membres ++ ctors.flatten do
      for d in c.getUsedConstantsAsSet do ajouterAcceptee nouvelles d
    let types := (membres.zip ctors).map fun (m, cs) =>
      ({ name := m.name, type := m.type, ctors := cs.map fun c => { name := c.name, type := c.type } } : InductiveType)
    ajouterDecl (.inductDecl v.levelParams v.numParams types false)
  | _ =>
    modify fun (e, vus) => (e, vus.insert n)
    for d in ci.getUsedConstantsAsSet do ajouterAcceptee nouvelles d
    match ci with
    | .defnInfo v => ajouterDecl (.defnDecl v)
    | .thmInfo v => ajouterDecl (.thmDecl v)
    | .axiomInfo v => ajouterDecl (.axiomDecl v)
    | .opaqueInfo v => ajouterDecl (.opaqueDecl v)
    | _ => pure ()

def principal (chemin : System.FilePath) (m : Nat) (nonce : String) : IO UInt32 := do
  let (donnees, _region) ← readModuleData chemin
  let imports := (donnees.imports.map (·.module)).toList.eraseDups.toArray
  let permis := donnees.imports == #[{ module := `Init }, { module := `Init, isMeta := true }, { module := `Mathlib }]
  emettre [("type", toJson "imports"), ("modules", toJson (imports.map toString)), ("permis", toJson permis)]
  if !permis then
    emettre [("type", toJson "fin"), ("nonce", toJson nonce)]
    return 0
  unsafe enableInitializersExecution  -- pour Init et Mathlib seulement ; le module de l'agent n'est jamais importé
  let env ← importModules donnees.imports {} (loadExts := true)
  let mut nouvelles : Std.HashMap Name ConstantInfo := {}
  for i in [0:donnees.constNames.size] do
    nouvelles := nouvelles.insert donnees.constNames[i]! donnees.constants[i]!
  for (n, ci) in nouvelles.toList do
    emettre [("type", toJson "constante"), ("nom", toJson n.toString), ("genre", toJson (genre ci)),
             ("surete", toJson (surete ci))]
  let rejoue ← try
      let _ ← env.toKernelEnv.replay nouvelles
      let e ← match ((nouvelles.toList.forM fun (n, _) => ajouterAcceptee nouvelles n).run (env, {})) with
        | .ok (_, (e, _)) => pure e
        | .error ex => throw (IO.userError s!"ajout des constantes rejouées : {← (ex.toMessageData {}).toString}")
      emettre [("type", toJson "rejeu"), ("ok", toJson true)]
      pure (some e)
    catch ex =>
      emettre [("type", toJson "rejeu"), ("ok", toJson false), ("erreur", toJson (toString ex))]
      pure none
  if let some envR := rejoue then
    let attendus := (List.range m).map (fun i => Name.mkSimple ("etape_" ++ toString (i + 1))) ++ [`enonce_item]
    for n in attendus do
      match envR.find? n, nouvelles.get? n with
      | some ci, some _ =>
        let (r, _) ← (MetaM.run' (enonceEtAllerRetour ci.type)).toIO contexte { env := envR }
        let citees := ci.type.getUsedConstants.filter (fun c => nouvelles.contains c)
        emettre [("type", toJson "attendu"), ("nom", toJson n.toString), ("present", toJson true),
                 ("genre", toJson (genre ci)), ("axiomes", toJson ((axiomesDe envR n).map (·.toString))),
                 ("enonce", toJson r.texte), ("enonce_explicite", toJson r.explicite), ("aller_retour", toJson r.egal),
                 ("tronque", toJson r.tronque), ("metavariables", toJson r.metavariables),
                 ("messages_elaboration", toJson r.messages), ("raison", toJson r.raison),
                 ("constantes_agent", toJson (citees.map (·.toString)))]
      | _, _ =>
        emettre [("type", toJson "attendu"), ("nom", toJson n.toString), ("present", toJson false)]
    for (n, ci) in nouvelles.toList do
      if genre ci != "theoreme" then
        let ((t, v), _) ← (MetaM.run' do
            let t := toString (← withOptions optionsImpression (ppExpr ci.type))
            let v ← match ci.value? with
              | some val => pure (toString (← withOptions optionsImpression (ppExpr val)))
              | none => pure ""
            pure (t, v)).toIO contexte { env := envR }
        emettre [("type", toJson "definition"), ("nom", toJson n.toString), ("genre", toJson (genre ci)),
                 ("enonce", toJson t), ("valeur", toJson v)]
  emettre [("type", toJson "fin"), ("nonce", toJson nonce)]
  return 0

end VerificateurNoyauV4

def main (args : List String) : IO UInt32 := do
  match args with
  | [chemin, m, nonce] =>
    match m.toNat? with
    | some k => VerificateurNoyauV4.principal chemin k nonce
    | none => IO.eprintln "nombre d'étapes illisible"; return 2
  | _ => IO.eprintln "usage : verificateur_noyau_v4 ITEM.olean M NONCE"; return 2
