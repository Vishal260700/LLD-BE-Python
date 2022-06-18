"""
Factory Pattern - We have a specific Factory which is responsible for providing us with the desired object as per the input.
Abstract Factory Pattern - We have a Factory (abstract) on top of Factory (prev) which allows for decoupling the Factories and addition of new Factory in the code is easier
"""

"""
Problem Statement - Design a Data Ingestion System where we have Sources (API, File, DataLake) and Storage (Cloud, OnPremise)
"""

"""
Use Case Flow -
1. System is requested to injest data from a certain source which can be an API, File, etc
2. The data is ingested into a certain source based on the request
"""

"""
Main Entities
1. CloudStorage implements IngestionService
    1. CloudAPISource implements IngestToDB
    2. CloudFileSource implements IngestToDB
    3. CloudDataLakeSource implements IngestToDB
2. OnPremiseStorage implements IngestionService
    1. APISource implements IngestToDB
    2. FileSource implements IngestToDB
    3. DataLakeSource implements IngestToDB
3. StorageFactory - responsible for providing desired Storage as per request
4. IngestionService - Interface (IngestDataToDB)
5. IngestToDB - Interface (IngestData)
"""

"""
Classes - 
1. IngestionService
    methods -
    IngestDataToDB -> getSourceObject and call IngestData of the source Object
    getSourceObject -> abstract method
2. OnPremiseStorage
    methods - 
    getSourceObject -> return either of APISource, FileSource, DataLakeSource based on reqType
3. CloudStorage
    methods - 
    getSourceObject -> return either of CloudAPISource, CloudFileSource, CloudDataLakeSource based on reqType
4. IngestToDB
    methods - 
    IngestData - abstract
5. APISource
6. FileSource
7. DataLakeSource
8. CloudAPISource
9. CloudFileSource
10. CloudDataLakeSource
"""

"""
Code Implementation
"""

# IngestToDB.py - Factory Pattern
from abc import ABC, abstractmethod
class IngestToDB(ABC):
    """
    Init @ IngestToDb
    """
    def __init__(self):
        pass

    """
    IngestData @ IngestToDB
    """
    @abstractmethod
    def IngestData(self):
        pass

# APISource.py
class APISource(IngestToDB):
    """
    Init @ APISource
    """
    def __init__(self):
        pass

    """
    Init @ APISource
    """
    def IngestData(self):
        print("Ingesting Data from API Source")


# DataLakeSource.py
class DataLakeSource(IngestToDB):
    """
    Init @ DataLakeSource
    """
    def __init__(self):
        pass

    """
    Init @ DataLakeSource
    """
    def IngestData(self):
        print("Ingesting Data from DataLake Source")


# FileSource.py
class FileSource(IngestToDB):
    """
    Init @ FileSource
    """
    def __init__(self):
        pass

    """
    Init @ FileSource
    """
    def IngestData(self):
        print("Ingesting Data from File Source")

# CloudAPISource.py
class CloudAPISource(IngestToDB):
    """
    Init @ CloudAPISource
    """
    def __init__(self):
        pass

    """
    Init @ CloudAPISource
    """
    def IngestData(self):
        print("Cloud: Ingesting Data from Cloud API Source")


# CloudDataLakeSource.py
class CloudDataLakeSource(IngestToDB):
    """
    Init @ CloudDataLakeSource
    """
    def __init__(self):
        pass

    """
    Init @ CloudDataLakeSource
    """
    def IngestData(self):
        print("Cloud: Ingesting Data from Cloud DataLake Source")


# CloudFileSource.py
class CloudFileSource(IngestToDB):
    """
    Init @ CloudFileSource
    """
    def __init__(self):
        pass

    """
    Init @ CloudFileSource
    """
    def IngestData(self):
        print("Cloud: Ingesting Data from Cloud File Source")


# IngestionService.py - Abstract Factory
class IngestionService(ABC):
    """
    Init @ IngestionService
    """
    def __init__(self):
        pass
    
    """
    IngestDataToDB @ IngestionService
    """
    def ingestDataToDB(self, source):
        sourceObject = self.getSourceInstance(source)
        sourceObject.IngestData()
    
    """
    getSourceInstance (abstract) @ IngestionService
    """
    @abstractmethod
    def getSourceInstance(self, source):
        pass

# CloudStorage.py
class CloudStorage(IngestionService):
    """
    Init @ CloudStorage
    """
    def __init__(self):
        pass
    
    """
    getSourceInstance (Ovveride) @ CloudStorage
    """
    def getSourceInstance(self, source):
        if(source == "API"):
            return CloudAPISource()
        elif(source == "FILE"):
            return CloudFileSource()
        elif(source == "DATALAKE"):
            return CloudDataLakeSource()
        else:
            print("Unknown source")

# OnPremiseStorage.py
class OnPremiseStorage(IngestionService):
    """
    Init @ OnPremiseStorage
    """
    def __init__(self):
        pass
    
    """
    getSourceInstance (Ovveride) @ OnPremiseStorage
    """
    def getSourceInstance(self, source):
        if(source == "API"):
            return APISource()
        elif(source == "FILE"):
            return FileSource()
        elif(source == "DATALAKE"):
            return DataLakeSource()
        else:
            print("Unknown source")
    
# StorageFactory.py
class StorageFactory:

    """
    Init @ StorageFactory
    """
    def __init__(self):
        pass
    
    """
    Storage Object @ StorageFactory
    """
    def getStorageObject(self, source):
        if(source == "CLOUD"):
            return CloudStorage()
        elif(source == "ONPREMISE"):
            return OnPremiseStorage()
        else:
            print("Unknown source")
            return None

# DataIngestionFramework.py
class DataIngestionFramework:
    """
    Init @ DataIngestionFramework
    """
    def __init__(self):
        pass

    """
    Ingest @ DataIngestionFramework
    """
    def ingest(self, storage, source):
        storageFactory = StorageFactory()
        storageObject = storageFactory.getStorageObject(storage)
        storageObject.ingestDataToDB(source)

"""
Testing
"""
DIFramework = DataIngestionFramework()
DIFramework.ingest("CLOUD", "API")
DIFramework.ingest("CLOUD", "FILE")
DIFramework.ingest("ONPREMISE", "DATALAKE")

