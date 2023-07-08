this library is used in copying, cutting, pasting and compressing files in python. we will start with simple demonstration.

## Compress
```python
import shutil  
  
shutil.make_archive("myfile", 'zip', root_dir='Fabric python')
```
in the above python file, the myfile is used to create a zip file name, the zip is the file it will be created as an extension and the root of the directory at where the files will be created from is the Fabric python. 

We can fish out the files possibly to be created as an archive file in python using the code below
```python
import shutil  
  
print(shutil.get_archive_formats())
# This will list the possible file extensions that can be created using the shutil library in python 
```

## Unpacking zip files
After creating the files, you can unpack them with the code below
```python
import shutil  
  
shutil.unpack_archive("myfile.zip", extract_dir='./openme', format='zip')
```


