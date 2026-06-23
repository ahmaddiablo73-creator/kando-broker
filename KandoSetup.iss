[Setup]
AppName=Kando Core
AppVersion=1.0
DefaultDirName={autopf}\KandoCore
DefaultGroupName=Kando Core
OutputBaseFilename=KandoCore_Setup
OutputDir=D:\KANDO-CORE
Compression=lzma
SolidCompression=yes

[Files]
Source: "D:\KANDO-CORE\app.exe.to.exe"; DestDir: "{app}"; DestName: "KandoCore.exe"; Flags: ignoreversion
Source: "D:\KANDO-CORE\database.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\KANDO-CORE\browser_config.json"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\Kando Core"; Filename: "{app}\KandoCore.exe"