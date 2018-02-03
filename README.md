# Anti-Duplicator

Gets path to folder and prints files with same name and size

# Quickstart

You have to start program with a patsh to folder as a parameter. See the following example.

Example of script launch on Linux, Python 3.5:

```bash

$ python duplicates.py <patsh to folder>

```
Launching on Windows via CMD or PowerShell is the same. 

Example:

```
$ python.exe E:/GitHub/devman/11_duplicates/duplicates.py E:\GitHub\devman\11_duplicates\foldertest\
Found 2 files copy1 — копия.txt with size 11 :
E:\GitHub\devman\11_duplicates\foldertest\copy1 — копия.txt
E:\GitHub\devman\11_duplicates\foldertest\subfolder1\copy1 — копия.txt
Found 3 files copy1.txt with size 5 :
E:\GitHub\devman\11_duplicates\foldertest\copy1.txt
E:\GitHub\devman\11_duplicates\foldertest\subfolder1\subsubfolder\copy1.txt
E:\GitHub\devman\11_duplicates\foldertest\subfolder2\copy1.txt
Found 2 files copy2.txt with size 21 :
E:\GitHub\devman\11_duplicates\foldertest\copy2.txt
E:\GitHub\devman\11_duplicates\foldertest\subfolder1\copy2.txt
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
