# Git Expert Walkthrough — ML Project
## Your Complete Step-by-Step Playbook

---

## THE PROJECT OVERVIEW

You have an ML pipeline with two files that need improvement:
- `src/data_cleaning.py` → Branch: feature/data-cleaning
- `src/model.py`         → Branch: feature/model-enhancement

Two developers (you playing both roles) improve these in parallel,
then both get merged back to main via Pull Requests.

---

## STEP 0 — Configure Git on Your Machine
> WHY: Git needs to know WHO you are. Every commit is stamped with your
> name and email. This is how GitHub knows which commits belong to your account.

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Set your default branch name to 'main' (modern standard):
```bash
git config --global init.defaultBranch main
```

Verify your config:
```bash
git config --list
```

You should see user.name and user.email in the output.

---

## STEP 1 — Create a GitHub Repository (do this on GitHub.com)
> WHY: GitHub is your remote — the central "source of truth" that all
> collaborators sync with. Local git alone = no backup, no collaboration.

1. Go to https://github.com/new
2. Repository name: ml-pipeline-git-practice
3. Description: Learning Git branching with an ML project
4. Set to Public (so you can open free PRs)
5. ✅ Check "Add a README file" — NO (we'll push our own)
6. Click "Create repository"

GitHub will show you a URL like:
  https://github.com/YOUR_USERNAME/ml-pipeline-git-practice.git

Copy this URL — you'll need it in Step 3.

---

## STEP 2 — Initialize Git Locally
> WHY: `git init` creates a hidden .git folder that tracks all your history.
> Without this, git doesn't know this folder is a repo.

Navigate to your project folder (wherever you saved the ml_project files):
```bash
cd path/to/ml_project
git init
```

You'll see: "Initialized empty Git repository in .../ml_project/.git/"

Check the status of your files:
```bash
git status
```

> WHY git status: This is your most-used command. It shows:
> - Untracked files (new files git doesn't know about yet)
> - Modified files (changed since last commit)
> - Staged files (ready to be committed)

---

## STEP 3 — Connect Your Local Repo to GitHub (Remote)
> WHY: "origin" is the conventional nickname for your GitHub remote.
> Think of it like saving a contact — instead of typing the full URL
> every time, you just say "origin".

```bash
git remote add origin https://github.com/YOUR_USERNAME/ml-pipeline-git-practice.git
```

Verify the remote was added:
```bash
git remote -v
```

You should see:
  origin  https://github.com/YOUR_USERNAME/... (fetch)
  origin  https://github.com/YOUR_USERNAME/... (push)

---

## STEP 4 — Stage and Commit to Main (First Commit)
> WHY Staging: Git has a 2-step commit process:
>   1. Stage (git add)   — "I want THESE changes in my next commit"
>   2. Commit (git commit) — "Save this snapshot forever"
> This lets you commit only part of your changes deliberately.

Stage ALL files:
```bash
git add .
```

Check what's staged:
```bash
git status
```

You should see all files under "Changes to be committed" in green.

Make your first commit:
```bash
git commit -m "Initial commit: base ML pipeline with data cleaning and model"
```

> WHY good commit messages: They are your project's history. Future you
> (and teammates) will read these to understand WHAT changed and WHY.
> Format: present tense, concise, specific.

---

## STEP 5 — Push Main to GitHub
> WHY: Your commit only exists locally so far. Push sends it to GitHub.
> The -u flag sets "upstream" — after this you can just type `git push`.

```bash
git push -u origin main
```

Go to GitHub and refresh — you'll see all your files! 🎉

---

## STEP 6 — Create Branch: feature/data-cleaning
> WHY Branches: A branch is an independent line of development.
> You're creating a copy of main where you can make changes safely
> without affecting the working code in main.
> 
> Think of it like: main is the live production website.
> The branch is your local dev environment where you experiment.

Create and switch to the new branch in one command:
```bash
git checkout -b feature/data-cleaning
```

Verify you're on the new branch:
```bash
git branch
```

The * shows your current branch. You'll see:
  * feature/data-cleaning
    main

> WHAT HAPPENED INTERNALLY: Git created a new pointer called
> "feature/data-cleaning" pointing at the same commit as main.
> Both branches are identical right now. Changes you make here
> will NOT touch main.

---

## STEP 7 — Make Improvements on feature/data-cleaning

Now replace the contents of src/data_cleaning.py with the improved v2 version.
(Copy the content from src/data_cleaning_v2.py into src/data_cleaning.py)

After making your edits, check what changed:
```bash
git diff
```

> WHY git diff: Shows you line-by-line what changed BEFORE staging.
> Red = removed, Green = added. Very useful to review before committing.

Stage only the data_cleaning.py file (deliberate staging!):
```bash
git add src/data_cleaning.py
```

Commit with a descriptive message:
```bash
git commit -m "feat: improve data cleaning with smart null handling and outlier clipping

- Replace dropna() with median imputation for numeric columns
- Only drop rows where target label is missing
- Add clip_outliers() to handle extreme values
- Add column validation to catch schema issues early
- Add structured logging throughout"
```

> WHY multi-line commit messages: The first line is the "subject" (shown in
> git log summaries). The blank line + bullet points are the "body" explaining
> the WHY. This is professional-grade commit hygiene.

Check your git log:
```bash
git log --oneline
```

You'll see your new commit on top. main is still at the initial commit.

---

## STEP 8 — Push feature/data-cleaning to GitHub
> WHY: Push this branch so it's on GitHub. This is what allows you
> to open a Pull Request. The -u sets upstream for this branch.

```bash
git push -u origin feature/data-cleaning
```

---

## STEP 9 — Switch Back to Main, Create feature/model-enhancement
> WHY checkout main first: We want model-enhancement to branch from
> main — NOT from data-cleaning. These are parallel workstreams.
> If we branched from data-cleaning, we'd have a dependency.

```bash
git checkout main
```

Confirm you're back on main:
```bash
git branch
```

Now create the model branch:
```bash
git checkout -b feature/model-enhancement
```

---

## STEP 10 — Make Improvements on feature/model-enhancement

Replace the contents of src/model.py with the improved v2 version.
(Copy content from src/model_v2.py into src/model.py)

Stage and commit:
```bash
git add src/model.py
git commit -m "feat: enhance model with pipeline, scaling, and cross-validation

- Wrap model in sklearn Pipeline (scaler + classifier)
- Add StandardScaler so feature magnitudes don't dominate
- Switch from LogisticRegression to RandomForestClassifier
- Add 5-fold cross-validation for reliable performance estimates
- Add classification_report and confusion_matrix for diagnostics
- Add stratify=y to train_test_split to preserve class distribution"
```

Push this branch:
```bash
git push -u origin feature/model-enhancement
```

---

## STEP 11 — Open Pull Requests on GitHub
> WHY Pull Requests (PRs): A PR is a formal request to merge your branch
> into main. It allows:
>   - Code review before merging
>   - Discussion and comments on specific lines
>   - CI/CD checks to run automatically
>   - An audit trail of WHY code was added
> 
> Even solo developers use PRs for self-review and clean history.

### PR 1: feature/data-cleaning → main

1. Go to your GitHub repo
2. You'll see a yellow banner: "feature/data-cleaning had recent pushes"
3. Click "Compare & pull request"
4. Fill in:
   - Title: "feat: improve data cleaning with robust null handling and outlier clipping"
   - Description (paste this):
     ```
     ## What this PR does
     Replaces the basic data cleaning logic with a production-grade version.
     
     ## Changes
     - Smart null handling: median imputation instead of dropping rows
     - Outlier clipping at 1st/99th percentile
     - Column schema validation on load
     - Structured logging for observability
     
     ## Why
     The original dropna() was silently deleting valid rows that just had
     one missing numeric field. Median imputation preserves those rows.
     ```
5. Click "Create pull request"

### PR 2: feature/model-enhancement → main

Repeat the same steps for the model branch.

---

## STEP 12 — Merge the PRs

### Merge PR 1 (data-cleaning)
On GitHub, on the first PR page:
1. Review the file diffs (the "Files changed" tab)
2. Click "Merge pull request"
3. Click "Confirm merge"
4. Click "Delete branch" (good hygiene — the work is merged, branch is done)

### Bring main up to date locally
> WHY git pull: The merge happened on GitHub (remote). Your local main
> still shows the old code. Pull brings the remote changes down.

```bash
git checkout main
git pull origin main
```

Now check the log:
```bash
git log --oneline
```

You'll see the merge commit from PR 1.

### Merge PR 2 (model-enhancement)
Go back to GitHub and merge the second PR the same way.

Then pull again locally:
```bash
git pull origin main
git log --oneline
```

---

## STEP 13 — Clean Up Local Branches
> WHY: Once branches are merged, delete them locally too.
> Stale branches are clutter and can cause confusion.

```bash
git branch -d feature/data-cleaning
git branch -d feature/model-enhancement
```

> The -d flag is "safe delete" — it only deletes if the branch
> is fully merged. Use -D (capital) to force delete.

Final check — you should only have main:
```bash
git branch
```

---

## BONUS — Useful Commands to Know

```bash
# See a pretty visual graph of your branches
git log --oneline --graph --all

# See who changed what line in a file
git blame src/model.py

# Temporarily save uncommitted work (switch branches safely)
git stash
git stash pop

# See difference between two branches
git diff main..feature/data-cleaning

# Undo the last commit (keep changes, un-stage them)
git reset HEAD~1

# See full history with author and dates
git log --stat
```

---

## THE MENTAL MODEL

WORKING DIRECTORY → (git add) → STAGING AREA → (git commit) → LOCAL REPO → (git push) → GITHUB (REMOTE)

GitHub (REMOTE) → (git pull / git fetch) → LOCAL REPO

Branches = parallel timelines
Commits = snapshots (not diffs!)
Main = the trunk all branches eventually rejoin

---
You're now a Git practitioner. Repeat this workflow on every project
and it becomes muscle memory. 🚀
