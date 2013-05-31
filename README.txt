*******************************
 Raspberry Pi - RGBLED running
*******************************


Available color settings
-------------------------

         R  G  B
WHITE    1  1  1
BLACK    0  0  0
RED      1  0  0 
GREEN    0  1  0
BLUE     0  0  1
MAGENTA  1  0  1
CYAN     0  1  1
YELLOW   1  1  0



Run from command line
----------------------
python /home/pi/python_code/rgbled.py 1 1 1 (desired color value) 



Run from a web browser
-----------------------
If accessing from a web browser on the Raspberry Pi desktop 

	http://localhost/rgbled/index.html

If accessing from a web browser on the same network as the Raspberry Pi

	http://<ip address>/rgbled/index.html

Determine the IP address of the Raspberry Pi

	ip addr show eth0