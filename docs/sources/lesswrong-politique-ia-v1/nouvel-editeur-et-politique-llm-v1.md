There's a new editor experience on LessWrong! A bunch of the editor page has been rearranged to make it much more WYSIWYG compared to published post pages. All of the settings live in panels that are hidden by default and can be opened up by clicking the relevant buttons on the side of the screen. We also adopted lexical as a new editor framework powering everything behind the scenes (we were previously using ckEditor).

![image.png](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1773433647/lexical_client_uploads/mwxl0xjswdu7vlubjxzh.png)

That scary arrow button in the top-left doesn't publish your post! It just opens the publishing menu.

Posts[^or44zdzw0tp] now have automatic real-time autosave while you're online (like Google Docs), but still support offline editing if your connection drops out. Point-in-time revisions will still get autosaved periodically, and you can always manually save your draft if you want a specific checkpoint.

The editor also has a slash menu now!

![image.png](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1773348116/lexical_client_uploads/adeo2xmststgotgztshj.png)

Good for ~~all~~ many of your custom content needs!

You might be eyeing the last two items in that slash menu. This post will demo some of the new features, and I'll demo two of them simultaneously by letting Opus 4.6 explain what they are:

%%% llm-output model="Claude Opus 4.6"

Hi! I'm Claude, and I'm writing this from inside the post you're reading right now. This block I'm in is one of the new editor features — let me walk you through a few of them.

### LLM Content Blocks

This visually distinct block is an **LLM Content Block**. Authors can insert these into their posts to clearly attribute a section to a specific AI model. The block header shows which model generated the content, so readers always know what they're looking at. It's a way to be transparent about AI-assisted writing while keeping everything in one document.

### Custom Iframe Widgets

The new editor supports **custom interactive widgets** embedded directly in posts. Authors can write HTML and JavaScript that runs in a sandboxed iframe right in the document — useful for interactive demos, visualizations, small tools, or anything else that benefits from being more than static text. There's one just below this block, in fact.

### Agent Integration

The editor now has an API that lets AI agents read and edit drafts collaboratively. If you share your draft's edit link with an AI assistant (like me), it can insert text, leave Google Docs-style comments, make suggested edits, and add LLM content blocks and widgets — all showing up live in the editor. That's how this entire block was written: not copy-pasted in, but inserted directly through the API while the post was open for editing.

To use it, open your post's sharing settings and set "Anyone with the link can" to Edit, then copy the edit URL and share it with your AI assistant.

With Edit permissions, the agent can do everything: insert and modify text, add widgets, create LLM content blocks, and more. If you'd prefer to keep tighter control, **Comment** permissions still allow the agent to leave inline comments and suggested edits, which you can accept or reject individually.

Setup depends on which AI tool you're using. Agent harnesses that can make HTTP requests directly — like Claude Code, Codex, or Cursor — should work out of the box. If you're using **Claude on** [**claude.ai**](https://claude.ai), you'll need to add `www.lesswrong.com` to your [allowed domains settings](https://claude.ai/settings/capabilities), then start a new chat. (The ChatGPT web UI doesn't currently support whitelisting external domains, so it can't be used for this feature yet.) Once that's done, just paste your edit URL and ask Claude to read the post — the API is self-describing, so it'll figure out the rest from there.

%%% /llm-output

And here's a small interactive widget, also written by Claude[^fzo5um3byng], to demonstrate custom iframe widgets:

```widget[9BFED9hSEdQxA6YdW]
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Font Synaesthesia Test</title>
  <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  <script crossorigin src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel">
const { useState, useEffect, useRef, useCallback } = React;


const LETTERS = "ABCDEFGHJKLMNPQRSTUVWXYZ".split("");


const SERIF_FONTS = [
  "'Georgia', 'Times New Roman', serif",
  "'Times New Roman', Times, serif",
];
const SANS_FONTS = [
  "'Helvetica Neue', Helvetica, Arial, sans-serif",
  "'Arial', Helvetica, sans-serif",
];


const GRID_CONFIGS = [
  { rows: 6, cols: 8 },
  { rows: 7, cols: 9 },
  { rows: 8, cols: 10 },
];


const TOTAL_TRIALS = 15;


function pickRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}


function shuffleArray(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}


function generateTrial(trialIndex) {
  const difficulty = Math.min(2, Math.floor(trialIndex / 5));
  const { rows, cols } = GRID_CONFIGS[difficulty];
  const total = rows * cols;


  // Decide direction: serif-in-sans or sans-in-serif
  const serifTarget = Math.random() < 0.5;
  const baseFont = serifTarget ? pickRandom(SANS_FONTS) : pickRandom(SERIF_FONTS);
  const targetFont = serifTarget ? pickRandom(SERIF_FONTS) : pickRandom(SANS_FONTS);


  const targetIdx = Math.floor(Math.random() * total);


  // Use the SAME letter for target and several distractors so shape doesn't help
  const targetLetter = pickRandom(LETTERS);


  const cells = [];
  for (let i = 0; i < total; i++) {
    const isTarget = i === targetIdx;
    // ~30% of distractors share the target letter
    const letter =
      isTarget || Math.random() < 0.3
        ? targetLetter
        : pickRandom(LETTERS);
    cells.push({
      letter,
      font: isTarget ? targetFont : baseFont,
      isTarget,
      id: i,
    });
  }


  return {
    cells,
    rows,
    cols,
    serifTarget,
    targetIdx,
    targetLetter,
    difficulty,
  };
}


// ── Screens ──────────────────────────────────────────────────


function IntroScreen({ onStart }) {
  return (
    <div style={styles.introContainer}>
      <div style={styles.introCard}>
        <div style={styles.labBadge}>PERCEPTUAL LAB</div>
        <h1 style={styles.introTitle}>Font Synaesthesia Test</h1>
        <p style={styles.introSubtitle}>
          A typographic embedded-figures task
        </p>


        <div style={styles.introExplainer}>
          <p style={styles.introText}>
            In the classic number-color synaesthesia test, a target digit is
            hidden in a field of distractors. For grapheme-color synaesthetes,
            the target "pops out" instantly because it appears in a vivid,
            involuntary color.
          </p>
          <p style={styles.introText}>
            This test adapts that paradigm for <em>font perception</em>. On
            each trial, a grid of letters will appear — all set in one font
            class (serif or sans-serif) except for <strong>one letter</strong>{" "}
            set in the opposite class. Find and click it as fast as you can.
          </p>
        </div>


        <div style={styles.demoRow}>
          <div style={styles.demoBlock}>
            <span style={{ fontFamily: "'Georgia', serif", fontSize: 38, color: "#1a1a1a" }}>
              A
            </span>
            <span style={styles.demoLabel}>Serif</span>
          </div>
          <span style={styles.demoVs}>vs</span>
          <div style={styles.demoBlock}>
            <span
              style={{
                fontFamily: "'Helvetica Neue', Helvetica, sans-serif",
                fontSize: 38,
                color: "#1a1a1a",
              }}
            >
              A
            </span>
            <span style={styles.demoLabel}>Sans-serif</span>
          </div>
        </div>


        <div style={styles.trialInfo}>
          {TOTAL_TRIALS} trials · difficulty increases every 5 trials
        </div>


        <button style={styles.startBtn} onClick={onStart}>
          Begin Test
        </button>
      </div>
    </div>
  );
}


function TrialScreen({ trial, trialNumber, onCellClick, startTime }) {
  const [elapsed, setElapsed] = useState(0);


  useEffect(() => {
    const iv = setInterval(() => {
      setElapsed(Date.now() - startTime);
    }, 47);
    return () => clearInterval(iv);
  }, [startTime]);


  const { cells, rows, cols, serifTarget } = trial;


  return (
    <div style={styles.trialContainer}>
      <div style={styles.trialHeader}>
        <div style={styles.trialMeta}>
          <span style={styles.trialLabel}>Trial</span>
          <span style={styles.trialNumber}>
            {trialNumber}/{TOTAL_TRIALS}
          </span>
        </div>
        <div style={styles.trialInstruction}>
          Find the{" "}
          <strong style={{ color: serifTarget ? "#b44" : "#38a" }}>
            {serifTarget ? "serif" : "sans-serif"}
          </strong>{" "}
          letter
        </div>
        <div style={styles.timer}>{(elapsed / 1000).toFixed(1)}s</div>
      </div>


      <div
        style={{
          ...styles.grid,
          gridTemplateColumns: `repeat(${cols}, 1fr)`,
          gridTemplateRows: `repeat(${rows}, 1fr)`,
        }}
      >
        {cells.map((cell) => (
          <button
            key={cell.id}
            style={{
              ...styles.cell,
              fontFamily: cell.font,
            }}
            onClick={() => onCellClick(cell)}
          >
            {cell.letter}
          </button>
        ))}
      </div>


      <div style={styles.difficultyBar}>
        {[0, 1, 2].map((d) => (
          <div
            key={d}
            style={{
              ...styles.diffDot,
              background:
                d <= trial.difficulty
                  ? "var(--accent)"
                  : "var(--bg-muted)",
            }}
          />
        ))}
        <span style={styles.diffLabel}>
          {["6×8", "7×9", "8×10"][trial.difficulty]} grid
        </span>
      </div>
    </div>
  );
}


function FeedbackFlash({ correct }) {
  return (
    <div
      style={{
        ...styles.flash,
        background: correct
          ? "rgba(34,160,90,0.12)"
          : "rgba(200,50,50,0.12)",
        color: correct ? "#1a7a42" : "#a03030",
      }}
    >
      {correct ? "✓ Correct" : "✗ Wrong — that was a distractor"}
    </div>
  );
}


function ResultsScreen({ results, onRestart }) {
  const correctResults = results.filter((r) => r.correct);
  const accuracy = ((correctResults.length / results.length) * 100).toFixed(0);
  const times = correctResults.map((r) => r.time);
  const mean = times.length ? times.reduce((a, b) => a + b, 0) / times.length : 0;
  const sorted = [...times].sort((a, b) => a - b);
  const median = sorted.length
    ? sorted.length % 2 === 0
      ? (sorted[sorted.length / 2 - 1] + sorted[sorted.length / 2]) / 2
      : sorted[Math.floor(sorted.length / 2)]
    : 0;
  const best = sorted.length ? sorted[0] : 0;
  const worst = sorted.length ? sorted[sorted.length - 1] : 0;
  const sd = times.length > 1
    ? Math.sqrt(times.reduce((s, t) => s + (t - mean) ** 2, 0) / (times.length - 1))
    : 0;


  // Build histogram bins (200ms wide)
  const binWidth = 200;
  const maxT = Math.max(...times, 2000);
  const bins = [];
  for (let lo = 0; lo <= maxT; lo += binWidth) {
    bins.push({
      lo,
      hi: lo + binWidth,
      count: times.filter((t) => t >= lo && t < lo + binWidth).length,
    });
  }
  const maxCount = Math.max(...bins.map((b) => b.count), 1);


  // By-difficulty breakdown
  const byDiff = [0, 1, 2].map((d) => {
    const dResults = correctResults.filter((r) => r.difficulty === d);
    const dTimes = dResults.map((r) => r.time);
    const dMean = dTimes.length
      ? dTimes.reduce((a, b) => a + b, 0) / dTimes.length
      : null;
    return { difficulty: d, label: ["6×8", "7×9", "8×10"][d], mean: dMean, n: dTimes.length };
  });


  // By-direction breakdown
  const serifInSans = correctResults.filter((r) => r.serifTarget);
  const sansInSerif = correctResults.filter((r) => !r.serifTarget);
  const serifMean = serifInSans.length
    ? serifInSans.reduce((a, b) => a + b.time, 0) / serifInSans.length
    : null;
  const sansMean = sansInSerif.length
    ? sansInSerif.reduce((a, b) => a + b.time, 0) / sansInSerif.length
    : null;


  return (
    <div style={styles.resultsContainer}>
      <div style={styles.resultsCard}>
        <div style={styles.labBadge}>RESULTS</div>
        <h2 style={styles.resultsTitle}>Test Complete</h2>


        <div style={styles.statGrid}>
          <StatBox label="Accuracy" value={`${accuracy}%`} sub={`${correctResults.length}/${results.length} correct`} />
          <StatBox label="Mean RT" value={`${mean.toFixed(0)}ms`} sub={`SD ${sd.toFixed(0)}ms`} />
          <StatBox label="Median RT" value={`${median.toFixed(0)}ms`} sub={`${best.toFixed(0)}–${worst.toFixed(0)}ms`} />
        </div>


        {/* Histogram */}
        {times.length > 0 && (
          <div style={styles.histSection}>
            <h3 style={styles.sectionTitle}>Reaction Time Distribution</h3>
            <div style={styles.histContainer}>
              {bins.map((bin, i) => (
                <div key={i} style={styles.histCol}>
                  <div
                    style={{
                      ...styles.histBar,
                      height: `${(bin.count / maxCount) * 100}%`,
                      background:
                        bin.count > 0
                          ? "var(--accent)"
                          : "transparent",
                    }}
                  >
                    {bin.count > 0 && (
                      <span style={styles.histCount}>{bin.count}</span>
                    )}
                  </div>
                  <span style={styles.histLabel}>
                    {bin.lo < 1000
                      ? `${bin.lo}`
                      : `${(bin.lo / 1000).toFixed(1)}k`}
                  </span>
                </div>
              ))}
            </div>
            <div style={styles.histAxis}>Reaction time (ms)</div>
          </div>
        )}


        {/* Direction comparison */}
        <div style={styles.comparisonSection}>
          <h3 style={styles.sectionTitle}>By Target Type</h3>
          <div style={styles.comparisonRow}>
            <CompBar
              label="Serif in sans-serif"
              value={serifMean}
              n={serifInSans.length}
              max={Math.max(serifMean || 0, sansMean || 0, 1)}
              color="#b44"
            />
            <CompBar
              label="Sans-serif in serif"
              value={sansMean}
              n={sansInSerif.length}
              max={Math.max(serifMean || 0, sansMean || 0, 1)}
              color="#38a"
            />
          </div>
        </div>


        {/* By difficulty */}
        <div style={styles.comparisonSection}>
          <h3 style={styles.sectionTitle}>By Grid Size</h3>
          <div style={styles.comparisonRow}>
            {byDiff.map((d) => (
              <CompBar
                key={d.difficulty}
                label={d.label}
                value={d.mean}
                n={d.n}
                max={Math.max(...byDiff.map((x) => x.mean || 0), 1)}
                color="var(--accent)"
              />
            ))}
          </div>
        </div>


        {/* Individual trial list */}
        <div style={styles.trialListSection}>
          <h3 style={styles.sectionTitle}>Individual Trials</h3>
          <div style={styles.trialList}>
            {results.map((r, i) => (
              <div
                key={i}
                style={{
                  ...styles.trialRow,
                  opacity: r.correct ? 1 : 0.5,
                }}
              >
                <span style={styles.trialRowNum}>#{i + 1}</span>
                <span
                  style={{
                    ...styles.trialRowIcon,
                    color: r.correct ? "#1a7a42" : "#a03030",
                  }}
                >
                  {r.correct ? "✓" : "✗"}
                </span>
                <span style={styles.trialRowTime}>
                  {r.time.toFixed(0)}ms
                </span>
                <span style={styles.trialRowType}>
                  {r.serifTarget ? "serif target" : "sans target"}
                </span>
                <span style={styles.trialRowGrid}>
                  {["6×8", "7×9", "8×10"][r.difficulty]}
                </span>
              </div>
            ))}
          </div>
        </div>


        <div style={styles.interpretSection}>
          <h3 style={styles.sectionTitle}>Interpretation</h3>
          <p style={styles.interpretText}>
            {mean < 1200
              ? "Very fast detection — font class differences pop out for you almost pre-attentively. This is consistent with heightened sensitivity to typographic form."
              : mean < 2200
              ? "Solid detection speed. You can distinguish serif from sans-serif with moderate effort — typical of someone with some typographic awareness."
              : "Slower detection suggests you may be relying on serial scanning rather than parallel pop-out. The serif/sans-serif distinction may not be perceptually salient for you."}
          </p>
          {serifMean && sansMean && Math.abs(serifMean - sansMean) > 200 && (
            <p style={styles.interpretText}>
              Notable asymmetry: you found{" "}
              <strong>
                {serifMean < sansMean ? "serif-in-sans" : "sans-in-serif"}
              </strong>{" "}
              targets ~{Math.abs(serifMean - sansMean).toFixed(0)}ms faster,
              suggesting that direction may be more perceptually distinct for
              you.
            </p>
          )}
        </div>


        <button style={styles.startBtn} onClick={onRestart}>
          Run Again
        </button>
      </div>
    </div>
  );
}


function StatBox({ label, value, sub }) {
  return (
    <div style={styles.statBox}>
      <div style={styles.statLabel}>{label}</div>
      <div style={styles.statValue}>{value}</div>
      <div style={styles.statSub}>{sub}</div>
    </div>
  );
}


function CompBar({ label, value, n, max, color }) {
  return (
    <div style={styles.compBarWrap}>
      <div style={styles.compBarLabel}>
        {label} <span style={{ opacity: 0.5 }}>n={n}</span>
      </div>
      <div style={styles.compBarTrack}>
        <div
          style={{
            ...styles.compBarFill,
            width: value ? `${(value / (max * 1.3)) * 100}%` : 0,
            background: color,
          }}
        />
      </div>
      <div style={styles.compBarValue}>
        {value ? `${value.toFixed(0)}ms` : "—"}
      </div>
    </div>
  );
}


// ── Main App ─────────────────────────────────────────────────


function FontSynaesthesiaTest() {
  const [phase, setPhase] = useState("intro"); // intro | countdown | trial | feedback | results
  const [trial, setTrial] = useState(null);
  const [trialNumber, setTrialNumber] = useState(0);
  const [results, setResults] = useState([]);
  const [startTime, setStartTime] = useState(0);
  const [countdown, setCountdown] = useState(3);
  const [lastCorrect, setLastCorrect] = useState(true);


  const startTrial = useCallback((num) => {
    const t = generateTrial(num - 1);
    setTrial(t);
    setTrialNumber(num);
    setPhase("trial");
    setStartTime(Date.now());
  }, []);


  const handleStart = useCallback(() => {
    setResults([]);
    setTrialNumber(0);
    setCountdown(3);
    setPhase("countdown");
  }, []);


  useEffect(() => {
    if (phase !== "countdown") return;
    if (countdown <= 0) {
      startTrial(1);
      return;
    }
    const timer = setTimeout(() => setCountdown((c) => c - 1), 700);
    return () => clearTimeout(timer);
  }, [phase, countdown, startTrial]);


  const handleCellClick = useCallback(
    (cell) => {
      const rt = Date.now() - startTime;
      const correct = cell.isTarget;
      const result = {
        time: rt,
        correct,
        serifTarget: trial.serifTarget,
        difficulty: trial.difficulty,
        trialNumber,
      };
      setResults((prev) => [...prev, result]);
      setLastCorrect(correct);
      setPhase("feedback");


      setTimeout(() => {
        if (trialNumber >= TOTAL_TRIALS) {
          setPhase("results");
        } else {
          startTrial(trialNumber + 1);
        }
      }, correct ? 500 : 1100);
    },
    [startTime, trial, trialNumber, startTrial]
  );


  return (
    <div style={styles.root}>
      <style>{cssVars}</style>
      {phase === "intro" && <IntroScreen onStart={handleStart} />}
      {phase === "countdown" && (
        <div style={styles.countdownWrap}>
          <div style={styles.countdownNum}>{countdown || "Go"}</div>
        </div>
      )}
      {phase === "trial" && trial && (
        <TrialScreen
          trial={trial}
          trialNumber={trialNumber}
          onCellClick={handleCellClick}
          startTime={startTime}
        />
      )}
      {phase === "feedback" && <FeedbackFlash correct={lastCorrect} />}
      {phase === "results" && (
        <ResultsScreen results={results} onRestart={handleStart} />
      )}
    </div>
  );
}


// ── Styles ───────────────────────────────────────────────────


const cssVars = `
  :root {
    --bg: #f5f2ed;
    --bg-card: #fffdf9;
    --bg-muted: #e8e4dd;
    --fg: #1a1a1a;
    --fg-dim: #6b6560;
    --accent: #8b5c3a;
    --accent-light: rgba(139,92,58,0.10);
    --radius: 8px;
    --font-body: 'Segoe UI', system-ui, -apple-system, sans-serif;
    --font-mono: 'SF Mono', 'Consolas', 'Menlo', monospace;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg); }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
  }
  @keyframes pulseIn {
    0% { transform: scale(0.8); opacity: 0; }
    60% { transform: scale(1.08); }
    100% { transform: scale(1); opacity: 1; }
  }
`;


const styles = {
  root: {
    minHeight: "100vh",
    background: "var(--bg)",
    fontFamily: "var(--font-body)",
    color: "var(--fg)",
  },


  // Intro
  introContainer: {
    minHeight: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: 24,
  },
  introCard: {
    background: "var(--bg-card)",
    border: "1px solid var(--bg-muted)",
    borderRadius: 16,
    padding: "48px 40px",
    maxWidth: 600,
    width: "100%",
    textAlign: "center",
    animation: "fadeIn 0.5s ease-out",
  },
  labBadge: {
    display: "inline-block",
    fontSize: 10,
    fontWeight: 700,
    letterSpacing: 3,
    color: "var(--accent)",
    background: "var(--accent-light)",
    padding: "5px 14px",
    borderRadius: 20,
    marginBottom: 20,
    fontFamily: "var(--font-mono)",
  },
  introTitle: {
    fontSize: 32,
    fontWeight: 300,
    letterSpacing: -0.5,
    marginBottom: 6,
    color: "var(--fg)",
  },
  introSubtitle: {
    fontSize: 14,
    color: "var(--fg-dim)",
    marginBottom: 28,
    fontStyle: "italic",
  },
  introExplainer: {
    textAlign: "left",
    marginBottom: 28,
    padding: "0 8px",
  },
  introText: {
    fontSize: 14,
    lineHeight: 1.65,
    color: "var(--fg-dim)",
    marginBottom: 12,
  },
  demoRow: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    gap: 28,
    margin: "28px 0",
  },
  demoBlock: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    gap: 6,
    background: "var(--bg)",
    borderRadius: 12,
    padding: "16px 28px",
  },
  demoLabel: {
    fontSize: 11,
    fontWeight: 600,
    letterSpacing: 1,
    textTransform: "uppercase",
    color: "var(--fg-dim)",
    fontFamily: "var(--font-mono)",
  },
  demoVs: {
    fontSize: 13,
    color: "var(--fg-dim)",
    fontStyle: "italic",
  },
  trialInfo: {
    fontSize: 12,
    color: "var(--fg-dim)",
    marginBottom: 24,
    fontFamily: "var(--font-mono)",
  },
  startBtn: {
    display: "inline-block",
    fontSize: 15,
    fontWeight: 600,
    color: "#fff",
    background: "var(--accent)",
    border: "none",
    borderRadius: 8,
    padding: "14px 44px",
    cursor: "pointer",
    letterSpacing: 0.5,
    transition: "transform 0.15s, box-shadow 0.15s",
  },


  // Countdown
  countdownWrap: {
    minHeight: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  countdownNum: {
    fontSize: 96,
    fontWeight: 200,
    color: "var(--accent)",
    animation: "pulseIn 0.5s ease-out",
    fontFamily: "var(--font-mono)",
  },


  // Trial
  trialContainer: {
    minHeight: "100vh",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    padding: "20px 16px",
  },
  trialHeader: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    width: "100%",
    maxWidth: 720,
    marginBottom: 16,
    padding: "0 4px",
  },
  trialMeta: {
    display: "flex",
    flexDirection: "column",
  },
  trialLabel: {
    fontSize: 10,
    fontWeight: 700,
    letterSpacing: 2,
    textTransform: "uppercase",
    color: "var(--fg-dim)",
    fontFamily: "var(--font-mono)",
  },
  trialNumber: {
    fontSize: 22,
    fontWeight: 300,
    fontFamily: "var(--font-mono)",
  },
  trialInstruction: {
    fontSize: 15,
    color: "var(--fg-dim)",
  },
  timer: {
    fontSize: 18,
    fontWeight: 500,
    fontFamily: "var(--font-mono)",
    color: "var(--accent)",
    minWidth: 60,
    textAlign: "right",
  },


  // Grid
  grid: {
    display: "grid",
    gap: 0,
    width: "100%",
    maxWidth: 720,
    aspectRatio: "10 / 7",
    background: "var(--bg-card)",
    border: "1px solid var(--bg-muted)",
    borderRadius: 12,
    overflow: "hidden",
    animation: "fadeIn 0.25s ease-out",
  },
  cell: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: "clamp(18px, 3vw, 30px)",
    fontWeight: 400,
    color: "var(--fg)",
    background: "transparent",
    border: "1px solid rgba(0,0,0,0.04)",
    cursor: "pointer",
    transition: "background 0.1s",
    padding: 0,
    lineHeight: 1,
    userSelect: "none",
    WebkitUserSelect: "none",
  },


  difficultyBar: {
    display: "flex",
    alignItems: "center",
    gap: 6,
    marginTop: 12,
  },
  diffDot: {
    width: 8,
    height: 8,
    borderRadius: "50%",
    transition: "background 0.3s",
  },
  diffLabel: {
    fontSize: 11,
    color: "var(--fg-dim)",
    marginLeft: 6,
    fontFamily: "var(--font-mono)",
  },


  // Feedback
  flash: {
    minHeight: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: 28,
    fontWeight: 400,
    animation: "pulseIn 0.25s ease-out",
  },


  // Results
  resultsContainer: {
    minHeight: "100vh",
    display: "flex",
    alignItems: "flex-start",
    justifyContent: "center",
    padding: "40px 24px",
  },
  resultsCard: {
    background: "var(--bg-card)",
    border: "1px solid var(--bg-muted)",
    borderRadius: 16,
    padding: "48px 40px",
    maxWidth: 660,
    width: "100%",
    textAlign: "center",
    animation: "fadeIn 0.5s ease-out",
  },
  resultsTitle: {
    fontSize: 28,
    fontWeight: 300,
    marginBottom: 28,
  },


  statGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: 16,
    marginBottom: 36,
  },
  statBox: {
    background: "var(--bg)",
    borderRadius: 12,
    padding: "18px 12px",
  },
  statLabel: {
    fontSize: 10,
    fontWeight: 700,
    letterSpacing: 2,
    textTransform: "uppercase",
    color: "var(--fg-dim)",
    fontFamily: "var(--font-mono)",
    marginBottom: 6,
  },
  statValue: {
    fontSize: 28,
    fontWeight: 300,
    color: "var(--accent)",
    fontFamily: "var(--font-mono)",
  },
  statSub: {
    fontSize: 11,
    color: "var(--fg-dim)",
    marginTop: 4,
    fontFamily: "var(--font-mono)",
  },


  sectionTitle: {
    fontSize: 12,
    fontWeight: 700,
    letterSpacing: 2,
    textTransform: "uppercase",
    color: "var(--fg-dim)",
    marginBottom: 16,
    fontFamily: "var(--font-mono)",
  },


  // Histogram
  histSection: {
    marginBottom: 32,
    textAlign: "center",
  },
  histContainer: {
    display: "flex",
    alignItems: "flex-end",
    height: 120,
    gap: 3,
    padding: "0 4px",
  },
  histCol: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    height: "100%",
    justifyContent: "flex-end",
  },
  histBar: {
    width: "100%",
    borderRadius: "4px 4px 0 0",
    display: "flex",
    alignItems: "flex-start",
    justifyContent: "center",
    minHeight: 2,
    transition: "height 0.4s ease-out",
  },
  histCount: {
    fontSize: 9,
    fontWeight: 700,
    color: "#fff",
    marginTop: 3,
    fontFamily: "var(--font-mono)",
  },
  histLabel: {
    fontSize: 8,
    color: "var(--fg-dim)",
    marginTop: 4,
    fontFamily: "var(--font-mono)",
  },
  histAxis: {
    fontSize: 10,
    color: "var(--fg-dim)",
    marginTop: 8,
    fontStyle: "italic",
  },


  // Comparison bars
  comparisonSection: {
    marginBottom: 28,
    textAlign: "left",
  },
  comparisonRow: {
    display: "flex",
    flexDirection: "column",
    gap: 10,
  },
  compBarWrap: {
    display: "flex",
    alignItems: "center",
    gap: 10,
  },
  compBarLabel: {
    fontSize: 12,
    color: "var(--fg-dim)",
    minWidth: 160,
    textAlign: "right",
    fontFamily: "var(--font-mono)",
  },
  compBarTrack: {
    flex: 1,
    height: 22,
    background: "var(--bg)",
    borderRadius: 6,
    overflow: "hidden",
  },
  compBarFill: {
    height: "100%",
    borderRadius: 6,
    transition: "width 0.6s ease-out",
    opacity: 0.75,
  },
  compBarValue: {
    fontSize: 13,
    fontWeight: 600,
    minWidth: 60,
    fontFamily: "var(--font-mono)",
    color: "var(--fg)",
  },


  // Trial list
  trialListSection: {
    marginBottom: 28,
    textAlign: "left",
  },
  trialList: {
    display: "flex",
    flexDirection: "column",
    gap: 2,
  },
  trialRow: {
    display: "flex",
    alignItems: "center",
    gap: 10,
    padding: "6px 8px",
    borderRadius: 6,
    fontSize: 12,
    fontFamily: "var(--font-mono)",
    background: "var(--bg)",
  },
  trialRowNum: {
    color: "var(--fg-dim)",
    minWidth: 28,
  },
  trialRowIcon: {
    fontWeight: 700,
    minWidth: 16,
  },
  trialRowTime: {
    fontWeight: 600,
    minWidth: 56,
  },
  trialRowType: {
    color: "var(--fg-dim)",
    flex: 1,
  },
  trialRowGrid: {
    color: "var(--fg-dim)",
  },


  // Interpretation
  interpretSection: {
    textAlign: "left",
    marginBottom: 28,
    padding: "20px",
    background: "var(--accent-light)",
    borderRadius: 12,
  },
  interpretText: {
    fontSize: 14,
    lineHeight: 1.65,
    color: "var(--fg)",
    marginTop: 8,
  },
};


// ── Mount ────────────────────────────────────────────────────


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<FontSynaesthesiaTest />);
  </script>
</body>
</html>
```

  

Policy on LLM Use
=================

*(Note: For first-time users, we have closer to a zero-LLM policy)*

You might be wondering what this means for our policy on LLM use.

Our initial policy was this:

> A rough guideline is that if you are using AI for writing assistance, you should spend a minimum of 1 minute per 50 words (enough to read the content several times and perform significant edits), you should not include any information that you can't verify, haven't verified, or don't understand, and you should not use the stereotypical writing style of an AI assistant.

You were also permitted to put LLM-generated content into collapsible sections, if you labeled it as LLM-generated.

In practice, the "you should not use the stereotypical writing style of an AI assistant" part of the requirement meant that this was a de-facto ban on LLM use, which we enforced mostly consistently on new users and very inconsistently on existing users[^s43frbsc5jb]. Bad!

To motivate our updated policy, we must first do some philosophy. Why do we care about knowing whether something we're reading was generated by an LLM? [LLM-generated text is not testimony](https://www.lesswrong.com/posts/DDG2Tf2sqc8rTWRk3/llm-generated-text-is-not-testimony) has substantially informed my thinking on this question. Take the synopsis:

> 1.  When we share words with each other, we don't only care about the words themselves. We care also—even primarily—about the mental elements of the human mind/agency that produced the words. What we want to engage with is those mental elements.
> 2.  As of 2025, LLM text does not have those elements behind it.
> 3.  Therefore LLM text categorically does not serve the role for communication that is served by real text.
> 4.  Therefore the norm should be that you don't share LLM text as if someone wrote it. And, it is inadvisable to read LLM text that someone else shares as though someone wrote it.

I don't think you even need to confidently believe in point 2[^09tu8uhs95tm] for the norm in point 4 to be compelling. It is merely sufficient that *someone else* produced the text.

Plagiarism is often considered bad because it's "stealing credit" for someone else's work. But it's also bad because it's misinforming your readers about your beliefs and mental models! What happens if someone asks you why you're so confident about [proposition X]? It really sucks if the answer is "Oh, uh, I didn't write that sentence, and re-reading it, it turns out I'm not actually *that* confident in that claim..."

This is also why having LLMs "edit" your writing is often pernicious. LLM editing, unless managed extremely carefully, often involves rephrasings, added qualifiers, and swapped vocabulary in ways that meaningfully change the semantic content of your writing. Very often this is in unendorsed ways, but this can be hard to pick up on because the typical LLM writing style has a tendency to make people's eyes slide off of it[^twnpwaeibe].

With all that in mind, our new policy is this:

*   **"LLM output"** includes all of:
    *   text written entirely by an LLM
    *   text that was written by a human and then substantially[^87euids1664] edited or revised by an LLM
    *   text that was written by an LLM and then edited or revised by a human
*   "LLM output" does not include:
    *   text that was written by a human and then lightly edited or revised by an LLM
    *   text written by a human, which includes facts, arguments, examples, etc, which were researched/discovered/developed with LLM assistance. (If you "borrow language" from the LLM, that no longer counts as "text written by a human".)
    *   code (either in code blocks or in the new widgets)

"LLM output" must go into the new LLM content blocks. You can put "LLM output" into a collapsible section without wrapping it in an LLM content block if all of the content is "LLM output". If it's mixed, you should use LLM content blocks within the collapsible section to demarcate those parts which are "LLM output".

We are going to be more strictly enforcing the "no LLM output" rule by normalizing our auto-moderation logic to treat posts by approved[^qcbd160asy] users similarly to posts by new users - that is, they'll be automatically rejected if they score above a certain threshold in our automated LLM content detection pipeline. Having spent a few months staring at what's been coming down the pipe, we are also going to be lowering that threshold.

This does not change our existing quality bar for new user submissions. If you are a new user and submit a post that substantially consists of content inside of LLM content blocks, it is pretty unlikely that it will get approved[^71sigspfz4y]. This does not suddenly become wise if you're an approved user. If you're confident that people will want to read it, then sure, go ahead, but please pay close attention to the kind of feedback you get (karma, comments, etc), and if this proves noisy we'll probably just tell people to cut it out.

What about translation?
-----------------------

If you are not a fluent english speaker and want to use LLMs to help you publish to LessWrong, the way to do this is to write it out normally in your native language, and then ask the LLM to do a direct word-for-word translation (no rewriting, embellishment, tweaks, etc). This usually results in content that feels reasonable / non-slop-like to read, and which doesn't trigger our AI writing detectors.

* * *

As always, please submit feedback, questions, and bug reports via Intercom (or in the comments below, if you prefer).

[^or44zdzw0tp]: Not comments or other content types that use the editor, like tags - those still have the same local backup mechanism they've always had, and you can still explicitly save draft comments, but none of them get automatically synced to the cloud as you type. Also, existing posts and drafts will continue to use the previous editor, and won't have access to the new features. 

[^fzo5um3byng]: Prompted by [@jimrandomh](http://localhost:3000/users/jimrandomh?mention=user). 

[^s43frbsc5jb]: For somewhat contingent reasons involving various choices we made with our moderation setup. 

[^09tu8uhs95tm]: See my [curation notice](https://www.lesswrong.com/posts/DDG2Tf2sqc8rTWRk3/llm-generated-text-is-not-testimony?commentId=L3robhc3TrTZcdPRf) on that post for some additional thoughts and caveats. 

[^twnpwaeibe]: I think [this recent thread](https://www.lesswrong.com/posts/jL7uDE5oH4HddYq4u/raemon-s-shortform?commentId=DZToM4tksLvsCRvrB) is instructive. 

[^87euids1664]: We'll know it when we see it. 

[^qcbd160asy]: In the ontology of our codebase, a term which means "users whose content goes live without further review by the admins", which is not true of users who haven't posted or commented before, and is also not true of a smaller number of users who have. 

[^71sigspfz4y]: I'm sure the people reading this will be able to conjure up some edge cases and counterexamples; go on, have fun.