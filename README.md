# Git Tutorial for High School Students

Welcome to the Git tutorial designed specifically for high school students. This guide will help you get started with Git, the popular version control system, and cover its most commonly used commands.

## Most Common Git Commands

- **`git init`**
    - Initializes a new Git repository.

- **`git add`**
    - Adds files to the staging area.
    - Usage: `git add <filename>` or `git add .` for all files.

- **`git commit -m "message"`**
    - Creates a new commit with staged changes.
    - Always include a meaningful commit message.

- **`git push`**
    - Uploads local commits to the remote repository.
    - Usage: `git push origin <branch-name>`.

- **`git pull`**
    - Downloads changes from the remote repository.
    - Updates your local branch with remote changes.

- **`git clone`**
    - Creates a copy of a remote repository.
    - Usage: `git clone <repository-url>`.

## Setting Up Git

Configure Git with your name and email:

```bash
# Sets up Git with your name
git config --global user.name "<Your Full Name>"

# Sets up Git with your email
git config --global user.email "<your-email-address>"
```

## Basic Git Commands

### Initializing a Repository

```bash
# Creates a new repository
git init
```

### Adding Files

```bash
# Adds a file to the repository
git add <file-name>

# Adds all files in the current directory
git add .
```

### Checking Status

```bash
# Checks the status of your repository
git status
```

### Committing Changes

```bash
# Commits the changes to the repository with a message
git commit -m "Your commit message"
```

### Pushing Changes

```bash
# Pushes the changes to the remote repository
git push
```

### Pulling Changes

```bash
# Pulls changes from the remote repository
git pull
```

### Cloning a Repository

```bash
# Clones a repository from a remote source
git clone <repository-url>
```

## Branch Operations

### Working with Branches

```bash
# Creates a new branch
git branch <branch-name>

# Switches to a branch
git checkout <branch-name>
```

### Merging Branches

```bash
# Merges a branch into the current branch
git merge <branch-name>
```

### Deleting a Branch

```bash
# Deletes a branch
git branch -d <branch-name>
```

## Viewing History

### Log Commands

```bash
# Shows the commit history
git log

# Shows the commit history in a single line
git log --oneline

# Shows the commit history with graph
git log --oneline --graph --all

# Shows the commit history with graph and decoration
git log --oneline --graph --all --decorate
```

## Best Practices

### Commit Messages

- Use clear, descriptive messages.
- Start with a verb (Add, Update, Fix, Refactor).
- Keep the first line under 50 characters.
- Add a detailed description if needed.

### Workflow Tips

1. **Check Status Frequently**
   - Use `git status` before commits.
   - Verify changes before pushing.

2. **Branch Management**
   - Create branches for new features.
   - Keep the `main` branch stable.
   - Delete merged branches.

3. **Regular Updates**
   - Pull changes frequently.
   - Resolve conflicts early.

## Common Issues and Solutions

If you make a mistake or encounter issues, refer to the [Git FAQ](https://git-scm.com/docs/git-faq) or seek help from the resources listed below.

## Additional Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com)
- [Interactive Git Learning](https://learngitbranching.js.org)

## Need Help?

- Check the [Git FAQ](https://git-scm.com/docs/git-faq).
- Join Git communities on [Discord](https://discord.com) or [Stack Overflow](https://stackoverflow.com).
- Ask your teacher or mentor.

*Last Updated: [Current Date]*
