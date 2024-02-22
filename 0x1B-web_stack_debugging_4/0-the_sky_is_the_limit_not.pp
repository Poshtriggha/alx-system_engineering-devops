# Adjusts server capacity by enhancing Nginx's ability to handle traffic.

# Update ULIMIT in the default Nginx configuration file to accommodate increased server traffic.
exec { 'update-nginx-ulimit':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx to apply the updated ULIMIT and ensure optimal server performance.
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}

