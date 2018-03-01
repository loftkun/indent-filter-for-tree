indent filter for tree
==================================================

# What it is?
filter for tree command.  
can indent directories and files without using indentation line.  
for linux ( filter.sh ) and windows ( filter.ps1 ).

## for Linux
### Prerequisites
- jq
- python3.x

### Usage
```bash
tree [${TARGET_DIRECTORY}] -J | ./filter.sh
```

### example
tree command only
```bash
$ tree ./directory0
./directory0
├── directory1
│   ├── directory2
│   │   ├── directory3
│   │   └── file3
│   └── file2
└── file1
```
tree commnad with filter
```bash
$ tree ./directory0 -J | ./filter.sh
./directory0/
        directory1/
                directory2/
                        directory3/
                        file3
                file2
        file1
$
```

<br>
## for Windows
### Prerequisites
- Windows Powershell

### Usage
create filter (see filter.ps1.)
```powershell
PS C:\test> filter ToIndent {
>> % { $_ -replace "^(.*[+,\\\\]-.*)$","$&\" } |
>> % { $_ -replace "\|   " ,"`t" }  |
>> % { $_ -replace "\+---" ,"`t" }  |
>> % { $_ -replace "\\---" ,"`t" }  |
>> % { $_ -replace "    "  ,"`t" }  |
>> % { If ( $_ -notmatch "`t+$" ){$_} }
>> }
```
use filter
```powershell
tree /F /A | ToIndent
```
### example
tree command only
```powershell
PS C:\test> tree .\directory0
C:\TEST\DIRECTORY0
└─directory1
    └─directory2
        └─directory3
PS C:\test>
```
tree commnad with filter
```powershell
PS C:\test> tree .\directory0 /F /A | ToIndent
C:\TEST\DIRECTORY0
        file1
        directory1\
                file2
                directory2\
                        file3
                        directory3\
PS C:\test>
```
