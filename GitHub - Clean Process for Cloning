

# Clean Process for Cloning and Merging Repositories
# ================================================

## 1. Backup Local Repository
# Create a backup of your local repository for safety
cp -r /path/to/your/local/repo /path/to/backup/repo_backup_$(date +%Y%m%d)

## 2. Clone Remote Repository
# Fetch the exact current state of the remote repository into a new directory
# This ensures you have all remote files (README.md, LICENSE, etc.) locally
git clone https://github.com/mridulja/demo-git-training.git
cd demo-git-training

## 3. Merge Local Files (If Required)
# Copy existing local files into the cloned repository
# This preserves your local changes while maintaining the remote repository structure
cp -r /path/to/your/local/files/* .

## 4. Stage and Commit Changes
# Track and record all local changes in Git
git add .
git commit -m "feat: merge local files with remote repository
- Integrated local changes with remote repository structure
- Preserved existing functionality while adding remote files"

## 5. Synchronize with Remote
# Pull remote changes and resolve any conflicts
# The --allow-unrelated-histories flag enables merging repositories with different histories
git pull origin main --allow-unrelated-histories

# Resolve any conflicts if they occur
# Use git status to check for conflicts
# Edit conflicting files manually if needed
# Then stage and commit resolved conflicts:
# git add .
# git commit -m "chore: resolve merge conflicts"

## 6. Update Remote Repository
# Push all changes to remote repository
git push origin main

# Verify Changes
# Check repository status and commit history
git status
git log --oneline -n 5
