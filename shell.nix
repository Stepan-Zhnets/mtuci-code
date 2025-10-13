{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = with pkgs; [
    (python312.withPackages(pypkgs: with pypkgs; [
      # Python библиотеки
    ]))
    # Другие инструменты Python

    # Пакетный менеджер Python
    uv
  ];
}