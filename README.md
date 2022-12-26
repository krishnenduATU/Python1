# Python
This repository contains Python exercises from the Infrastructure as Code (IaC) module's work during weeks two to five. This will students to develop Python programming skills.

Git Branching Strategy

It is useful in separating code that is currently in development and stable code for production environments. Below branches are created for this project :

- Dev - Code development starts at this branch, features are added first to this branch.
- Test - For extensive testing and bug fixes.
- Main - Current State of production environment, contains only stable codes.
- Feature - Created from Dev branch to add new features in codes.
- Bug Fix - Created from test branch to fix bugs in codes.

The "main" branch stores only stable code and needs to be protected from accidental commits. This is done by setting branch protection rules to this branch. Here, before pulling/merging requests to "main" branch, it requires atleast one approver with write permissions in the repository or from a designated code owner to review the changes.
