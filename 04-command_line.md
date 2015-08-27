# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

Cheat Sheet:

pwd outputs the name of the current working directory.

ls lists all files and directories in the working directory.
	These are some of ls’s options
	-a will show you files with a . in front of them, hidden files. 
	-l lists all fcontents in long form which shows: access rights, hard l 			links, username of file’s owner, group that owns file, size in 			bytes, date modified
	-t order files and directories by last time they were modified
	-alt uses multiple options at once. when used with ls, it would do 			all of the above options

cd switches you into the directory you specify.
	cd .. will move you up one directory
	cd ../../ will go up to directories 

mkdir creates a new directory in the working directory.

touch creates a new file inside the working directory.

working with files

cp if we do cp frida.txt lincoln.txt, we are copying the contents of frida into lincoln. Or, if we do cp cleopatra.txt historical/, it 
will copy cleopatra.txt into the historical/ directory. 
	cp * satire/ will copy all files, since * is a wildcard, into 			satire/
	cp m*.txt satire/ will copy all files starting with m and 			ending in .txt into satire/

mv will  move a file to another place. mv superman.txt superhero/ will move superman.txt into superhero/ directory. You can also add another source file and it will move both to the new directory. 
You can also rename a file with mv. We can rename superman to spiderman by doing mv superman.txt spiderman.txt

rm will delete files and directories that follow it. 
The -r option modifies the behavior of the rm command. it stands for “recursive,” and it deletes the directory and all it’s child directories.
Also, there isn’t an undelete button, so this is serious and permanent!

which will tell you where something is. 
—-version will tell you which version of the thing you have. 

cat somefile.txt will display contents of somefile.txt
cat > somefile.txt  will read whatever you type next and then write it to that file. ctrl d will close the file so you stop writing in it. 
cat file1 file2 will concatenate file1 and file2. 



grep 'word' filename will search filename for word. adding -i after grep will make it ignore case. 
grep -r ‘word' filename will search recursively, which is to say for all files in a directory, for that word. 




---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls lists the contents of the working directory. 
ls -a shows the hidden files, which is to say those with a . in front of them. 
ls -l lists the contents in long form with more metadata such as user access rights and date modified. 
ls -lh adding the h will make the size more readable by listing it in b, kb, etc. The numbers are restricted to 3 characters.


---


---

What does `xargs` do? Give an example of how to use it.

REPLACE THIS TEXT WITH YOUR RESPONSE

---
