# 2-puppet_custom_http_response_header.pp

# Install Nginx
class { 'nginx': }

# Set the hostname
file { '/etc/hostname':
  ensure  => present,
  content => '03-web-02',
}

exec { 'set_hostname':
  command => '/bin/hostnamectl set-hostname 03-web-02',
  path    => ['/bin', '/usr/bin'],
  unless  => '/bin/hostnamectl | grep "Static hostname: 03-web-02"',
}

# Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "# Nginx default site configuration\n
              server {\n
                listen 80 default_server;\n
                listen [::]:80 default_server;\n
                root /var/www/html;\n
                index index.html index.htm index.nginx-debian.html;\n
                server_name _;\n
                location / {\n
                  try_files \$uri \$uri/ =404;\n
                }\n
                # Custom HTTP response header\n
                add_header X-Served-By \$hostname;\n
                # Additional configurations...\n
              }\n",
  require => Class['nginx'],
}

# Reload Nginx to apply changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}

# Display the custom header using curl
exec { 'check_custom_header':
  command => 'curl -sI localhost | grep X-Served-By',
  path    => ['/bin', '/usr/bin'],
  require => Service['nginx'],
}

