# install_flask.pp

package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  path    => '/usr/local/bin:/usr/bin:/bin',
  require => Package['python3-pip'],
}
