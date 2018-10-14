# DHKeyExchange
## An exercise in implementing the Diffie-Hellman Key Exchange Protocol.

There is a lot of code I have left commented out because it can be uncommented to help in making sure both machines are calculating their values the same.

Both the prime for modulus (p) and the random secret exponent (a) should be at least 500 bits long (although 504 bits brings it to a nice even 63 bytes),

In a bash shell, you can use openssl to generate p like so:
    
`openssl prime -generate -bits 504 -safe`

On linux, the following command can be used to generate random numbers:

`od -vAn -N66 -tu8 < /dev/urandom`

_Note: urandom is a somewhat funky utility to deal with. If you want to change up how you extract data from it, be sure you read up on how to do it. Do not just use cat to try and get some data out._

The generator I used was 5, but I left it open to changing.

A truncating length of 1 will remove 1 number off the end of the shared key (ex. 123 become 12). Input 0 for no truncation.

The python script can be run like so (Anaconda Python 3.7.0 on Ubuntu 18.04.1 LTS):

`python DH.py`

_Note: 'python' references the version of python specified above, so you will need to use whatever keyword invokes the version of python on your machine closest to it._