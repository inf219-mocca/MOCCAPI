with import <nixpkgs> {};
with pkgs.python36Packages;

stdenv.mkDerivation {
  name = "moccapi";
  buildInputs = [
    python36
    python36Packages.virtualenv
  ];
  shellHook = ''
    virtualenv --no-setuptools .venv
    export PATH=$PWD/.venv/bin:$PATH
    export PIPENV_VENV_IN_PROJECT=1
    pip install --upgrade pip
    pip install --upgrade pipenv
    pipenv sync --dev
  '';
}
