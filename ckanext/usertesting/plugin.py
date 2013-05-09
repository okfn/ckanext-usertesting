import os

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def popular_datasets(limit=4):
    '''Return a list of the most popular datasets on the site.'''
    response = toolkit.get_action('package_search')(
            data_dict={'sort': 'views_recent desc', 'rows': limit})
    return response['results']


def latest_datasets(limit=4):
    '''Return a list of the most popular datasets on the site.'''
    response = toolkit.get_action('package_search')(
            data_dict={'sort': 'metadata_modified desc', 'rows': limit})
    return response['results']


class UserTestingCustomizations(plugins.SingletonPlugin):
    plugins.implements(plugins.IRoutes)
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IConfigurable, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        here = os.path.dirname(__file__)
        rootdir = os.path.dirname(os.path.dirname(here))

        our_public_dir = os.path.join(rootdir, 'ckanext', 'usertesting', 'theme',
                'public')
        template_dir = os.path.join(rootdir, 'ckanext', 'usertesting', 'theme',
                'templates')
        config['extra_public_paths'] = ','.join([our_public_dir,
                config.get('extra_public_paths', '')])
        config['extra_template_paths'] = ','.join([template_dir,
                config.get('extra_template_paths', '')])

        toolkit.add_resource('theme/resources', 'ckanext-usertesting')

    def before_map(self, route_map):
        return route_map

    def after_map(self, route_map):
        return route_map

    def get_helpers(self):
        return {
                'popular_datasets': popular_datasets,
                'latest_datasets': latest_datasets,
                }
