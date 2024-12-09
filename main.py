import platform
from analyzers.linux_analyzer import LinuxAnalyzer

if platform.system() == "Windows":
    from analyzers.windows_analyzer import WindowsAnalyzer

def main():
    source = input("Quelle source voulez-vous analyser ? (windows/linux) : ").lower()

    if source == "linux":
        logfile = input("Entrez le chemin du fichier journal Linux : ")
        analyzer = LinuxAnalyzer(logfile)
        analyzer.run()
    elif source == "windows":
        if platform.system() != "Windows":
            print("L'analyse des journaux Windows n'est disponible que sur Windows.")
        else:
            analyzer = WindowsAnalyzer()
            analyzer.run()
    else:
        print("Source non reconnue. Utilisez 'windows' ou 'linux'.")

if __name__ == "__main__":
    main()
