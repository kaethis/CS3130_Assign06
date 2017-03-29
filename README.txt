-----------------------------------------------------------------
          _          _                         _    __   __ 
         /_\   _____(_)__ _ _ _  _ __  ___ _ _| |_ /  \ / / 
        / _ \ (_-<_-< / _` | ' \| '  \/ -_) ' \  _| () / _ \
       /_/ \_\/__/__/_\__, |_||_|_|_|_\___|_||_\__|\__/\___/
                      |___/                                 
-----------------------------------------------------------------

[AUTHOR]  Matt W. Martin, 4374851
          kaethis@tasmantis.net

[VERSION] 1.0

[PROJECT] CS3130, Assign06
          GPRC COURSE SEARCH

          A Python program that connects to the GPRC course
          search webpage and retrieves information related to
          that course.  Uses default contexts and TLSL socket
          wrapper.

[DATE]    28-Mar-2017

[ISSUED]  20-Mar-2017

[USAGE]   'python3 prog.py'

[FILES]   ./README.txt
          ./prog.py

[ISSUES]  - 'REGEX FOR HTML PARSING'
            Not necessarily and issue, but an observation.  I say
            this with all due respect: REGEX is a lousy method
            for parsing content contained within elements in a
            DOM tree.  There's a structure inherit in XML that
            consists of parent and child elements.  The tags 
            clearly define where the elements begin and end
            (they're there for a good reason!).  You can exploit
            this structure to get exactly the elements you're
            looking for.  Here, a text validation solution like
            REGEX feels like using a scalpel to cut down a tree
            (or, very specific trees in a great big forest).

[REPO]    https://github.com/kaethis/CS3130_Assign06
