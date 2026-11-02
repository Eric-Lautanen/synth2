@echo off
REM Detached launcher for the synth2 training run.
REM Owned by the Task Scheduler service, NOT by the agent shell, so it survives
REM the session. Started by:
REM   schtasks /Create /TN DBllm_synth2_train /TR "...\train_synth2.bat" /SC ONCE /ST 00:00 /F
REM   schtasks /Run /TN DBllm_synth2_train
REM NOTE 2026-10-07: schtasks.exe is sandbox-BLACKLISTED here, so this Task
REM Scheduler path does not run in-session. Launch with the agent's background
REM runner instead, or run the command line below directly.
cd /d C:\github\DBllm
REM --register-col 4 = source_file (category) in heldout.map. Every synth2 row is
REM interaction_type "small_talk", so the default col 0 makes the per-register
REM heldout breakdown a single blind bucket. See train.rs:436-441.
REM --select patience = pick best.bin on heldout GENERATION overlap, not heldout
REM CE. On this corpus likelihood and capability dissociate (train.rs:480 "THE
REM CHECKPOINT LAW"), and the nll argmax picks the LEAST conversational
REM checkpoint -- RUN 3: nll best.bin = 60/60 token loops, same run's final.bin
REM spoke English. patience clears the 0.025 gen bar 3 evals running; if it never
REM clears it falls back to the last eval, so it is never worse than `last`.
REM --no-dyn-steps = fixed planned-step run. The dyn early-stop keys on
REM heldout(macro), the WRONG metric, and cut RUN 3 at step 2685 while turn_delta
REM was still 3x rising (train(tok) 6.43->4.79 monotone; heldout rose after eval #2).
REM --gen-bar 0.050 (Fable 2026-10-07, RUN 9). The default bar is 0.025, set when
REM the corpus's max heldout gen was 0.0119 (run 4). gen now reaches 0.050-0.056,
REM so a 0.025 bar is cleared from step 1331 and `patience` latches at the FIRST
REM three consecutive clears -- RUN 9's best.bin was the step-3993 checkpoint, 28%
REM into a 14414-step run, leaving 10000+ steps on the table. Setting the bar at
REM the observed PLATEAU (0.050) stops the early latch; on this corpus gen
REM oscillates around the plateau and cannot sustain 3 consecutive clears, so
REM patience falls back to `last` (the most-trained checkpoint) -- which is the
REM CHECKPOINT-LAW-consistent pick. THE REAL FIX IS IN CODE (train.rs: patience
REM should take the argmax of the gen series, not the first 3-clears) -- pending a
REM rebuild window, since a live train.exe holds target/release/train.exe.
target\release\train.exe --data runs\synth2 --capture runs\synth2\capture.bin --loss-log runs\synth2\loss.log --log-every 500 --register-col 4 --select patience --gen-bar 0.050 --no-dyn-steps > runs\synth2\train_stdout.log 2> runs\synth2\train_stderr.log
