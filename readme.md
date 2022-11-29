# AWS Lambda to pull Crowdstrike sample results

This program is written to be implemented as a Lambda function in AWS. It calls the Crowdstrike Falcon API to pull submission results.
It can be used as standalone code or without secrets management with minor modifications

The FalconPy module for a Lambda layer can be downloaded from here: https://github.com/CrowdStrike/falconpy/discussions/496
