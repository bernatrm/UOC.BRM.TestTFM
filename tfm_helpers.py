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

def getPathToCleanedHistoricalReservasHotel(path: str, hotel: str, format: str) -> str:
    """Given a root path, hotel and format builds dest string path to Reservas"""
    return (fr"{path}\historical\reservas\{format}\{hotel}_historico_reservas.{format}")

def getPathToCleanedHistoricalReservasDiariasHotel(path: str, hotel: str, format: str) -> str:
    """Given a root path, hotel and format builds dest string path to Reservas Diarias"""
    return (fr"{path}\historical\reservas_diarias\{format}\{hotel}_historico_reservas_diarias.{format}")

to_integer = lambda i: (int(float(i)))

if __name__ == "__main__":
    print("Helpers for TFM project")
