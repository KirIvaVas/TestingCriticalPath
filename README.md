**Project description:**

The idea of the script was to get aquainted with new libraries and make an 
automated test. This included the next steps:

1) to use a User-like attitude (Critical-Path) to test a possibility finding a  
   way for a particular product in the given URL. 
   The product is the first one on all pages that corresponds to the given name.
   Then check the presence of information about the product in different 
   widgets, including name, label, discount, price, description. See main.py
   
2) Catch possible exceptions relating to selenium driver and make a log file 
   gathering them. See exceptions.py

3) Automatically test text samples for an appropriate information content, 
   including: length, brand name, label pattern, discount and price structure. 
   See testingParameters.py. Results are gathered to a log file.

Libraries partially used in project:

- math
- functools
- selenium
- logging
- re
