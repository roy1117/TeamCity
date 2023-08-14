def start_codesys():
    with open("start_codesys.bat", 'w') as fp:
            fp.write('start /b /wait CoDeSys.exe --profile="CoDeSys V3.5 SP16" --runscript="server_script.py"')

if __name__ == "__main__":
    start_codesys()
