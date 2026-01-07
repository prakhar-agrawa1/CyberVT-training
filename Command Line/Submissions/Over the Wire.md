### Setup

1. Opened PowerShell on my Windows PC
2. Ran command "ssh bandit0@bandit.labs.overthewire.org -p 2220"
3. Entered password "bandit0"

### Level 0

1. cat readme
2. Password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
3. exit
2. Ran command "ssh bandit1@bandit.labs.overthewire.org -p 2220"
4. Entered password

### Level 1

1. Searched Google for "dashed filename"
2. Simply running "cat -" isn't working because a dash is interpreted as the start to an option flag for a command
3. Ran command "cat ./-" to specify the present working directory
4. Password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

### Level 2

1. I started typing "cat ./-"
2. Pressed Tab to autofill
3. Filename presented as "--spaces\ in\ this\ filename--". The backslash character indicates that the next character isn't to be taken literally and is a continuation of the string provided.
4. Password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

### Level 3

1. Ran "cd inhere"
2. Ran "ls", - nothing. "ls -la" revealed a hidden file "...Hiding-From-You"
3. Ran "cat ./...Hiding-From-You"
4. Password: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

### Level 4

1. Ran "cd inhere"
2. There were many dashed files, only one human-readable.
3. Ran "cat ./*" and found some human-readable string that should be the password.
4. Turns out there were additional characters at the start of the string from the previous unreadable file. -file07 is the right one.
5. Password: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

### Level 5

1. inhere is filled with distraction directories filled with distraction files.
2. Searched google for "find" command options that could help me with the provided parameters i.e. file size.
3. Ran "find . -size 1033c"
4. Password: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

### Level 6

1. Ran "find /home -size 33c -user bandit7 -group bandit6"
2. Permission denied for everything.
3. Ran "find find / -size 33c -user bandit7 -group bandit6 2>&1 | grep -v "Permission denied"". What this does is first combine stderror into stdout with "2>&1", or send 2 (stderror) into 1 (stdout). Then, it pipes the entire output into the grep command with the -v option disclude any line containing "Permission denied".
4. Still outputed errors "no such file or directory", but it was narrowed down a lot. Found file "/var/lib/dpkg/info/bandit7.password"
5. Password: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

### Level 7

1. I tried catting "data.txt", and it was filled with lines upon lines of distraction text.
2. Instructions said the password was next to the word "millionth", so I ran "grep millionth data.txt"
3. Password: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

### Level 8

1. I read through the "Commands you may need to solve this level", and found one that should help: the "uniq" command.
2. Read online that I should sort first, as uniq only detects adjacent matching files.
3. Ran "sort data.txt | uniq -u". The -u option made it so that ONLY the unique line outputted.
4. Password: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

### Level 9

1. Running grep directly gives me a "binary file matches" error, meaning that it won't search within a file detected to be binary. To override this, I need to use option -a
2. Ran "grep -a "===" data.txt" which narrowed down enough.
3. Password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

### Level 10 - Base64

    Base64 is an encoding algorithm that converts data into binary and then base64 characters (a-z, A-z, 0-9, = and /) --> 26 + 26 + 10 + 2 = 64. Why 64? Because 2^6 = 64. This means that each base64 character is 6 bits instead of 8 like in a byte. Why do we use it? Because transmission channels usually handle 8-bit, text-based data, and data such as binary can get corrupted. Therefore, base64 works for all data down to binary.

1. Ran "base64 -d data.txt" to decode the file.
2. Password: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

### Level 11 - Rot13

1. File uses rot13 encoding. I can use rot13 again to decode since the alphabet is 26 letters.
2. Searched online for a rot13 encoder/decoder, pasting in the string that is the length of a flag.
3. Password: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

### Level 12 - Hex Dump

    Recall that a hexidecimal digit is 4 bits, and 2^4 = 16 (0-9, a-f) --> 10 + 6 = 16. 1 byte of data (8 bits) can be represented by a two-digit hexadecimal number, 4 and 4 bits.

    In a hex-DUMP, the left-most column represents memory address, or where the data in its row fits in order.

1. I cd'd into /tmp and ran "mkdir (temp directory)" to create temp dir for myself
2. I ran "mkdir bandit12" for level 12, and cd'd into it.
3. I ran "cp ~/data.txt ./data.txt" to copy data from bandit12 into my own dir
4. Ran "xxd -r data.txt > data2.txt" to reverse hexdump on the data textfile and save it as "data2".
5. Ran "file data2.txt" to understand this file. Outputted "gzip compressed data, was "data2.bin"".
6. I tried to run "gzip -d data2.txt", but it gives error "unknown suffix -- ignored". Searched online and learned that the file must end in .gz to decompress.
7. Ran "mv data2.txt data2.gz" to set it as the correct filetype.
8. Ran "gzip -d data2.gz" to decompress from gz.
9. Ran "file data2" and it is now "bzip2 compressed data".
10. Ran "mv data2 data2.bz2"
11. Ran "bzip2 -d data2.bz2" to decompress from bz.
12. Ran "file data2" again. It is gzip compressed again.
13. "mv data2 data2.gz", "gunzip data2.gz", "file data2" = "POSIX tar archive (GNU)".
14. Searched online since "tar --help" outputted way too much. Ran "mv data2 data2.tar" then "tar -xf data2.tar" to extract the directory.
15. I end up with a data5.bin, which is another tar archive. Repeat tar extraction steps to get data6.bin, which is bzip2 compressed. Repeat bzip2 decompress steps to get data7.bin, which is another tar archive. This leads to data8.bin, gzip compressed. Decompressing this finally leads to the password.
16. Password: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

### Level 13

1. I get a private sshkey, which should just let me ssh into bandit14. Searched online for using ssh keys to login instead of password.
2. Ran "ssh -i sshkey.private bandit14@host..."
3. Didn't work from within the server. I copied the file contents and pasted them into a text file in my own folder. Ran ssh again, and it worked.
4. Ran "cat /etc/bandit_pass/bandit14"
5. Password: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

### Level 14

1. Ran "nmap localhost" and found port 30000 open with service ndmps running. 
2. Ran "nc localhost 30000", established connection.
3. Sent bandit14 password and received bandit15 password.
4. Password: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

### Level 15

Reached