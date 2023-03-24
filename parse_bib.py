import re
import sys
from typing import Dict

# move to json file
abbreviations_db =  {
        "Acta Phys. Pol. A": "Acta Physica Polonica A",
        "Acta Phys. Pol. B": "Acta Physica Polonica B",
        "Adv. High Energy Phys.": "Advances in High Energy Physics",
        "Adv. Phys.": "Advances in Physics",
        "Annu. Rev. Astron. Astrophys.": "Annual Review of Astronomy and Astrophysics",
        "Annu. Rev. Condens. Matter Phys.": "Annual Review of Condensed Matter Physics",
        "Annu. Rev. Nucl. Part. Sci.": "Annual Review of Nuclear and Particle Science",
        "Appl. Phys. A": "Applied Physics A",
        "Appl. Phys. B": "Applied Physics B",
        "Appl. Phys. Express": "Applied Physics Express",
        "Astrophys. J.": "Astrophysical Journal",
        "Astrophys. J. Lett.": "Astrophysical Journal Letters",
        "Astrophys. J. Suppl. Ser.": "Astrophysical Journal Supplement Series",
        "At. Data Nucl. Data Tables": "Atomic Data and Nuclear Data Tables",
        "Biochim. Biophys. Acta Biomembr.": "Biochimica et Biophysica Acta - Biomembranes",
        "Braz. J. Phys.": "Brazilian Journal of Physics",
        "Can. J. Phys.": "Canadian Journal of Physics",
        "Chaos": "Chaos",
        "Chem. Phys.": "Chemical Physics",
        "Chem. Phys. Lett.": "Chemical Physics Letters",
        "Classical Quantum Gravity": "Classical and Quantum Gravity",
        "Comput. Phys. Commun.": "Computer Physics Communications",
        "Econ. Phys.": "Economic Physics",
        "EPL": "Europhysics Letters",
        "Eur. Phys. J. A": "European Physical Journal A",
        "Eur. Phys. J. B": "European Physical Journal B",
        "Eur. Phys. J. C": "European Physical Journal C",
        "Eur. Phys. J. D": "European Physical Journal D",
        "Eur. Phys. J. E": "European Physical Journal E",
        "Eur. Phys. J. H": "European Physical Journal H",
        "Found. Phys.": "Foundations of Physics",
        "Front. Phys.": "Frontiers of Physics",
        "Gen. Relativ. Gravit.": "General Relativity and Gravitation",
        "IEEE Trans. Plasma Sci.": "IEEE Transactions on Plasma Science",
        "Int. J. Mod. Phys. A": "International Journal of Modern Physics A",
        "Int. J. Mod. Phys. B": "International Journal of Modern Physics B",
        "Int. J. Mod. Phys. C": "International Journal of Modern Physics C",
        "Int. J. Mod. Phys. D": "International Journal of Modern Physics D",
        "Int. J. Mod. Phys. E": "International Journal of Modern Physics E",
        "Int. J. Theor. Phys.": "International Journal of Theoretical Physics",
        "J. Appl. Phys.": "Journal of Applied Physics",
        "J. Biol. Phys.": "Journal of Biological Physics",
        "J. Chem. Phys.": "Journal of Chemical Physics",
        "J. Cosmol. Astropart. Phys.": "Journal of Cosmology and Astroparticle Physics",
        "J. Fluid Mech.": "Journal of Fluid Mechanics",
        "J. Geophys. Res.": "Journal of Geophysical Research",
        "J. High Energy Phys.": "Journal of High Energy Physics",
        "J. Low Temp. Phys.": "Journal of Low Temperature Physics",
        "J. Magn. Magn. Mater.": "Journal of Magnetism and Magnetic Materials",
        "J. Math. Phys.": "Journal of Mathematical Physics",
        "J. Mod. Opt.": "Journal of Modern Optics",
        "J. Nonlinear Sci.": "Journal of Nonlinear Science",
        "J. Opt.": "Journal of Optics",
        "J. Phys.": "Journal of Physics",
        "J. Phys. A": "Journal of Physics A: Mathematical and Theoretical",
        "J. Phys. B": "Journal of Physics B: Atomic, Molecular and Optical Physics",
        "J. Phys. Chem.": "Journal of Physical Chemistry",
        "J. Phys. D": "Journal of Physics D: Applied Physics",
        "J. Phys. J": "Journal of Physics G: Nuclear and Particle Physics",
        "J. Plasma Phys.": "Journal of Plasma Physics",
        "J. Stat. Mech.": "Journal of Statistical Mechanics: Theory and Experiment",
        "J. Stat. Phys.": "Journal of Statistical Physics",
        "Laser Phys. Lett.": "Laser Physics Letters",
        "Math. Proc. Camb. Philos. Soc.": "Mathematical Proceedings of the Cambridge Philosophical Society",
        "Math. Phys. Anal. Geom.": "Mathematical Physics, Analysis and Geometry",
        "Mod. Phys. Lett. A": "Modern Physics Letters A",
        "Mod. Phys. Lett. B": "Modern Physics Letters B",
        "Nat. Phys.": "Nature Physics",
        "Nucl. Data Sheets": "Nuclear Data Sheets",
        "Nucl. Fusion": "Nuclear Fusion",
        "Nucl. Instrum. Methods Phys. Res. A": "Nuclear Instruments and Methods in Physics Research Section A",
        "Nucl. Instrum. Methods Phys. Res. B": "Nuclear Instruments and Methods in Physics Research Section B",
        "Nucl. Instrum. Methods Phys. Res. C": "Nuclear Instruments and Methods in Physics Research Section C",
        "Nucl. Instrum. Methods Phys. Res. D": "Nuclear Instruments and Methods in Physics Research Section D",
        "Nucl. Instrum. Methods Phys. Res. E": "Nuclear Instruments and Methods in Physics Research Section E",
        "Nucl. Instrum. Methods Phys. Res. F": "Nuclear Instruments and Methods in Physics Research Section F",
        "Phys. Chem. Chem. Phys.": "Physical Chemistry Chemical Physics",
        "Phys. Educ.": "Physics Education",
        "Phys. Lett.": "Physics Letters",
        "Phys. Rev. Lett.": "Physical Review Letters",
        "Phys. Rev. A": ("Physical Review A - Atomic, Molecular, and Optical Physics",
                         "Physical Review A"),
        "Phys. Rev. B": "Physical Review B",
        "Phys. Rev. C": "Physical Review C",
        "Phys. Rev. D": "Physical Review D",
        "Phys. Rev. E": "Physical Review E",
        "Phys. Rev. X": "Physical Review X",
        "Rev. Mod. Phys.": "Reviews of Modern Physics",
        "Phys. Rev. Accel. Beams": "Physical Review Accelerators and Beams",
        "Phys. Rev. Applied": "Physical Review Applied",
        "Phys. Rev. Fluids": "Physical Review Fluids",
        "Phys. Rev. Materials": "Physical Review Materials",
        "Phys. Rev. Phys. Educ. Res.": "Physical Review Physics Education Research",
        "Phys. Med. Biol.": "Physics in Medicine and Biology",
        "Phys. Part. Nucl.": "Physics of Particles and Nuclei",
        "Phys. Rep.": "Physics Reports",
        "Phys. Rev. Accel. Beams": "Physical Review Accelerators and Beams",
        "Phys. Rev. Applied": "Physical Review Applied",
        "Phys. Rev. Fluids": "Physical Review Fluids",
        "Phys. Rev. Materials": "Physical Review Materials",
        "Phys. Rev. Phys. Educ. Res.": "Physical Review Physics Education Research",
        "Phys. Scr.": "Physica Scripta",
        "Phys. Status Solidi A": "Physica Status Solidi A",
        "Phys. Status Solidi B": "Physica Status Solidi B",
        "Phys. Today": "Physics Today",
        "Phys. World": "Physics World",
        "Physica A": "Physica A: Statistical Mechanics and its Applications",
        "Physica B": "Physica B: Condensed Matter",
        "Physica C": "Physica C: Superconductivity and its Applications",
        "Physica D": "Physica D: Nonlinear Phenomena",
        "Physica E": "Physica E: Low-dimensional Systems and Nanostructures",
        "Physics Essays": "Physics Essays",
        "Pramana": "Pramana - Journal of Physics",
        "Prog. Energy Combust. Sci.": "Progress in Energy and Combustion Science",
        "Prog. Part. Nucl. Phys.": "Progress in Particle and Nuclear Physics",
        "Prog. Theor. Phys.": "Progress of Theoretical Physics",
        "Rep. Prog. Phys.": "Reports on Progress in Physics",
        "Rev. Sci. Instrum.": "Review of Scientific Instruments",
        "Science": "Science",
        "Solid State Commun.": "Solid State Communications",
        "Supercond. Sci. Technol.": "Superconductor Science and Technology",
        "Z. Phys.": "Zeitschrift fur Physik"
    }

def abbreviate_journal(journal: str, journal_abbreviations: Dict[str, str]) -> str:
    for key, value in journal_abbreviations.items():
        if isinstance(value, tuple):
            for element in value:
                if journal.strip().lower() == element.strip().lower():
                    return key
        elif journal.strip().lower() == value.strip().lower():
            return key
    # add prompt to register new abbreviation when none is found for a given journal
    return journal

def modify_bibtex_entry(entry: str, journal_abbreviations: Dict[str, str]) -> str:
    author_pattern = re.compile(r'author\s*=\s*{([^}}]+)}', re.IGNORECASE)
    year_pattern = re.compile(r'year\s*=\s*{(\d+)}', re.IGNORECASE)
    title_pattern = re.compile(r'title\s*=\s*{([^}}]+)}', re.IGNORECASE)
    journal_pattern = re.compile(r'journal\s*=\s*{([^}}]+)}', re.IGNORECASE)
    
    
    authorfullname = author_pattern.search(entry).group(1).split(' and ')[0]
    if ',' in authorfullname:
        author = authorfullname.split(',')[0].strip().replace('-', '').lower()
    else:
        author = authorfullname.split()[-1].strip().replace('-', '').lower()
    year = year_pattern.search(entry).group(1).strip()
    title = title_pattern.search(entry).group(1).split()[0].strip(' :').replace('-', '').lower()

    new_id = f"{author}{year}{title}"
    entry = re.sub(r'@(\w+){[^,]*,', rf'@\1{{{new_id},', entry)
    
    try:
        journal = journal_pattern.search(entry).group(1).strip()
        abbreviated_journal = abbreviate_journal(journal, journal_abbreviations)
        entry = journal_pattern.sub(f"journal = {{{abbreviated_journal}}}", entry)
    except AttributeError:
        print(f" - Entry {new_id} is missing the 'journal' attribute.", end='\n')
        pass

    return entry

def process_bibtex_file(input_filename: str, output_filename: str, journal_abbreviations: Dict[str, str]) -> None:
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        buffer = ''
        for line in infile:
            buffer += line
            if line.strip() == "}":
                try:
                    modified_entry = modify_bibtex_entry(buffer, journal_abbreviations)
                    outfile.write(modified_entry)
                except AttributeError:
                    print(f' - Entry might be ill-defined: \n {buffer}', end='\n')
                    outfile.write(buffer)
                buffer = ''

if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    process_bibtex_file(input_filename, output_filename, abbreviations_db)