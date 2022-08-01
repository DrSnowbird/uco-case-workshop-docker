This repository provides resources for the CASE Workshop held the week of August 1, 2022.

The slides are here:

[`https://docs.google.com/presentation/d/137eapchBGFG8Uo0YJKRD3tleUJYItJ_Rl1wJ-ulSj90/edit`](https://docs.google.com/presentation/d/137eapchBGFG8Uo0YJKRD3tleUJYItJ_Rl1wJ-ulSj90/edit).


## Running sample code, and PowerShell logistics

This has scripts to run its tests and commands, but they are orchestrated in one of two mostly-equally-functional ways:

1. Make (for Linux, macOS, and Windows users with Windows Subsystem for Linux)
2. Powershell (for Windows users)

Often, PowerShell execution is disabled by policy.  Consider running the following command in order to run the tests in this repository:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

If you are able to respond `Y` to the prompt, your current PowerShell session will be permitted to run scripts.  The directories with scripts to run during the workshop have a file named `check.ps1`, callable with:

```powershell
.\check.ps1
```
