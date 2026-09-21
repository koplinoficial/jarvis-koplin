import subprocess


def abrir_chrome():
    subprocess.Popen(
        ["cmd", "/c", "start", "", "chrome"],
        shell=False
    )


def abrir_vscode():
    subprocess.Popen(
        ["cmd", "/c", "code"],
        shell=False
    )
    