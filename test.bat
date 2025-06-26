@echo off
echo ==========================================
echo         CALCULADORA - TESTES
echo ==========================================
echo.

if "%1"=="lib" goto test_lib
if "%1"=="calc" goto test_calc
if "%1"=="integration" goto test_integration
if "%1"=="all" goto test_all
if "%1"=="" goto test_all

echo Uso: test.bat [lib|calc|integration|all]
echo.
echo   lib         - Executa apenas testes da biblioteca math_lib
echo   calc        - Executa apenas testes da calculadora
echo   integration - Executa apenas testes de integracao
echo   all         - Executa todos os testes (padrao)
echo.
goto end

:test_lib
echo Executando testes da biblioteca math_lib...
cd math_lib
python run_tests.py
cd ..
goto end

:test_calc
echo Executando testes da calculadora...
python -m pytest test_calculadora.py -v
goto end

:test_integration
echo Executando testes de integracao...
python run_all_tests.py
goto end

:test_all
echo Executando todos os testes...
python run_all_tests.py
goto end

:end
pause
