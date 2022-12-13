### Using pandoc for file conversions
<!--using powershell-->
cd into  <!--C:\Users\Engr. Gentle\Documents\Obsidian Vault\Najib guide-->

<!--this command will be used to convert the content of obsidian into a pdf file-->
after the above navigation, 
type in the command
```powershell
pandoc --version
```
<!-- the above will  display the version  of the pandoc-->
```powershell
pandoc inputFileNameOnObsidien -o fileoutputname.extension

example pandoc '.\files send by najib.mc' -o beginners.pdf

pandoc -t slidy -s `changThis.md` -o `changeThis.html`

*note that the input file should reside in the active directory*

```
