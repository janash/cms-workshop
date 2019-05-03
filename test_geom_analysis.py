import geom_analysis as ga

def test_calculate_distance():
    coord1 = [0, 0, 0]
    coord2 = [1, 0, 0]
    expected = 1.0
    observed = ga.calculate_distance(coord1,coord2)
    assert observed == expected

def test_bond_check_true():
    bond_distance = 1.2
    expected = True
    observed = ga.bond_check(bond_distance)
    assert observed == expected

def test_bond_check_false():
    bond_distance = 1.6
    expected = False
    observed = ga.bond_check(bond_distance)
    assert observed == expected

def test_bond_check_0():
    bond_distance = 0
    expected = False
    observed = ga.bond_check(bond_distance)
    assert observed == expected
