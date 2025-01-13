# Use this file with nix-shell or similar tools; see https://nixos.org/
with import <nixpkgs> {};

mkShell {
  buildInputs = [
    python3
  ];

  # First run:
  #
  #   python -m venv .venv
  #   . .venv/bin/activate
  #   pip install Pillow Django sorl-thumbnail
  shellHook = ''
    . .venv/bin/activate
    # Remember to export PRODUCTION_DOMAIN
  '';
}
