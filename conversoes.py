def mgL_to_mcgL(value):
    return value * 1000


def mcgL_to_mgL(value):
    return value / 1000


def mgL_to_ngL(value):
    return value * 1000000


def ngL_to_mgL(value):
    return value / 1000000


def mcgL_to_ngL(value):
    return value * 1000


def ngL_to_mcgL(value):
    return value / 1000


def gL_to_mgL(value):
    return value * 1000


def mgL_to_gL(value):
    return value / 1000


def gL_to_mcgL(value):
    return value * 1000000


def mcgL_to_gL(value):
    return value / 1000000


def gL_to_ngL(value):
    return value * 1000000000


def ngL_to_gL(value):
    return value / 1000000000


def gL_to_molL(value, mass_per_mol):
    return value / mass_per_mol


def molL_to_gL(value, mass_per_mol):
    return value * mass_per_mol


def mcgmL_to_mgL(value):
    return value


def mgL_to_mcgmL(value):
    return value


def mgKg_to_mgL(value, density):
    return value * density


def mgL_to_mgKg(value, density):
    return value / density


def mgmL_to_mgL(value):
    return value * 1000


def mgL_to_mgmL(value):
    return value / 1000


def mgL_to_molL(value, mass_per_mol):
    return value / (mass_per_mol * 1000)


def mcgL_to_molL(value, mass_per_mol):
    return value / (mass_per_mol * 1000000)


def mgL_to_mcgKg(value, density):
    return (1000 * value) / density


def mcgL_to_mcgmL(value):
    return value / 1000


def mcgL_to_mgKg(value, density):
    return value / (density * 1000)


def mcgL_to_mgmL(value):
    return value / 1000000


def mcgL_to_mcgKg(value, density):
    return value / density


def ngL_to_mcgKg(value, density):
    return value / (1000 * density)


def ngL_to_mcgmL(value):
    return value / 1000000


def ngL_to_mgmL(value):
    return value / 1000000000


def ngL_to_mgKg(value, density):
    return value / (1000000 * density)


def ngL_to_molL(value, mass_per_mol):
    return value / (mass_per_mol * 1000000000)


def gL_to_mcgmL(value):
    return value * 1000


def gL_to_mgKg(value, density):
    return (1000 * value) / density


def gL_to_mgmL(value):
    return value


def gL_to_mcgKg(value, density):
    return (1000000 * value) / density


def molL_to_mgL(value, mass_per_mol):
    return value * mass_per_mol * 1000


def molL_to_mcgL(value, mass_per_mol):
    return value * mass_per_mol * 1000000


def molL_to_ngL(value, mass_per_mol):
    return value * mass_per_mol * 1000000000


def molL_to_mcgmL(value, mass_per_mol):
    return value * mass_per_mol * 1000


def molL_to_mgKg(value, density, mass_per_mol):
    return (value * mass_per_mol * 1000) / density


def molL_to_mgmL(value, mass_per_mol):
    return value * mass_per_mol


def molL_to_mcgKg(value, density, mass_per_mol):
    return (value * mass_per_mol * 1000000) / density


def mcgmL_to_mcgL(value):
    return value * 1000


def mcgmL_to_ngL(value):
    return value * 1000000


def mcgmL_to_gL(value):
    return value / 1000


def mcgmL_to_molL(value, mass_per_mol):
    return value / (1000 * mass_per_mol)


def mcgmL_to_mgKg(value, density):
    return value / density


def mcgmL_to_mgmL(value):
    return value / 1000


def mcgmL_to_mcgKg(value, density):
    return (value * 1000) / density


def mgKg_to_mcgL(value, density):
    return value * 1000 * density


def mgKg_to_ngL(value, density):
    return value * 1000000 * density


def mgKg_to_gL(value, density):
    return (value * density) / 1000


def mgKg_to_molL(value, density, mass_per_mol):
    return (value * density) / (1000 * mass_per_mol)


def mgKg_to_mcgmL(value, density):
    return value * density


def mgKg_to_mgmL(value, density):
    return (value * density) / 1000


def mgKg_to_mcgKg(value):
    return value * 1000


def mgmL_to_mcgL(value):
    return value * 1000000


def mgmL_to_ngL(value):
    return value * 1000000000


def mgmL_to_gL(value):
    return value


def mgmL_to_molL(value, mass_per_mol):
    return value / mass_per_mol


def mgmL_to_mcgmL(value):
    return value * 1000


def mgmL_to_mgKg(value, density):
    return (value * 1000) / density


def mgmL_to_mcgKg(value, density):
    return (value * 1000000) / density


def mcgKg_to_mgL(value, density):
    return (value * density) / 1000


def mcgKg_to_mcgL(value, density):
    return value * density


def mcgKg_to_ngL(value, density):
    return value * density * 1000


def mcgKg_to_gL(value, density):
    return (value * density) / 1000000


def mcgKg_to_molL(value, density, mass_per_mol):
    return (value * density) / (1000000 * mass_per_mol)


def mcgKg_to_mcgmL(value, density):
    return value * density / 1000


def mcgKg_to_mgKg(value):
    return value / 1000


def mcgKg_to_mgmL(value, density):
    return value * density / 1000000
