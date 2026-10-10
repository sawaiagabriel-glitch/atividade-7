import subprocess
import sys


def test_cli_frete_padrao():
    resultado = subprocess.run(
        [sys.executable, "-m", "src.frete", "200"],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0
    assert resultado.stdout.strip() == "15.0"


def test_cli_frete_gratis():
    resultado = subprocess.run(
        [sys.executable, "-m", "src.frete", "250"],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0
    assert resultado.stdout.strip() == "0.0"

