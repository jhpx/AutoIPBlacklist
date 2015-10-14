AutoIPBlacklist
===============

Generate ip blacklist conf in apache2 format by analysizing the database table of wordpress plugin my-visitors and akismet

Usage:
	./autofix_visitors_records

You should create a my.cnf file like this:

	[client]
	user=your_mysql_username
	password=your_mysql_password
	database=your_wordpress_database
	host=your_host_url
	port=3306_or_other
	[ssh]
	user=your_username
	host=your_host_url
	port=22_or_other
	privatekey=~/.ssh/id_rsa_or_other


And you must install openssh to run the command "sftp" and "ssh".

Also your public key must be put in the content of /root/.ssh/authorized_keys in your VPS.
