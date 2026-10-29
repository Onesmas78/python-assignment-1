# Python Assignment 1 — Practice for Classes 1 & 2

This assignment has **15 short exercises** that test what you've learned so far: variables, strings, conditionals, loops, lists, dictionaries and functions. It is checked automatically every time you push your code to GitHub.

**Deadline:** _2nd November 2026_
**Score:** 1 point per exercise, 15 points total.

| File | Exercises | Topics |
| --- | --- | --- |
| `assignment/part_a_basics.py` | A1–A5 | Operators, `if`/`elif`/`else`, strings, f-strings |
| `assignment/part_b_loops.py` | B1–B5 | Lists, dictionaries, `for` loops |
| `assignment/part_c_functions.py` | C1–C5 | Functions that combine everything |

Each exercise is a function with a description and examples. Replace the `pass` with your code. **Use `return`, not `print`.** The checker looks at what your function gives back.

---

## Step 1 — Get your own copy on GitHub

1. Sign in to [github.com](https://github.com) (create a free account if you don't have one).
2. Open the assignment link your instructor shared. Click the green **Use this template** button → **Create a new repository**.
3. Fill in the form:
   - **Repository name:** `python-assignment-1-<yourname>`, e.g. `python-assignment-1-amina`
   - **Visibility:** **Private**
   - Click **Create repository**.
4. Give your instructor access: in your new repository go to **Settings → Collaborators → Add people**. Then type your instructor's GitHub username.
5. Copy your repository's address: click the green **Code** button → **HTTPS** → copy. It looks like `https://github.com/<your-username>/python-assignment-1-<yourname>.git`.

## Step 2 — Connect Git to your GitHub account (one time only)

You already installed Git in setup. Now tell Git who you are. Use the same email as your GitHub account:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Next, install the GitHub CLI and log in. This lets `git push` work without passwords.

| OS | Install command |
| --- | --- |
| Windows (PowerShell) | `winget install --id GitHub.cli -e` |
| macOS | `brew install gh` |
| Ubuntu / Debian | `sudo apt install gh` |
| Fedora | `sudo dnf install gh` |

Close and reopen your terminal, then run:

```bash
gh auth login
```

Choose **GitHub.com → HTTPS → Yes (authenticate Git) → Login with a web browser**. Copy the one-time code shown, press Enter, and approve in the browser. Finally:

```bash
gh auth setup-git
gh auth status
```

`gh auth status` should say **Logged in to github.com**.

## Step 3 — Download (clone) your repository and set it up

Go to the folder where you keep class work, then clone. Paste **your** address from Step 1:

```bash
cd ~
git clone https://github.com/<your-username>/python-assignment-1-<yourname>.git
cd python-assignment-1-<yourname>
```

Create and activate a virtual environment, just like in setup:

| OS | Create | Activate |
| --- | --- | --- |
| Windows | `py -3.14 -m venv .venv` | `.venv\Scripts\Activate.ps1` |
| macOS | `python3.14 -m venv .venv` | `source .venv/bin/activate` |
| Linux | `python3 -m venv .venv` | `source .venv/bin/activate` |

Then install the checker and open the project in VS Code:

```bash
python -m pip install -r requirements.txt
code .
```

In VS Code, select the `.venv` interpreter (Ctrl/Cmd+Shift+P → **Python: Select Interpreter**).

## Step 4 — Do the exercises and check them on your computer

Run the checks from the repository's main folder (the one containing this README), with `(.venv)` showing:

```bash
pytest                          # check everything
pytest tests/test_part_a.py     # check only Part A
pytest -k a3                    # check only exercise A3
python tools/score.py           # (after: pytest --junitxml=results.xml) see a score table
```

At the start, everything fails. That is expected. Each exercise you finish turns from `FAILED` to `PASSED`. When something fails, read the message under `AssertionError`, which tells you what was expected.

You can also try a function by hand in the terminal:

```bash
cd assignment
python -c "from part_a_basics import get_grade; print(get_grade(74))"
cd ..
```

## Step 5 — Save (commit) and submit (push) your work

Commit **after you finish each part**. You should have at least 3 commits by the end. Small, regular commits are a habit real developers have.

```bash
git status                                  # see which files changed (red = not staged)
git add assignment/part_a_basics.py         # stage the file you changed
git status                                  # it should now be green
git commit -m "Complete Part A exercises"   # save a snapshot with a message
git push                                    # upload to GitHub = submit
```

Repeat for Part B and Part C with their own messages. Every `git push` sends your latest work. Your instructor grades the last commit you pushed **before the deadline**.

To check your history:

```bash
git log --oneline
```

## Step 6 — See your score on GitHub

After every push, GitHub runs the same checks automatically:

1. Open your repository on github.com and click the **Actions** tab.
2. Click the latest run, called **Check answers**. It shows a yellow dot while running, then a green ✓ or a red ✗ (about 30–60 seconds).
3. Scroll down on the run's **Summary** page to see your **Score: X/15** table, with a hint for each failing exercise.

A red ✗ only means some exercises aren't passing yet. Fix them, commit, push again, and a new run starts.

---

## Rules

- **Don't edit anything in `tests/` or `.github/`.** Your instructor grades with an original copy of the tests, so changing them won't change your grade.
- **Don't rename functions or change their parameters.** The checker calls them by name.
- **Your own work.** You may use your class notes and the Python docs. Discussing ideas with classmates is fine, but don't copy code.
- **Don't commit the `.venv` folder.** The included `.gitignore` already skips it.

## Git cheat sheet

| Command | What it does |
| --- | --- |
| `git clone <url>` | Download a repository to your computer (once) |
| `git status` | Show what has changed since your last commit |
| `git add <file>` | Stage a file for the next commit (`git add .` stages everything) |
| `git commit -m "message"` | Save a snapshot of staged changes |
| `git push` | Upload your commits to GitHub |
| `git pull` | Download changes from GitHub (e.g. if you edited on the website) |
| `git log --oneline` | List your commits |
| `git diff` | Show exactly what you changed but haven't staged |
| `git restore <file>` | Throw away un-staged changes to a file (careful!) |

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `pytest: command not found` / `No module named pytest` | Activate `.venv`, then `python -m pip install -r requirements.txt`. |
| `ModuleNotFoundError: No module named 'part_a_basics'` | Run `pytest` from the repository's main folder, not from inside `assignment/` or `tests/`. |
| All tests show `None` errors | You still have `pass`, or you used `print` instead of `return`. |
| `IndentationError` / `SyntaxError` | The whole file fails. Fix the line number shown, and use 4 spaces for indentation. |
| A test hangs forever | You have an infinite `while` loop. Press Ctrl+C and check your loop condition. |
| `git push` rejected: *Updates were rejected… fetch first* | You changed something on github.com. Run `git pull`, then `git push`. |
| `git push` asks for a password or says *Authentication failed* | Redo Step 2: `gh auth login` then `gh auth setup-git`. |
| `nothing to commit, working tree clean` | You haven't saved the file in VS Code, or there are no changes since your last commit. |
| `Author identity unknown` | Run the two `git config --global` commands in Step 2. |
| No runs in the Actions tab | Make sure the `.github/workflows/check.yml` file exists, then push again. On a brand-new repository, enable Actions if GitHub asks. |
