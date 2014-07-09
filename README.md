AutoIPBlacklist
===============

Generate ip blacklist conf in apache2 format by analysizing the database table of wordpress plugin my-visitors and akismet

Usage:

You should create a my.cnf file like this:

	[client]
	user=your_username
	password=your_password
	database=your_wordpress_database
	host=your_host_url
	port=3306_or_other
