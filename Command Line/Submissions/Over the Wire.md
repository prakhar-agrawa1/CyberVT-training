### Level 0

1. Opened PowerShell on my Windows PC
2. Ran command "ssh bandit0@bandit.labs.overthewire.org -p 2220"
3. Entered password "bandit0"

### Level 1

1. cat readme
2. Password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
3. exit
2. Ran command "ssh bandit1@bandit.labs.overthewire.org -p 2220"
4. Entered password

### Level 2

1. Searched Google for "dashed filename"
2. Simply running "cat -" isn't working because a dash is interpreted as the start to an option flag for a command
3. Ran command "cat ./-" to specify the present working directory
4. Password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

### Level 3

1. I started typing "cat ./-"
2. Pressed Tab to autofill
3. Filename presented as "--spaces\ in\ this\ filename--". The backslash character indicates that the next character isn't to be taken literally and is a continuation of the string provided.
4. Password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

### Level 4

1. Ran "cd inhere"
2. Ran <ls> - nothing. "ls -la" revealed a hidden file "...Hiding-From-You"