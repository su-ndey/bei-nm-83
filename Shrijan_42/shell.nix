{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python3.withPackages (ps: with ps; [
    numpy
    sympy
  ]);
in

pkgs.mkShell {
  name = "numerical-methods-shell";

  buildInputs = [
    pkgs.git
    pkgs.curl
    pkgs.jq
    pythonEnv
  ];

  shellHook = ''
    echo "Numerical Methods dev shell (Python + numpy + sympy)"
    echo "Lab scripts live in subfolders — run from here, e.g.:"
    echo "  python lab4/ex1.py"
    echo "  python lab3/ex1.py"
  '';
}
