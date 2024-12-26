this is a readme file

##################################
# Git tutorial for High School Kids.
##################################


## Most Common Git Commands

- `git init`
    - Initializes a new Git repository
    
- `git add`
    - Adds files to the staging area
    - Usage: `git add <filename>` or `git add .` for all files
    
- `git commit -m "message"`
    - Creates a new commit with staged changes
    - Always include a meaningful commit message
    
- `git push`
    - Uploads local commits to the remote repository
    - Usage: `git push origin <branch-name>`
    
- `git pull`
    - Downloads changes from the remote repository
    - Updates your local branch with remote changes
    
- `git clone`
    - Creates a copy of a remote repository
    - Usage: `git clone <repository-url>`


# sets up Git with your name
git config --global user.name "<Your-Full-Name>"

# sets up Git with your email
git config --global user.email "<your-email-address>"

# creates a new repository
git init

# adds a file to the repository
git add <file-name>

#git status command is the key to Git’s mind
$ git status

# commits the changes to the repository
git commit -m "message"

# pushes the changes to the remote repository
git push

# pulls the changes from the remote repository
git pull

# clones a repository from a remote repository
git clone <repository-url>

# creates a new branch
git branch <branch-name>

# switches to a branch
git checkout <branch-name>

# merges a branch into the current branch
git merge <branch-name>

# deletes a branch
git branch -d <branch-name> 

# shows the commit history
git log

# shows the commit history in a single line
git log --oneline

# shows the commit history in a single line with graph
git log --oneline --graph --all

# shows the commit history in a single line with graph and decorate
git log --oneline --graph --all --decorate
