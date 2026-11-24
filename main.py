
# Skills test- 2nd Quarter
from js import document, window
from pyscript import display

non_metals = {
    # place all non-metal elements
       'H': ("Hydrogen", 1, 1.008),
       'O': ("Oxygen", 8, 15.999),
       'Br': ("Bromine", 35, 79.904),
       'H': ("Hydrogen", 1, 1.008),
       'Xe': ("Xenon", 54, 131.293),
       'P': ("Phosphorus", 15, 30.974),
       'He': ("Helium", 2, 4.003),
       'Rn': ("Radon", 86, 222),
       'C': ("Carbon", 6, 12.011),
       'At': ("Astatine", 85, 210),
       'Ne': ("Neon", 10, 20.180),
       'S': ("Sulfur", 16, 32.06),
       'Og': ("Oganesson", 118, 294),
       'F': ("Fluorine", 9, 18.998),
       'Kr': ("Krypton", 36, 83.798),
       'N': ("Nitrogen", 7, 14.007),
       'Ts': ("Tennessine", 117, 294),
       'Ar': ("Argon", 18, 39.948),
       'I': ("Iodine", 53, 126.904),
       'Cl': ("Chlorine", 17, 35.45),
       'Se': ("Selenium", 34, 78.971)
}


def search_element(e):
    document.getElementById("result").innerHTML = ""
    element1 = document.getElementById("blank").value.strip().title()

    # Using .get() - no if statement
    name, atomic_number, atomic_mass = non_metals.get(
        element1, ("Element not found", "-", "-")
    )

    document.getElementById("result").innerHTML = f"""
        <b>Symbols:</b> {element1} <br>
        <b>Element:</b> {name}<br>
        <b>Atomic:</b> {atomic_number}<br>
        <b>Atomic mass:</b> {atomic_mass}
    """


def go_to_homepage(e):
    window.location.href = "index.html"
