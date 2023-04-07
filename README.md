# My Python Package Template

This is a Python package for interacting with my service.


## Installation

You can install the package using pip:

Run the command ```python setup.py sdist``` in the top-level package directory. This command creates a source distribution of your package in the `dist/` directory.

On the target system, run `pip install <path_to_tar_gz_file>` to install your package (wiwthout uploading to pip).

## Upload to AWS CodeArtifact
* NOT tested yet
pip install twine

```
twine upload --repository-url https://my-domain-123.d.codeartifact.us-west-2.amazonaws.com/pypi/my-repo/ --username AWS --password "$(aws codeartifact get-authorization-token --domain my-domain --query authorizationToken --output text)" dist/*
```
OR
```
aws codeartifact push-package-version --repository myrepo --namespace mynamespace --package package_template --format pypi --version 0.1.0 --s3-object-version <S3_OBJECT_VERSION_ID> --asset <PATH_TO_DIST_FILE>
```  
