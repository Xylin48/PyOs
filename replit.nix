{ pkgs }: {
  deps = [
    pkgs.python38Packages.getkey
    pkgs.python39Packages.getkey
    pkgs.haskellPackages.simple-sendfile
    pkgs.python39Packages.cloudsplaining
    pkgs.firefox
    pkgs.wget
  ];
}
