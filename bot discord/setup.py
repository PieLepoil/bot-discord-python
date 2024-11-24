
try:
    import sys
    import os

    if sys.platform.startswith("win"):
        print("Installing the python modules required for the bot:")
        os.system("cls")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        os.system("pip install requests")
        os.system("pip install discord.py ")
        os.system("pip install json")
        os.system("pip install asyncio")
        os.system("pip install py")
        



except Exception as e:
    print(e)
    os.system("pause") 