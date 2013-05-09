# ckanext-usertesting

Custom CKAN extension for a user testing instance

## How to Install Locally for Development

1. Install CKAN from source.

2. Install ckanext-usertesting. Activate your CKAN virtual environment and:

        git clone git@github.com:okfn/ckanext-usertesting.git
        cd ckanext-usertesting
        python setup.py develop

3. Edit the following settings to the `[app:main]` section of your CKAN config
   file (e.g. `development.ini` or `sa.ini`):

        ckan.plugins = usertesting_customizations

4. Run CKAN, e.g. `paster serve usertesting.ini`

Note on CKAN versions: at the time of writing the `master` branch of
ckanext-usertesting is intended to work with CKAN 2.0 (currently the `master`
branch of ckan).