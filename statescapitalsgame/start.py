import subprocess

def main():
    subprocess.run(["powershell.exe", "&",
     "'C:\\Program Files\\Java\\jdk-17.0.1\\bin\\java.exe'", 
     "'--module-path'", "'C:\\Users\\lukem\\Downloads\\openjfx-17.0.2_windows-x64_bin-sdk\\javafx-sdk-17.0.2\\lib'",
      "'--add-modules'", "'javafx.controls,javafx.fxml,javafx.media'", 
      "'-XX:+ShowCodeDetailsInExceptionMessages'",
       "'@C:\\Users\\lukem\\AppData\\Local\\Temp\\cp_2w181az48y1g2vvhmh4nmxqj3.argfile'",
        "'statescapitals.StatesandCapitalsGuiForPeopleWhoAreBad'"])
if __name__ == "__main__":
    main()