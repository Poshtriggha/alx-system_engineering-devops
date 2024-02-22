# Enhance user 'holberton' permissions for seamless login and file operations.

# Adjust the hard file limit to 50,000 for the 'holberton' user in the system's security limits configuration.
exec { 'increase-hard-file-limit-for-holberton':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# Modify the soft file limit to 50,000 for the 'holberton' user in the system's security limits configuration.
exec { 'increase-soft-file-limit-for-holberton':
  command => 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

