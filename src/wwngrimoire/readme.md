# WWNGrimoire Package

This package is multipurpose
- Act as a sdk for obtaining spell information
- Act as a rest api for obtaining spell information
- Act as a graphical webpage for searching spells
    - Will need react.js for the non javascript version

## File structure

- pages
  - Holds the flask backend for the gui website
- spells
  - Name and description of all spells in the game
  - The name of the spell is the text file name
    - Spaces are replaced with underscores
- templates
  - Flask's default place to look for html
  - Will not use most likely? TODO?
- utils
  - General utils for the project