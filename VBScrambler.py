import argparse
import random
import string

banner = r"""
____   ______________   _________                               ___.    .__       
\   \ /   /\______   \ /   _____/  ____ _______ _____     _____ \_ |__  |  |    ____ _______  
 \   Y   /  |    |  _/ \_____  \ _/ ___\\_  __ \\__  \   /     \ | __ \ |  |  _/ __ \\_  __ \ 
  \     /   |    |   \ /        \\  \___ |  | \/ / __ \_|  Y Y  \| \_\ \|  |__\  ___/ |  | \/ 
   \___/    |______  //_______  / \___  >|__|   (____  /|__|_|  /|___  /|____/ \___  >|__|    
                   \/         \/      \/             \/       \/     \/            \/ 
        VBScrambler by GH: @Bobby-Tablez
        https://github.com/bobby-tablez/VBScrambler

"""
print(banner)
def main():

    parser = argparse.ArgumentParser(description="VBScrambler")
    parser.add_argument("-c", "--content", nargs=argparse.REMAINDER, help="VBScript one liner.", default=[], required=False)
    parser.add_argument("-f", "--file", type=str, help="VBScript file.", required=False)
    parser.add_argument("-o", "--output", type=str, help="Output file to save the scrambled VBScript to", required=False)
    parser.add_argument("-s", "--shift", type=int, help="Manually set the ROT/Shift number", required=False)

    args = parser.parse_args()

    # Handle the various input types
    if args.content:
        vbsCode = ' '.join(args.content)
    elif args.file:
        try:
            with open(args.file, 'r') as file:
                vbsCode = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{args.file}' does not exist.")
            return
    else:
        vbsCode = input("Provide a VBScript one-liner (Mind your quotes!):")

    if args.shift:
        shiftNum = args.shift
    else:
        shiftNum = random.randint(-5, 7) # Define range for byte shifts. This range seems to work well with most VBScripts. Increasing this could break the generated script
    
    obfuscatedVBS = ''.join(chr(ord(v) + shiftNum) for v in vbsCode)
    
    vbs_len = len(obfuscatedVBS)
    
    # Fix double quotes if they're generated after the shift
    finalVBS = obfuscatedVBS.replace('"', '""')
    
    # Ranomize variable name
    vbVar = ''.join(random.choices(string.ascii_letters, k=4))

    # Generate the output
    stringbuilder = (vbVar + r' = "":for i = 1 to ' + f"{vbs_len}" + ": " + vbVar + f" = {vbVar} + chr(Asc(mid(\"{finalVBS}\",i,1)) - ({shiftNum})):Next:Execute " + vbVar + ":")

    # Either save output as a file, or print it based on paramaters used
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(stringbuilder)
            print(f"\nContent saved to {args.output}\n")
        except IOError as e:
            print(f"\nError writing to file: {e}\n")
    else:
        print(f"\n{stringbuilder}\n")

if __name__ == "__main__":
    main()
