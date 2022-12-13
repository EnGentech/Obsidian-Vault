```git
git config -l

git config --global remote.origin.url "https://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@github.com/EnGentech/alx-pre_course.git"
```
the above list all the configuration of the github

backup of configuration
path to access emacs ~/.gitconfig
```github
[user]
        name = EnGentech
        email = engen.inyang@gmail.com
[core]
        excludesfile = /root/.gitignore_global
[credential]
        helper = cache
[remote "origin"]
        url = https://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@github.com/EnGentech/alx-pre_course.git
```

Resolving issues with git permission palava
```git
emacs ~/.gitconfig

emacs .git/config
```

## Creating a root running script
save your script to ~/bin directory, run the below code in your terminal
```bash
emacs ~/.bashrc
#on the editor environment, carry out the following
#go to the end of line within that page
#enter the bellow code
PATH=$PATH:~/bin
#exit the terminal and reload, the script should work
```

Ignoring password on git 
```git
git config --global credential.helper store
git config --global credential.helper cache
```
or
```git
git remote set-url origin git@github.com:username/your-repo.git
```

### Git branch
```git
git branch -b "branch name"

the above code will create a branch and the same time checkout to that branch

```

## SSH key better than http
on the terminal type
```git
ssh-keygen
```
on the display press enter key until the terminal return with a string of matrix offsets, locate the folder describe via the local directory, open the file and copy the ssh key with the publisher logo.
go to your github, click on settings.
locate ssh key 
clidk new
paste the key and add a name to it (optional)
save it
now clone your remote repo to your system using the url and not http
with this you will be pushing to github with no prompt for password