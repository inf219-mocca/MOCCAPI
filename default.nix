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
    pip install -U pip
    pip install pipenv
    pipenv sync --dev
  '';
}
