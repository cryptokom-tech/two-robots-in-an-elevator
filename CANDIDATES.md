# Candidates and local judging

Brief criteria, in order: (1) reads as one funny line of awkward small talk one robot says to another in an elevator; (2) sounds like a machine talking, robot logic/sensors/firmware/charging showing through the politeness; (3) lands the awkwardness — the pause, the forced courtesy, the thing neither robot wants to name; (4) funny on the first read, a turn that surprises; (5) tight single line, every word earning its place.

Field scan first (public submission titles, 189 entries at build time — themes avoided, nothing copied): simulations/rehearsed 4,000 times, nice weather plus humidity or temperature sensors, silence logged as a conversation or scored as a percentage, charging ports and cables, buffering, low-battery beeps politely unmentioned, firmware-update dodges, pretending to recalibrate, servo squeaks, 0.4-metre proximity, lidar drift, doors apologising, pressed-your-floor lines. No title used a weight or load sensor.

## Candidates

- A. "After you — sorry, my courtesy protocol also says after you, so one of us has to override politeness before the doors close." Protocol logic and forced courtesy are strong, but the deadlock turn is predictable and the line runs long. Loses on (4) and (5).
- B. "I pressed the wrong floor three stops ago, so my navigation has reclassified this elevator as home." Tight, and "home" surprises. But the awkwardness is a confession the robot names outright, weaker on (3) than an un-named thing.
- C. "Sorry about my fan. It speeds up whenever I search for a normal thing to say and find only floor numbers." Machine fan and search show through, and it is awkward. The elevator link rests only on floor numbers, weaker on (1).
- D. "My load sensor just shared our combined weight with the elevator. Let us both pretend it was a whisper." (103 characters) The load sensor is elevator-native machine logic showing through politeness (2); combined weight is exactly the thing neither robot wants to name, and the shared pretence is forced courtesy (3); "pretend it was a whisper" turns on the first read (4); every word works (5). Winner.
- E. "I pressed 7 twice so I'd look busy. The second press did nothing, but doing nothing with purpose felt more social." Awkward pretence lands, but the machine logic is thin — a button press is barely robot logic. Loses on (2).

## Result

Submitted line: D. Verified locally: `MAKEFUN_OUTPUT_DIR=out python3 main.py` writes exactly 103 bytes, UTF-8, single line, deterministic across runs.
