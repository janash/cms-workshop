import numpy
import os
import sys

def calculate_distance(atom1, atom2):
    """Calculate the distance between two atoms in 3D"""
    distance = numpy.sqrt((atom1[0] - atom2[0])**2 + (atom1[1] - atom2[1]) **2
                          + (atom1[2] - atom2[2])**2 )
    return distance

def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    """
    Check if distance is bond.

    Distance is a bond if it is between the minimum and maximum length.

    Parameters
    ----------
    atom_distance: float
        The distance between two atoms
    minimum_length: float
        The minimum length for a bond
    maximum_length: float
        The maximum length for a bond

    Returns
    -------
    bool
        True if bond, False otherwise

    """

    if atom_distance > minimum_length and atom_distance <= maximum_length:
        return True
    else:
        return False

def read_xyz(filename):
    """
    Read an xyz file

    Parameters
    ----------
    filename: str
        The file path to the xyz fiole

    Returns
    -------
    symbols: list
        List of atom symbols

    coords: list
        Atom coordinates
    """

    xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coord = xyz_file[:,1:]
    coord = coord.astype(numpy.float)

    return symbols, coord


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise NameError('Incorrect input - script requires an xyz file name.')

    xyz_file = sys.argv[1]

    symbols, coord = read_xyz(xyz_file)

    for numA, atomA in enumerate(coord):
        for numB, atomB in enumerate(coord):
            if numB > numA:
                bond_length_AB = calculate_distance(atomA, atomB)

                if bond_check(bond_length_AB):
                    print(F'{symbols[numA]} to {symbols[numB]} : {bond_length_AB:.3f}')
