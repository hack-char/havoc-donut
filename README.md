# havoc-donut
Havoc C2 plugin to run shellcode with donut.
See [Havoc C2](https://github.com/HavocFramework/Havoc) and [Donut](https://github.com/TheWover/donut).

## Requires PR
Havoc C2 must have the shellcode spawn API PR https://github.com/HavocFramework/Havoc/pull/435.
Can use https://github.com/hack-char/Havoc/tree/add_shellcode_spawn_api

## Notes
* Must install and compile donut on the host you run your Havoc C2 client on. Must also install the donut python module.
* Add the havoc-donut.py plugin in the client: click scripts->script manager->Load Script and choose havoc-donut.py
  * havoc-donut.py is for the Havoc C2 'dev' branch and havoc-donut-main.py is for the 'main' branch
* If it gets loaded, can verify by typing 'help donut' in a listener window. Will see:
```
 - Command       :  donut
 - Description   :  Automatic shellcode generation and execution using Donut

  Command                   Description      
  ---------                 -------------     
  spawn                     Generate shellcode using Donut and spawn new process. Example: 'donut spawn something.exe param1 param2'
```

## To Do
* Implement inject and execute shellcode methods
* Add functionality to:choose x32, techniques for Havoc C2 as well as Donut, additional options for Donut




