# VBScrambler - A Python-Based VBScript Code Obfuscator
![header image_vbscrambler](https://raw.githubusercontent.com/bobby-tablez/VBScrambler/main/assets/vbscrambler_header.png) 

VBScrambler is a Python based VBScript code obfuscator which essentially takes VBScript as a form of input, either file or inline code, and provides an obfuscated VBScript one liner as output. The obfuscation works by taking the original VBScript, performing a byte shift on the supplied code. It will then take the garbage-looking code and insert it into a randomly generated deobfuscation script in VB, which will reverse the byte shift and then execute its contents. 

The shift works similar to ROT13 with a randomly supplied shift value ranging from -5 to 7. Larger numbers tend to prevent the generated script from executing, producing errors. Other errors can occur when copying generated code from console, as special characters, especially in Linux, may not copy correctly. 

### Optional arguments:
- `-c, --content` Supply inline VBScript. (This must be the last argument supplied)
- `-f, --file` Supply a .vbs file to obfuscate (supports multi-line)
- `-o, --output` Save generated output to file [filename.vbs]
- `-s, --shift` Manually specify a shift value
If no argument is provided, the script will prompt the user for code to obfuscate.

![help image_vbscrambler](https://raw.githubusercontent.com/bobby-tablez/VBScrambler/main/assets/vbscrambler_help.png)

### Example:
Obfuscating the following VBScript using the command: `python3 VBScrambler.py -s 5 -f ps.vbs`
```VBScript
Dim shell,command
command = "powershell.exe -nologo -command ""New-Item C:\text\vbstest.txt -Force"""
Set shell = CreateObject("WScript.Shell")
shell.Run command,0
```
Generates the following VBScript code:
```VBScript
lgwi = "":for i = 1 to 163: lgwi = lgwi + chr(Asc(mid("Inr%xmjqq1htrrfsihtrrfsi%B%'ut|jwxmjqq3j}j%2stqtlt%2htrrfsi%''Sj|2Nyjr%H?ayj}ya{gxyjxy3y}y%2Ktwhj'''Xjy%xmjqq%B%HwjfyjTgojhy-'\Xhwnuy3Xmjqq'.xmjqq3Wzs%htrrfsi15",i,1)) - (5)):Next:Execute lgwi:
```

#### Errors and issues
After extensively testing various VBScripts, I've discovered that certain scritps will produce errors with specific shift number combinations (typically 1 out of 10) when using the default provided range. If you encounter an error, try either adjusting the shfit number manually, or simply run it again to get a potentially new value. 

Another issue occurs in Linux more often than in Windows where the console doesn't properly print the shifted ASCII characters properly, thus copying the printed code could skip some characters. If you run into this, use the `-o` option to print to a file and use a text editor such as Sublime which handles special characters well. 

#### Future plans
- Support for JScript, selectable via flags

**DISCLAIMER: Use at your own risk, for educational and demonstration purposes only!**
