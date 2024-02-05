Get-ChildItem *.py | ForEach-Object {
  $_.Attributes = "Archive"
}
the ls -l equivalent in powershell
Get-ChildItem -Path . -Force | Select-Object Mode, LastWriteTime, Length, Name
