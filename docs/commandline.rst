Command-line Reference
======================

Overview
--------

The ``m209`` command-line utility peforms three functions:

* Creates key list files
* Encrypts text, either given on the command line or read from a file
* Decrypts text, either given on the command line or read from a file
 
These functions are implemented as sub-commands. To see the list of
sub-commands and options common to all sub-commands, use the ``-h`` or
``--help`` option::

   $ m209 --help
   usage: m209 [-h] [-l {debug,info,warning,error,critical}]
               {encrypt,enc,decrypt,dec,keygen,key} ...

   M-209 simulator and utility program

   optional arguments:
     -h, --help            show this help message and exit
     -l {debug,info,warning,error,critical}, --log {debug,info,warning,error,critical}
                           set log level [default: warning]

   list of commands:
     type m209 {command} -h for help on {command}

     {encrypt,enc,decrypt,dec,keygen,key}
       encrypt (enc)       encrypt text from file or command-line
       decrypt (dec)       decrypt text from file or command-line
       keygen (key)        generate key list

The ``-l`` / ``--log`` options control the verbosity of output. Currently only
the ``keygen`` sub-command makes use of this option.

Each sub-command has an alias for those who prefer shorter commands.

Keygen Sub-command
------------------

``keygen``, or ``key`` for short, is the sub-command that pseudo-randomly
creates key list files for use by the ``encrypt`` and ``decrypt`` sub-commands,
as well as by the ``m209`` library routines. 

Help on the ``keygen`` sub-command can be obtained with the following
invocation::

   $ m209 keygen --help
   usage: m209 keygen [-h] [-z KEY_FILE] [-o] [-s XX] [-n NUMBER]

   Generate key list file

   optional arguments:
     -h, --help            show this help message and exit
     -z KEY_FILE, --key-file KEY_FILE
                           path to key list file [default: m209keys.cfg]
     -o, --overwrite       overwrite key list file if it exists
     -s XX, --start XX     starting indicator; if omitted, random indicators are
                           used
     -n NUMBER, --number NUMBER
                           number of key lists to generate [default: 1]

The options for ``keygen`` are described below.

The ``-z`` or ``--key-file`` option names the key list file. If not supplied,
this defaults to ``m209keys.cfg``. Note that the other sub-commands also have
this option, and they too use the same default value.

The ``-o`` or ``--overwrite`` switch must be present if the key list file
already exists. It provides confirmation that the user wants to overwrite an
existing file. If the key list file already exists, and this option is not
supplied, this sub-command will exit with an error message and the original key
list file will be unchanged.

The ``-s`` or ``--start`` option sets the starting indicator for the key list
file. Key list indicators are two letters in the range ``AA`` to ``ZZ``. For
example, ``keygen`` can be told to create 3 key lists, starting with indicator
``AA``.  In this case the key lists ``AA``, ``AB``, and ``AC`` would be written
to the file. If this parameter is omitted, ``keygen`` picks indicators at
random. Key list indicators simply name the key list, and are placed in the
leading and trailing groups of encrypted messages to tell the receiver which
key list was used to create the message. Both sender and receiver must have the
same key list (name and contents) to communicate.

The ``-n`` or ``--number`` option specifies the number of key lists to
generate. The default value is 1.

.. NOTE:: 

   The algorithm the ``keygen`` sub-command uses to generate key lists is based
   on the actual US Army procedure taken from the 1944 manual. This procedure
   is somewhat loosely specified and a lot is left up to the soldier creating
   the key list. The ``keygen`` algorithm is ad-hoc and uses simple heuristics
   and random numbers to make decisions.  Occasionally this algorithm may fail
   to generate a key list that meets the final criteria defined in the manual.
   If this happens an error message will be displayed and no key list file will
   be created. It is suggested to simply run the command again as it is not
   likely to happen twice in a row.
