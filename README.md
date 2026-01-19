# Azure End-to-End Data Engineering Project

## Overview
This project implements a complete end-to-end data engineering pipeline on Azure, covering data ingestion, transformation, modeling, and serving. It demonstrates real-world data engineering practices using Azure-native services and Databricks, with a focus on scalability, incremental processing, and production-ready design.

## Architecture
- **Ingestion**: Azure Data Factory (incremental loads, backfilling, looping pipelines)
- **Storage & Processing**: Azure Databricks with PySpark
- **Governance**: Unity Catalog
- **Streaming**: Spark Structured Streaming with Databricks Auto Loader
- **Data Modeling**: Star Schema, Slowly Changing Dimensions (SCD)
- **Transformation**: Metadata-driven PySpark pipelines using Jinja2
- **Serving Layer**: Azure SQL Database
- **Reliability**: Delta Lake, Delta Live Tables
- **CI/CD**: Databricks Asset Bundles with GitHub integration

## Key Features
- Incremental and backfill-enabled ingestion pipelines  
- Metadata-driven transformations for reusability  
- Batch and streaming data processing  
- Dimensional data modeling with SCD implementation  
- Production-grade Delta Lake pipelines  
- CI/CD-ready Databricks workflows  

## Tech Stack
- Azure Data Factory  
- Azure Databricks  
- Azure SQL Database  
- PySpark & Apache Spark  
- Delta Lake & Delta Live Tables  
- Unity Catalog  
- GitHub  

## Use Case
Designed as a reference architecture for building scalable, maintainable, and enterprise-ready data platforms on Azure.

## Reference
This project is inspired by the end-to-end Azure Data Engineering walkthrough by Ansh Lamba and adapted as a hands-on implementation.

---
