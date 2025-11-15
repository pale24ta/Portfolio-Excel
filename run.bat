@echo off

REM Obtener la carpeta del script
set SCRIPT_FOLDER=%~dp0
pushd %SCRIPT_FOLDER%

REM Ruta al entorno virtual
set WINPYTHON_ACTIVATE=env\\Scripts\\activate.bat

REM Ruta al intérprete de Python
set PYTHON_EXE=env\\Scripts\\python.exe

REM Ruta al script Python
set PYTHON_PROGRAM=.\src\main.py

REM Activar el entorno virtual
call %WINPYTHON_ACTIVATE%

REM Verificar si la activación fue exitosa
if errorlevel 1 (
    echo Error al activar el entorno virtual.
    exit /b 1
)

REM Ejecutar el script Python
call %PYTHON_EXE% %PYTHON_PROGRAM%

REM Desactivar el entorno virtual
deactivate

pause   