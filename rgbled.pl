#!/usr/bin/perl

if (length ($ENV{'QUERY_STRING'}) > 0){
	$buffer = $ENV{'QUERY_STRING'};
      	@pairs = split(/&/, $buffer);
      	foreach $pair (@pairs){
        	($name, $value) = split(/=/, $pair);
           	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
           	$in{$name} = $value; 
      	}
}

$r = $in{'r'};
$g = $in{'g'};
$b = $in{'b'};

system("python /home/pi/python_code/rgbled.py $r $g $b");

