log into python CLI
```python
import os
import sys
os.path.dirname(sys.executable)
```

to get all environment variable in windows
```cmd
set
```

for shell users
```shell
Get-ChildItem Env:
```

And if you want to list only the user variables, run this command: _
```shell
[Environment]::GetEnvironmentVariables("User")
```

About Environment variables: link: [What are environment variables in Windows? - Digital Citizen](https://www.digitalcitizen.life/simple-questions-what-are-environment-variables/)