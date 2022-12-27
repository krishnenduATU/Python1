# PowerShell

### Table of Contents
**[Description](#description)**<br>
**[Requirements](#requirements)**<br>
**[Tested On](#tested-on)**<br>
**[Overview](#overview)**<br>
**[Git Branching Strategy](#git-branching-strategy)**<br>
**[Bug Fix Request](#bug-fix-request)**<br>
**[Feature Request](#feature-request)**<br>
**[Authors](#authors)**<br>
**[Conclusion](#conclusion)**<br>

# Description
This PowerShell repository covered the fundamental concepts of PowerShell and provided a practical method for honing scripting skills. In accordance with the Exercises provided and research on the same, learners should be able to use PowerShell to automate a wide range of tasks, to manage enterprise infrastructure using PowerShell's Desired State Configuration (DSC) framework, and to control nearly every aspect of the Windows operating system.

## Requirements
- Operating System : > Windows-10
- PowerShell :  > PowerShell 5.1.22621.963

## Tested On

Windows-10-10.0.22621-SP0 with PowerShell version 7.3.0

## Overview

| Exercises   |      Description     | 
|----------| :---------------|
| Exercises_01 | To comprehend assignment, operators, and variables' interactions   | 
| Exercises_02 | To understand the importance of comments and docstrings while writing scripts   | 
| Exercises_03 | To explore the use of Python's data structures |
| Exercises_04 | To begin writing Python code that uses control flows and statements  | 
| Exercises_05 | To illustrate use of functions for code reuse | 
| Exercises_06 | To understand modules, and packages in Python| 
| Exercises_07 | To systematically handle errors in Python |
| Exercises_08 | To improve scalability and code reuse via Object-Oriented (OO) coding | 
| Exercises_09 | To develop Python tests that effectively demonstrate unit testing | 
| Exercises_10 | To demonstrate use of Python standard libraries  |
| Exercises_11 | To demonstrate how Python can be used to manage network utilities  | 
| Exercises_12 | To delve into the Python project structure  | 

## Git Branching Strategy

An efficient branching strategy is useful in separating code that is currently in development from stable code for production environments. Below are the branches created for this project:

- Main: Current State of the production environment, contains only stable codes.
- Dev: Code development starts at this branch, features are added first to this branch.
- Test:  For extensive testing and bug fixes.
- Feature: Created from the development branch to add new code features.
- Bug Fix: Created from the test branch to fix code bugs.

The "main" branch stores only stable code and needs to be protected from accidental commits. This is done by setting branch protection rules for this branch. Here, before pulling/merging requests to the "main" branch, it requires at least one approver with write permissions in the repository or from a designated code owner to review and approve the changes.

![image](https://user-images.githubusercontent.com/119352610/209552683-8e19d791-8e86-4ff9-9212-3cecc11ce98a.png)


## Bug Fix Request

Reported bugs can be found at [Bug Fix](https://github.com/krishnenduATU/Python/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)  

If developers encounter a bug with one of the Python programs, please follow the below steps:
- A "Bug" issue is created for the identified bug as shown below.

![image](https://user-images.githubusercontent.com/119352610/209512161-854ed88e-c16c-474d-b11d-da1ad1154951.png)

- Clone the Python repo to local machine.
```
git clone https://github.com/krishnenduATU/Python.git
``` 

- A new branch is created from the "test" branch, named "bug_fix_#<bug_fix_number>"
  
  ![image](https://user-images.githubusercontent.com/119352610/209512959-1c818968-b75a-4623-8da4-0d8ba7fb0074.png)

- A developer will work on the bug and fix the issue, then commit the changes. Make sure to add the bug fix number to the commit message, for example, "BugFix #4 : Corrected Pie value "
- Now merge the newly created bug fix branch into the "test" branch. Delete the bugfix branch once it has been merged.
- Checkout to "dev" branch and merge the changes made in the "test" branch so that all the branch are in same state..
- Push the changes on local "dev" and "test" branches to remote repo 
- In the end, the changes from "dev" branch is pulled to "main" branch and issue is closed in GitHub.
 
## Feature Request

Feature requests can be found at [Features](https://github.com/krishnenduATU/Python/issues?q=is%3Aissue+is%3Aclosed+label%3Aenhancement+)

To create a new feature in the Python programs, developer should follow below steps :

- A "Enhancement" issue is created as shown below.

![image](https://user-images.githubusercontent.com/119352610/209514336-9782f35b-9747-4cbf-8f4e-07a7eddee361.png)

- Clone the Python repo to the local machine.
```
git clone https://github.com/krishnenduATU/Python.git
``` 

- A new branch is created from "dev" branch, named "Feature_#<issue number>" as shown below.  

  ![image](https://user-images.githubusercontent.com/119352610/209512959-1c818968-b75a-4623-8da4-0d8ba7fb0074.png)
  
- Developer will work on the new feature. Then commits the changes. Make sure to add issue number to the commit message, for example "Feature #8 : Created UDP server and client scripts" to track the changes.
- Now, checkout to "dev" branch and merge the newly created feature branch. Delete the feature branch.
- Checkout to "test" branch and merge the changes made in "dev" branch so that all the branch are in same state.
- Push the changes on local "dev" and "test" branches to remote repo.
- In the end, the changes from "dev" branch is pulled to "main" branch and the feature request is closed in GitHub.

## Authors

This Python repository was developed as a part of Infrastructure as Code module's assignment by Krishnendu VP.  

## Conclusion

This Python repository covered the fundamental concepts of Python and offered a doable strategy for improving programming skills. In accordance with the provided exercises and research on the same, learners should be able to build and organise Python projects for network or server administration, log analysis, and the automation of routine tasks.


