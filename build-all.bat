@echo off
setlocal EnableDelayedExpansion

set "ROOT=%~dp0"

echo Building all HungerControlMod versions...

for /d %%D in ("%ROOT%versions\*") do (
    echo ========================================
    echo Building %%~nxD
    echo ========================================
    cd /d "%%D"
    set "JAVA_VER=21"
    echo %%~nxD | findstr /C:"1.20.2" >/dev/null && set "JAVA_VER=17"
    echo %%~nxD | findstr /C:"1.20.3" >/dev/null && set "JAVA_VER=17"
    echo %%~nxD | findstr /C:"1.20.4" >/dev/null && set "JAVA_VER=17"
    
    if "!JAVA_VER!"=="17" (
        set "JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-17.0.17.10-hotspot"
    ) else (
        set "JAVA_HOME=C:\Program Files\Android\openjdk\jdk-21.0.8"
    )
    set "PATH=!JAVA_HOME!\bin;%PATH%"
    
    call gradlew.bat build --no-daemon
    if errorlevel 1 (
        echo BUILD FAILED for %%~nxD
        exit /b 1
    )
)

echo.
echo All versions built successfully!
pause
