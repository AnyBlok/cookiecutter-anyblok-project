# This file is a part of the AnyBlok project
#
#    Copyright (C) 2018 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
import anyblok
from anyblok.blok import BlokManager
from anyblok.registry import RegistryManager
from anyblok.config import Configuration, get_url
from logging import getLogger
from sqlalchemy_utils.functions import database_exists, create_database

logger = getLogger(__name__)

Configuration.add_application_properties(
    'update-project', ['logging'], prog='AnyBlok update project, version')


def update_project():
    anyblok.load_init_function_from_entry_points()
    Configuration.load('update-project')
    anyblok.configuration_post_load()
    BlokManager.load()
    db_name = Configuration.get('db_name')
    logger.info("update project: db_name=%r", db_name)

    to_install = []
    to_update = []
    to_uninstall = []

    url = get_url()
    options = {}
    if not database_exists(url):
        db_template_name = Configuration.get('db_template_name', None)
        create_database(url, template=db_template_name)
        to_install.append('toolsapiblok')
        version = None
    else:
        options.update(dict(loadwithoutmigration=True))

    registry = RegistryManager.get(db_name, **options)
    registry.update_blok_list()  # case, new blok added
    version = registry.System.Blok.query().filter_by(
        name='{{ cookiecutter.blok_name }}').one().installed_version

    if version is None:
        pass
    else:
        to_update.append('toolsapiblok')

    registry.upgrade(install=to_install, update=to_update,
                     uninstall=to_uninstall)

    registry.commit()
    registry.close()
    logger.info("Project updated: db_name=%r", db_name)
