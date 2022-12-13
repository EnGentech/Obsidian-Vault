### running git  add commit and push with bash command
```bash
#!/bin/bash`  
i=1;
msg=""; 
for word in "$@" 
do 
msg+="${word} ";  
i=$((i + 1));  
done;
echo "$msg";

git status
git add .  
git status 
git commit -m "$msg" 
git push
```

My description
```bash
#!/bin/bash
git add .                                                                                     git status                                                                                    echo "Enter commit message"                                                                   read commit                                                                                   git commit -m "$commit"                                                                       git push                                                                                                
```

Add scripts to bash
```shell
echo $PATH
export PATH=$PATH:directory (~/bin)
```

when a command is entered where tap is needed to complete the directory, press tap twice to reveal all contents 
e.g
```bash
		cd m
		# using tap twice will list all directories with m as the head content
```

#### Manipulating escape sequence
```bash
mkdir "\\*\\\\'\"Best School\"\\'\\\\*$\\?\\*\\*\\*\\*\^C\\*:)"/Best School  
```

confusing task 17 on shell variables 
```shell
echo $(printf %o $(($((5#$(echo $WATER | tr 'water' '01234'))) + $((5#$(echo $STIR | tr 'stir.' '01234'))))) | tr '01234567' 'behlnort')
```

