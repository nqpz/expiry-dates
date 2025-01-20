# To use this, put
#
#   (import /var/www/expiry-dates/server.nix "domain.tld" 8123)
#
# into your imports in another file.
domain: internalPort:
let
  root = "/var/www/expiry-dates";
in
{ config, pkgs, ... }:
{
  services.nginx.virtualHosts."${domain}" = {
    forceSSL = true;
    enableACME = true;
    locations."/" = {
      proxyPass = "http://localhost:${builtins.toString internalPort}";
    };
    locations."/static" = {
      root = "${root}/varer";
    };
    locations."/upload" = {
      root = "${root}";
    };
    locations."/cache" = {
      root = "${root}";
    };
  };

  # See https://github.com/nqpz/nielx/blob/master/nielx/services.nix
  nielx.services.expiry-dates-backup = {
    preStart = null;
    command = "${root}/backup";
    packages = [ pkgs.rclone ];
    user = "${config.nielx.user}";
    group = "users";
    when = "*-*-* 20:00:00";
  };
}
