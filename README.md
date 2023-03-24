This is a script that runs over a bibtex file and renames each entry to the convention [firstauthorsurname][year][firstwordoftitle], it also abbreviates the journal to the corresponding ISO 4 abbreviation. These abbreviations are contained in a dictionary inside the script.

To run from the command line: `python parse_bib.py in.bib out.bib`

The code was written by gpt4 are tweaked afterwards for edge cases. 

Would be nice to turn into a plugin for browser.