# Script Version Compatibility

## ClarityNLP
Note: ClarityNLP Lite is not version controlled at this time. Please always use the "latest" tag for docker images or the current contents of the related branch in the repository alongside the "latest" folder SQL scripts provided here.

## Registry Manager - Vocababulary
The "vocab" schema uses the OMOP Common Data Model 5.4.

OMOP SQL Scripts pulled from https://github.com/OHDSI/CommonDataModel/tree/main/inst/ddl/5.4/postgresql on **December 5th, 2023**.

## Registry Manager - Condition Registry
Each individual registry uses an extended version of the OMOP Common Data Model 5.4, which includes additional table support for FHIR, case management, and some modifications to field types in the base OMOP 5.4 specification.

  Viewer Manager Version | Script Version
-------------------------|-----------------
  ??                     | 1.0.0

## Registry Viewer API
The Registry Viewer API uses the "viewer" schema.

  Viewer API Version | Script Version
---------------------|-----------------
  < 1.6.2            | 1.0.0
  1.6.2+             | 1.1.0