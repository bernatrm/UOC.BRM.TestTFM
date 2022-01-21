import os
from datetime import datetime
from queue import Empty

to_integer = lambda i: (int(float(i)))
hoteles = ["02", "04", "05", "15", "16", "21", "22"]

def getListOfFiles(path: str) -> list:
    """Get the list of all files in directory tree at given path"""
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    return listOfFiles

def createDirIfNoExists(path: str):
    if not os.path.exists(path):
        os.mkdir(path)

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
    """Given a format builds dest string path to Cleaned Reservas Diarias File"""
    return (fr"data\cleaned\historical\reservas_diarias\{format}\historico_reservas_diarias.{format}")

def getPathToProcessedSnapshotReservas(format: str, snapshot_date: datetime) -> str:
    """Given a format and snapshot date builds dest string path to Reservas Diarias Snapshot File"""  
    year = f"{snapshot_date.year}"
    month = f"{snapshot_date.strftime('%m')}"
    day = f"{snapshot_date.strftime('%d')}"

    createDirIfNoExists(fr"data\processed\snapshots\reservas\{format}\{year}")
    createDirIfNoExists(fr"data\processed\snapshots\reservas\{format}\{year}\{month}")
    
    return (fr"data\processed\snapshots\reservas\{format}\{year}\{month}\{year}{month}{day}_reservas.{format}")

def getPathToProcessedSnapshotReservasFolder(format: str, year: str) -> str:
    """Given a format builds dest string path to Reservas Diarias Snapshot main folder"""  
    
    if year =="":
        return (fr"data\processed\snapshots\reservas\{format}")
    else:
        return (fr"data\processed\snapshots\reservas\{format}\{year}")

def getPathToProcessedSnapshotOcupacion(format: str, year: str) -> str:
    """Given a format builds dest string path to Ocupacion Snapshot file"""
    
    if year =="":
        return (fr"data\processed\snapshots\ocupacion\{format}\ocupacion.{format}")
    else:
        return (fr"data\processed\snapshots\ocupacion\{format}\{year}_ocupacion.{format}")


if __name__ == "__main__":
    print("Helpers for TFM project")
