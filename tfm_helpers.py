import os

def getListOfFiles(path: str) -> list:
    """Get the list of all files in directory tree at given path"""
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    return listOfFiles

def getSourcePathToHistoricalReservasHotel(path: str, hotel: str) -> str:
    """Given a root path and hotel, builds source stirng path to Historico Reservas"""
    return (fr"{path}\Historicos\Reservas\{hotel}")

def getSourcePathToHistoricalReservasDiariasHotel(path: str, hotel: str) -> str:
    """Given a root path and hotel, builds source stirng path to Historico Reservas Diarias"""
    return (fr"{path}\Historicos\ReservasDiarias\{hotel}")

def getPathToProcessedHistoricalReservasHotel(hotel: str, format: str) -> str:
    """Given a hotel and format builds dest string path to Reservas"""
    return (fr"data\processed\historical\reservas\{format}\{hotel}_historico_reservas.{format}")

def getPathToProcessedHistoricalReservasDiariasHotel(hotel: str, format: str) -> str:
    """Given a hotel and format builds dest string path to Reservas Diarias"""
    return (fr"data\processed\historical\reservas_diarias\{format}\{hotel}_historico_reservas_diarias.{format}")


def getPathToCleanedHistoricalReservasHotel(format: str) -> str:
    """Given a root path, hotel and format builds dest string path to Reservas"""
    return (fr"data\cleaned\historical\reservas\{format}\historico_reservas.{format}")

def getPathToCleanedHistoricalReservasDiariasHotel(format: str) -> str:
    """Given a root path, hotel and format builds dest string path to Reservas Diarias"""
    return (fr"data\cleaned\historical\reservas_diarias\{format}\historico_reservas_diarias.{format}")

to_integer = lambda i: (int(float(i)))
hoteles = ["02", "04", "05", "15", "16", "21", "22"]

if __name__ == "__main__":
    print("Helpers for TFM project")
