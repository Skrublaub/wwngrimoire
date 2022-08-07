# WWNGrimoire Package

wg is the cli utility created to interact with managing the
website.

This package is multipurpose
- Act as a sdk for obtaining spell information
- Act as a rest api for obtaining spell information
- Act as a graphical webpage for searching spells
    - Will need react.js for the non javascript version

## Documentation

### Docstrings

This project uses [google style](https://google.github.io/styleguide/pyguide.html#doc-function-args) 
docstrings for functions. Note: Using docstrings for typer makes a lot of screen bloat, so I will
not make them for those functions.

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

## Adding a spell

Run `wg generate-json`

This will look in the `src/wwngrimoire/wwngrimoire/spells` directory 
and generate a single json file based off of a specifically
formatted text file name and structure.

The text file must be named as so:  
`spell_name_here_#.txt`

`spell_name_here` would be the spell name with the words of the spell split by
an underscore. `#` is the level of the spell.

For example:
`The_Howl_of_Light_3.txt`

Python knows the spell is named `The Howl of Light` and that the spell's level is `3`.

Inside the text file, copy and paste the spell's description. Might be worth it
to pretty up the description slightly so there's not too much weird formatting.