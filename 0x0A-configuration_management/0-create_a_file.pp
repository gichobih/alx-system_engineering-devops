#creating a file in /tmp sing puppet

file { '/tmp/school':
  mode  ->   '0744',
  content -> 'I love Puppet',
  owner  ->  'www-data',
  group  ->  'www-data',
}
