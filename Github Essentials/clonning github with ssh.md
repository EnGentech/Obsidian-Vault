1. Create or generate an ssh token on the folder you will clone 
```git
ssh-keygen
or
ssh-keygen -t ecdsa -b 521 -C "your_email@example.com"
```
2. copy and paste the code in the /root/.ssh/id_rsa.pub
3. to ensure you have done the right thing, put in the code below
```git
ssh -T git@github.com
```
4. if there's no error, head to your git repository and clone the repository to your local machine

that was pretty simply right!! smiles