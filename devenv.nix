{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [ 
    pkgs.git 
    pkgs.poetry
    # dependencies for the bot
    pkgs.python311Packages.discordpy
    pkgs.python311Packages.slixmpp
  ];

  # https://devenv.sh/scripts/
  enterShell = ''
    git --version
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep "2.42.0"
  '';

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/languages/
  languages.python.enable = true;

  # https://devenv.sh/pre-commit-hooks/
  pre-commit.hooks.black.enable = true;

  # https://devenv.sh/processes/
  processes.alfredbot.exec = "python3.11 alfred.py -x";

  # See full reference at https://devenv.sh/reference/options/
}
